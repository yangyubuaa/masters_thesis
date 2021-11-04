import json
import re
from tqdm import tqdm
add_punc = '''，,。、【 】 “”"：:；;'（）〔〕《》‘’{}？！()、×*'''
new_lists = []
with open('dapt_data/abstract.json', 'r', encoding='utf-8') as f:
    count = 0
    for l in tqdm(f):
        tmp = json.loads(l)
        texts = re.sub("[%s]+" % add_punc, "", tmp[0])
        title = re.sub("[%s]+" % add_punc, "", tmp[1])
        new_lists.append((texts, title))
    with open('dapt_data/dapt_train_prepared.json', 'w', encoding='utf-8') as f1:
        for d in new_lists:
            f1.write(json.dumps(d, ensure_ascii=False) + '\n')
f.close()
f1.close()
print("处理完毕")