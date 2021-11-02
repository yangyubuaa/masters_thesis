'''
使用pegasus原始论文的方法进行伪摘要数据集的构建，并进行dapt
'''
from bert4keras.snippets import text_segmentate
import jieba
import json
import numpy as np
from tqdm import tqdm
from rouge import Rouge

import yaml

# 基本参数
maxlen = 512
batch_size = 96
epochs = 100000
summary_rate = 0.25
t_maxlen = maxlen // 4
s_maxlen = maxlen - t_maxlen


class PegasusPrincipalMethodGenerator:
    '''复现pegasus原始论文的伪代码，进行伪摘要数据集的生成
    '''
    def __init__(self, config):
        self.config = config
        self.clear_corpus_path = config["clear_corpus_path"]
        self.rouge = Rouge()
    
    def generate(self):
        '''调用函数进行伪摘要数据集生成
        '''
        D = []
        texts_list = self.__corpus()
        # for texts in tqdm(texts_list):
        #     source, target = pseudo_summary(texts)
        #     D.append((source, target))
        # source, target = pseudo_summary(texts_list[0])
        with open('abstract.json', 'a+', encoding='utf-8') as f:
            for texts in tqdm(texts_list):
                # 对每个裁判文书文本调用伪摘要生成代码
                source, target = self.__pseudo_summary(texts)
                print(source, "_____", target)
                # 测试用
                break
                f.write(json.dumps([source, target], ensure_ascii=False) + '\n')
            # f.write(json.dumps([source, target], ensure_ascii=False) + '\n')

    def __compute_rouge(self, source, target, unit='word'):
        """计算rouge-1、rouge-2、rouge-l
        """
        if unit == 'word':
            source = jieba.cut(source, HMM=False)
            target = jieba.cut(target, HMM=False)
        source, target = ' '.join(source), ' '.join(target)
        try:
            scores = self.rouge.get_scores(hyps=source, refs=target)
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

    def __corpus(self):
        """读取clear语料
        """
        D = []
        temp = []
        # f = 'dapt_data/corpus.json'
        f = self.clear_corpus_path
        with open(f, 'r', encoding='utf-8') as f:
            for l in f:
                l = json.loads(l)
                # 将没有真实label的数据读取，用于生成伪摘要
                temp = self.__text_process(l[0])
                D.append(temp)
        return D

    def __text_process(self, text):
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


    def __gather_join(self, texts, idxs):
        """取出对应的text，然后拼接起来
        """
        return ''.join([texts[i] for i in idxs])


    def __pseudo_summary(self, texts):
        """根据一段texts构建伪标签数据对
        """
        print(texts)  # 测试用
        source_idxs, target_idxs = list(range(len(texts))), []
        print(source_idxs)  # 测试用
        while True:
            sims = []
            # 对于输入的每一个句子
            for i in source_idxs:
                # 得到其他句子构成的索引
                new_source_idxs = [j for j in source_idxs if j != i]
                # 把当前扫描到的句子加入目标句子
                new_target_idxs = sorted(target_idxs + [i])
                # 构建样本进行rouge计算
                new_source = self.__gather_join(texts, new_source_idxs)
                new_target = self.__gather_join(texts, new_target_idxs)
                sim = self.__compute_rouge(new_source, new_target, 'char')
                # sim = pylcs.lcs(new_source, new_target)
                sims.append(sim['rouge-l'])
            new_idx = source_idxs[np.argmax(sims)]
            source_idxs.remove(new_idx)
            target_idxs = sorted(target_idxs + [new_idx])
            source = self.__gather_join(texts, source_idxs)
            target = self.__gather_join(texts, target_idxs)
            if (
                len(source_idxs) == 1 or
                1.0 * len(target) / len(source) > summary_rate
            ):
                break
        if len(source) < len(target):
            source, target = target, source
        return source, target


if __name__=='__main__':
    with open(r'generate_dapt_corpus_pegasus_paper_principal.yaml', 'r', encoding='utf-8') as f:
        result = f.read()
        config = yaml.load(result)
    p = PegasusPrincipalMethodGenerator(config)
    p.generate()
    