#coding:utf-8
'''
使用pegasus原始论文中的ind/origin方式进行dapt的模型代码
'''

import sys
sys.path.append("../../")
print(sys.path)
from mytransformers.models.t5 import T5Model
    

if __name__=="__main__":
    m = T5Model()