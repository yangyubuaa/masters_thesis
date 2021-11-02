#-*- coding: utf-8 -*-
import re
import os
from zipfile import ZipFile
from bs4 import BeautifulSoup
import json

data_path = "F:\\NLP\\数据集\\全国\\docx"
filename_data_path = "../documents_name/judgement_documents_names_cls"
cls_filename_list = os.listdir(filename_data_path)
# print(cls_filename_list[0][2:-4])
path = '../documents_name/process_data_cls'

for k in range(27, len(cls_filename_list)):
    dict = []
    path_cls = os.path.join(path, cls_filename_list[k][:-4] + '.json')
    names = os.path.join(filename_data_path, cls_filename_list[k])
    filename_list = open(names, "r", encoding='utf-8').readlines()
    for filename in filename_list:
        print(filename)
        filename = filename.replace('\n', '')
        # 读取某一个裁判书
        file = os.path.join(data_path, filename)
        document = ZipFile(file)
        xml = document.read("word/document.xml")
        wordObj = BeautifulSoup(xml.decode("utf-8"))
        sentences = wordObj.findAll("w:t")
        # # 添加罪名至第一行
        # paragraph_list = []
        # paragraph_list.append(cls_filename_list[k][3:-4])

        paragraph_list = []
        for p in sentences:
            sentence = p.text
            if '。' in sentence:
                paragraph_list.append(p.text)

        texts = []
        summary = []
        r0 = r'本院认为|本院意见(.*?)构成(.*?)罪'
        r1 = r'(依照)*(.*?)《中华人民共和国刑(.*?)法》第(.*?)条(.*?)(判决如下)*'
        # 查找 原文 部分
        for para in paragraph_list:
            if re.match(r0, para):
                break
            texts.append(para)

        # 查找 本院认为 部分
        summary = [para for para in paragraph_list if para not in texts]
        # for para in paragraph_list:
        #     temp = paragraph_list[i].replace(' ', '')
        #     summary.append(temp)

        summary_text = '。'.join(summary)
        summary_sentences = summary_text.split('。')

        court_view_list = []
        for sen in summary_sentences:
            if re.match(r1, sen):
                break
            court_view_list.append(sen)
        court_view = '。'.join(court_view_list)

        dict.append((texts, court_view))

    with open(path_cls, 'w', encoding='utf-8') as f:
        for d in dict:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

    print(cls_filename_list[k][:-4] + '读取完成')