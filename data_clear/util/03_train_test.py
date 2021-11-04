#-*- coding: utf-8 -*-
import os
import json
import numpy as np

raw_path = '../documents_name/process_data_cls_1'
res_path = '../datasets'
train_path = os.path.join(res_path, 'train_new.json')
test_path = os.path.join(res_path, 'test_new.json')
valid_path = os.path.join(res_path, 'valid_new.json')

cls_filenames_list = os.listdir(raw_path)
print(cls_filenames_list)

train = []
test = []
valid = []
for name in cls_filenames_list:
    path = os.path.join(raw_path, name)
    with open(path, "r", encoding='utf-8') as f:
        lists = f.readlines()
        size = len(lists)
        test_size = int(0.02 * size)
        valid_size = test_size + int(0.1 * size)
        print(size, test_size)

        idxs = list(range(size))
        np.random.shuffle(idxs)
        lists = [lists[i] for i in idxs]

        count = 0
        for l in lists:
            if count < test_size:
                test.append(json.loads(l))
            elif count < valid_size:
                valid.append(json.loads(l))
            else:
                train.append(json.loads(l))
            count += 1

with open(test_path, 'w', encoding='utf-8') as f:
    for d in test:
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
print("测试集读取完毕")

with open(valid_path, 'w', encoding='utf-8') as f:
    for d in valid:
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
print("验证集读取完毕")

with open(train_path, 'w', encoding='utf-8') as f:
    for d in train:
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
print("训练集读取完毕")