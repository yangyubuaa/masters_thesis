'''
根据dapt_data文件夹中的数据得到data,需要根据不同的mask策略动态构建不同的数据集
'''

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
        # 使用autoencoder的方式进行pta
        if is_autoencoder:
            autoencoder_dataset = self.autoencoder_edition_generate()
        # 根据stage返回动态构建的数据集
        # 论文里面的版本
        if self.stage == "pegasus_source_edition":
            dataset = self.pegasus_source_edition_generate()
        # 我们的版本
        elif self.stage == "pegasus_our_edition":
            dataset = self.pegasus_our_edition_generate()
    def autoencnder_edition_generate(self):
        return 
    def pegasus_source_edition(self):
        if is_random_mask:
        else:

    def pegasus_our_edition(self):
        if is_random_mask:
        else:
