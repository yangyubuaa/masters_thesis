#! -*- coding: utf-8 -*-
'''
根据dape_prepare生成的dapt_data文件夹中的seg_corpus.json数据得到data,需要根据不同的mask策略动态构建不同的数据集
'''
import yaml
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
        print(store_name)

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
            return None
    def pegasus_permute_edition_generage(self):
        if self.is_random_mask:
            return None
        else:
            return None

if __name__=="__main__":
    with open(r'getdata.yaml', 'r', encoding='utf-8') as f:
        result = f.read()
        config = yaml.load(result)
    print(config)
    getdata = GetData(config)
    getdata.get_data()