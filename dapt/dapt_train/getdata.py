#! -*- coding: utf-8 -*-
'''
根据dape_prepare生成的dapt_data文件夹中的seg_corpus.json数据得到data,需要根据不同的mask策略动态构建不同的数据集
'''
import yaml

import json

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import numpy as np

from tqdm import tqdm

class GetData:
    def __init__(self, config):
        self.config = config
        self.prepared_data_path = config["data_path"]["prepared_data_path"]
        self.autoencoder_data_path = config["data_path"]["autoencoder_data_path"]
        # 是否混合autoendocer和mask的训练过程
        self.is_autoencoder = config["is_autoencoder"]
        self.stage = config["stage"]
        self.gsr = config["gsr"]
        # 是否采用random mask
        self.is_random_mask = config["is_random_mask"]
        self.random_mask_rate = config["random_mask_rate"]
        self.store_name = None

    def get_data(self):
        store_name = "pta_"
        if self.is_autoencoder:
            store_name = store_name + "autoendocer_"
        else:
            store_name = store_name + ""
        if self.stage == "pegasus_source_edition":
            store_name = store_name + "source_"
        else:
            store_name = store_name + "permute_"
        store_name = store_name + "gsr_" + str(self.gsr)
        if self.is_random_mask:
            store_name = store_name + "_rmrate_" + str(self.random_mask_rate)
        store_name = store_name + ".json"
        self.store_name = store_name

        '''
        判断store_name的文件是否存在，存在则直接读取，不存在则生成
        '''
        
        '''
        生成
        '''
        # 使用autoencoder的方式进行pta
        if self.is_autoencoder:
            autoencoder_dataset = self.autoencoder_edition_generate()
        # 根据stage返回动态构建的数据集
        # 论文里面的版本
        if self.stage == "pegasus_source_edition":
            dataset = self.pegasus_source_edition_generate()
        # 我们的版本
        elif self.stage == "pegasus_permute_edition":
            dataset = self.pegasus_permute_edition_generate()

    def autoencoder_edition_generate(self):
        return None

    def pegasus_source_edition_generate(self):
        if self.is_random_mask:
            return None
        else:
            print(self.prepared_data_path)
            data_pair = list()
            with open(self.prepared_data_path, "r", encoding="utf-8") as prepared_file:
                for line in tqdm(prepared_file):
                    texts, scores = json.loads(line)
                    # print(scores)
                    # print(source_index)
                    target_length = int(self.gsr * len(texts)) + 1
                    topk_idx, else_idx = self.__get_top_k(target_length, texts, scores)
                    input = ""
                    label = ""
                    for index in else_idx:
                        input = input + texts[index]
                    for index in topk_idx:
                        label = label + texts[index]
                    # print(input)
                    # print(label)
                    data_pair.append([input, label])
            with open(self.store_name, "w") as w:
                for d in data_pair:
                    w.write(json.dumps(d))
            return None

    def pegasus_permute_edition_generage(self):
        if self.is_random_mask:
            return None
        else:
            return None

    def __get_top_k(self, k, texts, scores):
        '''得到top k的index以及剩余的index
        '''
        np_scores = np.array(scores)
        source_index = list(np.argsort(np_scores))
        topk_index = source_index[-k:]
        else_index = [i for i in range(len(scores)) if i not in topk_index]
        topk_index_sorted = sorted(topk_index)
        else_index_sorted = sorted(else_index)
        return topk_index_sorted, else_index_sorted



if __name__=="__main__":
    with open(r'getdata.yaml', 'r', encoding='utf-8') as f:
        result = f.read()
        config = yaml.load(result)
    print(config)
    getdata = GetData(config)
    getdata.get_data()