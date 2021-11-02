# -*- coding: utf-8 -*-

import os
import json
import re
from string import punctuation

add_punc = '，。、【 】 “”：；（）〔〕《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥'
all_punc = punctuation + add_punc

raw_path = '../documents_name/process_data_cls'
res_path = '../documents_name/process_data_cls_1'

cls_filenames_list = os.listdir(raw_path)
print(cls_filenames_list)

for name in cls_filenames_list:
    path = os.path.join(raw_path, name)
    new_lists = []
    with open(path, 'r', encoding='utf-8') as f:
        lists = f.readlines()
        for l in lists:
            temp = json.loads(l)
            # print(len(temp[1]))
            texts = ''.join(temp[0][1:])
            # 如果不想去掉标点符号就不要这两行
            texts = re.sub("[%s]+" % all_punc, "", texts)
            title = re.sub("[%s]+" % all_punc, "", temp[1])
            if len(title) == 0 or len(title) > 500:
                continue
            new_lists.append((texts, title))
    new_filenames = os.path.join(res_path, name)
    with open(new_filenames, 'w', encoding='utf-8') as f1:
        for d in new_lists:
            f1.write(json.dumps(d, ensure_ascii=False) + '\n')
    print(name + "处理完毕")