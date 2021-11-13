'''
预训练
'''
import torch
from torch.data.utils import Dataloader
from torch.data.utils import Dataset

import sys
sys.path.append("../../")

from mytransformers.models.t5 import T5ForConditionalGeneration
from mytransformers.models.t5.tokenization_t5 import T5Tokenizer
from model_principal import T5PrincipalPta

from getdata import GetData

class PtaDataset(Dataset):
    def __init__(self):
        pass
    def __getitem__(self):
        pass
    def __len__(self):
        pass

class Trainer:
    def __init__(self, config):
        self.config = config
        self.source_data_generator = GetData(config)
        self.dataset = None

    def train(self):
        self.dataset = self.__dataset()

    def evaluate(self):
        pass
    
    def __dataset(self):
        '''根据soure_data_generator生成的数据进行tokenizer并封装为Dataset类
        '''
        tokenizer = T5Tokenizer(self.config["model_path"])
                


if __name__=="__main__":
    with open(r'train_one_stage.yaml', 'r', encoding='utf-8') as f:
        result = f.read()
        config = yaml.load(result)
    trainer = Trainer(config)