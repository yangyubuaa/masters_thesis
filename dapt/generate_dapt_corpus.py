from bert4keras.snippets import text_segmentate
import jieba
import json
import numpy as np
from tqdm import tqdm
from rouge import Rouge

# 基本参数
maxlen = 512
batch_size = 96
epochs = 100000
summary_rate = 0.25
t_maxlen = maxlen // 4
s_maxlen = maxlen - t_maxlen


def compute_rouge(rouge, source, target, unit='word'):
    """计算rouge-1、rouge-2、rouge-l
    """
    if unit == 'word':
        source = jieba.cut(source, HMM=False)
        target = jieba.cut(target, HMM=False)
    source, target = ' '.join(source), ' '.join(target)
    try:
        scores = rouge.get_scores(hyps=source, refs=target)
        return {
            'rouge-1': scores[0]['rouge-1']['f'],
            'rouge-2': scores[0]['rouge-2']['f'],
            'rouge-l': scores[0]['rouge-l']['f'],
        }
    except ValueError:
        return {
            'rouge-1': 0.0,
            'rouge-2': 0.0,
            'rouge-l': 0.0,
        }


def corpus():
    """语料生成器
    """
    D = []
    temp = []
    f = 'dapt_data/corpus.json'
    with open(f, 'r', encoding='utf-8') as f:
        for l in f:
            l = json.loads(l)
            temp = text_process(l[0])
            D.append(temp)
    return D


def text_process(text):
    """分割文本
    """
    texts = text_segmentate(text, 32, u'\n。')
    result, length = [], 0
    for text in texts:
        if length + len(text) > maxlen * 1.5 and len(result) >= 3:
            return result
        result.append(text)
        length += len(text)
    if result and len(result) >= 3:
        return result


def gather_join(texts, idxs):
    """取出对应的text，然后拼接起来
    """
    return ''.join([texts[i] for i in idxs])


def pseudo_summary(texts, rouge):
    """构建伪标签摘要数据集
    """
    source_idxs, target_idxs = list(range(len(texts))), []
    while True:
        sims = []
        for i in source_idxs:
            new_source_idxs = [j for j in source_idxs if j != i]
            new_target_idxs = sorted(target_idxs + [i])
            new_source = gather_join(texts, new_source_idxs)
            new_target = gather_join(texts, new_target_idxs)
            sim = compute_rouge(rouge, new_source, new_target, 'char')
            # sim = pylcs.lcs(new_source, new_target)
            sims.append(sim['rouge-l'])
        new_idx = source_idxs[np.argmax(sims)]
        source_idxs.remove(new_idx)
        target_idxs = sorted(target_idxs + [new_idx])
        source = gather_join(texts, source_idxs)
        target = gather_join(texts, target_idxs)
        if (
            len(source_idxs) == 1 or
            1.0 * len(target) / len(source) > summary_rate
        ):
            break
    if len(source) < len(target):
        source, target = target, source
    return source, target


if __name__=='__main__':
    D = []
    # 计算rouge用
    rouge = Rouge()
    texts_list = corpus()
    # for texts in tqdm(texts_list):
    #     source, target = pseudo_summary(texts)
    #     D.append((source, target))
    # source, target = pseudo_summary(texts_list[0])
    texts_list = texts_list[75467:]
    with open('abstract.json', 'a+', encoding='utf-8') as f:
        for texts in tqdm(texts_list):
            source, target = pseudo_summary(texts, rouge)
            f.write(json.dumps([source, target], ensure_ascii=False) + '\n')
        # f.write(json.dumps([source, target], ensure_ascii=False) + '\n')