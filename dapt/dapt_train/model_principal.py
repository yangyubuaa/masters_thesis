#coding:utf-8
'''
使用pegasus原始论文中的ind/origin方式进行dapt的模型代码
'''

import sys
sys.path.append("../../")

import torch

import yaml

from mytransformers.models.t5 import T5ForConditionalGeneration
from mytransformers.models.t5.tokenization_t5 import T5Tokenizer


class T5PrincipalPta(torch.nn.Module):
    def __init__(self, config):
        super(T5PrincipalPta, self).__init__()
        self.config = config
        self.model_path = self.config["model_path"]
        self.mt5_model = T5ForConditionalGeneration.from_pretrained(self.model_path)

    def forward(self, input_ids, labels):
        return self.mt5_model(input_ids=input_ids, labels=labels)

    def generate(self, input_ids):
        output = self.mt5_model.generate(input_ids=input_ids)
        output_token_ids = output.numpy().tolist()
        return output_token_ids

if __name__=="__main__":
    with open(r'model_principal.yaml', 'r', encoding='utf-8') as f:
        result = f.read()
        config = yaml.load(result)
    model = T5PrincipalPta(config)
    tokenizer = T5Tokenizer.from_pretrained(config["model_path"])
    input_ids = tokenizer('将中文翻译成英文：我爱你', return_tensors='pt').input_ids
    labels = tokenizer('Das Haus ist wunderbar.', return_tensors='pt').input_ids
    print(input_ids, labels)
    print(input_ids.numpy().tolist()[0])
    print(tokenizer.decode(input_ids.numpy().tolist()[0]))
