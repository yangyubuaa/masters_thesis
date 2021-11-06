# -*- coding:utf-8 -*-
import re
import yaml
import json
from tqdm import tqdm


class SentenceSegmentation:
    def __init__(self, config):
        self.config = config
        self.clear_corpus_path = self.config["clear_corpus_path"]
        self.seg_corpus_path = self.config["seg_corpus_path"]

    def generate(self):
        texts_list = self.__corpus()
        with open(self.seg_corpus_path, 'a+', encoding='utf-8') as f:
            for texts in tqdm(texts_list):
                seg_sen = self.__cut_sentence(texts, 1, u'\n。.；;：:，,（）()')
                f.write(json.dumps(seg_sen, ensure_ascii=False) + '\n')

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
                temp = l[0]
                D.append(temp)
        return D

    def __cut_sentence(self, text, maxlen, seps='\n', strips=None):
        """将文本按照标点符号划分为若干个短句
        """
        text = text.strip().strip(strips)
        if seps and len(text) > maxlen:
            pieces = text.split(seps[0])
            text, texts = '', []
            for i, p in enumerate(pieces):
                if text and p and len(text) + len(p) > maxlen - 1:
                    texts.extend(self.__cut_sentence(text, maxlen, seps[1:], strips))
                    text = ''
                if i + 1 == len(pieces):
                    text = text + p
                else:
                    text = text + p + seps[0]
            if text:
                texts.extend(self.__cut_sentence(text, maxlen, seps[1:], strips))
            return texts
        else:
            return [text]


if __name__ == '__main__':
    with open(r'sentence_segmentation.yaml', 'r', encoding='utf-8') as f:
        result = f.read()
        config = yaml.load(result)

    p = SentenceSegmentation(config)
    p.generate()