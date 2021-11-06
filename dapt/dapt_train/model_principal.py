#coding:utf-8
'''
使用pegasus原始论文中的ind/origin方式进行dapt的模型代码
'''

import sys
sys.path.append("../../")

import torch

from mytransformers.models.t5 import T5ForConditionalGeneration
from mytransformers.models.t5.tokenization_t5 import T5Tokenizer


class T5PrincipalPta(torch.nn.Module):
    def __init__(self):
        super(T5PrincipalPta, self).__init__()
        self.mt5_model = T5ForConditionalGeneration.from_pretrained("../dapt_model/mt5-small-simplify")

    def forward(self, input_ids, labels):
        return self.mt5_model(input_ids=input_ids, labels=labels)

    def generate(self, input_ids):
        output = self.mt5_model.generate(input_ids=input_ids)
        output_token_ids = output.numpy().tolist()
        return output_token_ids

if __name__=="__main__":
    model = T5PrincipalPta()
    tokenizer = T5Tokenizer.from_pretrained("../dapt_model/mt5-small-simplify")
    input_ids = tokenizer('将中文翻译成英文：我爱你', return_tensors='pt').input_ids
    labels = tokenizer('Das Haus ist wunderbar.', return_tensors='pt').input_ids
    print(input_ids, labels)
    print(input_ids.numpy().tolist()[0])
    print(tokenizer.decode(input_ids.numpy().tolist()[0]))
