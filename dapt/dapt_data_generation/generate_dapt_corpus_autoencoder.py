'''
使用输入样本构建输入-输出，输入和输出样本相同，即把输入样本复制一遍即可，对pegasus进行预训练，类似于训练自编码器
此任务作为pegasus任务的基础上的第一次dapt，实验比较是否有效果
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


class AutoEncoderMethodGenerator:
    '''使用auto encoder方式进行伪摘要数据集的生成
    '''
    def __init__(self, config):
        self.config = config
        self.clear_corpus_path = self.config["clear_corpus_path"]
        self.pseudo_summary_path = self.config["pseudo_summary_path"]
    
    def generate(self):
        '''调用函数进行伪摘要数据集生成
        '''
        D = []
        texts_list = self.__corpus()
        # for texts in tqdm(texts_list):
        #     source, target = pseudo_summary(texts)
        #     D.append((source, target))
        # source, target = pseudo_summary(texts_list[0])
        with open(self.pseudo_summary_path, 'a+', encoding='utf-8') as f:
            for texts in tqdm(texts_list):
                # 对每个裁判文书文本调用伪摘要生成代码
                source, target = texts, texts
                # 测试用
                f.write(json.dumps([source, target], ensure_ascii=False) + '\n')
            # f.write(json.dumps([source, target], ensure_ascii=False) + '\n')

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
            
if __name__=='__main__':
    with open(r'generate_dapt_corpus_autoencoder.yaml', 'r', encoding='utf-8') as f:
        result = f.read()
        config = yaml.load(result)
    p = AutoEncoderMethodGenerator(config)
    p.generate()
    