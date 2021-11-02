import os

filename_path = '../documents_name/judgement_documents_names_cls'

charge_dict = {"交通肇事罪": 0, "危险驾驶罪": 1, "重大责任事故罪": 2, "生产销售": 3, "走私贩卖运输制造毒品罪": 4, "非法吸收公众存款罪": 5,
               "信用卡诈骗罪": 6, "合同诈骗罪": 7, "诈骗罪": 8,  "逃税罪": 9, "假冒注册商标罪": 10, "组织领导传销活动罪": 11, "非法经营罪": 12,
               "过失致人死亡罪": 13, "故意伤害罪": 14, "强奸罪": 15, "非法拘禁罪": 16, "侵犯公民个人信息罪": 17, "抢劫罪": 18, "盗窃罪": 19,
               "职务侵占罪": 20, "挪用资金罪": 21, "敲诈勒索罪": 22, "故意毁坏财物罪": 23, "拒不支付劳动报酬罪": 24, "妨害公务罪": 25,
               "伪造变造买卖国家机关公文证件印章罪": 26, "聚众斗殴罪": 27, "寻衅滋事罪": 28, "赌博罪": 29, "开设赌场罪": 30,
               "拒不执行判决裁定罪": 31, "污染环境罪": 32, "非法捕捞水产品罪": 33, "非法狩猎罪": 34, "非法占用农用地罪": 35, "非法采矿罪": 36,
               "滥伐林木罪": 37, "非法持有毒品罪": 38, "容留他人吸毒罪": 39, "引诱容留介绍卖淫罪": 40, "贪污罪": 41, "受贿罪": 42}
data_path = "F:\\NLP\\数据集\\全国\\docx"
filelist = os.listdir(data_path)
print('原裁判文书个数为：%d' % (len(filelist)))

'''
1. 保留只含一种罪名的裁判书
'''
file_list = [file for file in filelist if (file.count('罪') == 1) and ('二审' not in file)]
print('去掉二审且只含一种罪名的裁判文书个数为：%d' % (len(file_list)))

'''
2. 交通肇事罪裁判书名称提取并保存
'''
list_0 = [file for file in file_list if ('交通肇事罪' in file)]
file_list = [file for file in file_list if file not in list_0]
print('交通肇事罪裁判文书个数为：%d' % (len(list_0)))
file_0 = open(filename_path + '/00_交通肇事罪.txt', 'w+', encoding='utf-8')
for file in list_0:
    file_0.write(file + '\n')

'''
3. 危险驾驶罪裁判书名称提取并保存
'''
list_1 = [file for file in file_list if ('危险驾驶罪' in file)]
file_list = [file for file in file_list if file not in list_1]
print('危险驾驶罪裁判文书个数为：%d' % (len(list_1)))
file_1 = open(filename_path + '/01_危险驾驶罪.txt', 'w+', encoding='utf-8')
for file in list_1:
    file_1.write(file + '\n')

'''
4. 重大责任事故罪裁判书名称提取并保存
'''
list_2 = [file for file in file_list if ('重大责任事故罪' in file)]
file_list = [file for file in file_list if file not in list_2]
print('重大责任事故罪裁判文书个数为：%d' % (len(list_2)))
file_2 = open(filename_path + '/02_重大责任事故罪.txt', 'w+', encoding='utf-8')
for file in list_2:
    file_2.write(file + '\n')

'''
5. 生产销售XXX罪裁判书名称提取并保存
'''
list_3 = [file for file in file_list if ('生产销售' in file)]
file_list = [file for file in file_list if file not in list_3]
print('生产销售XXX罪裁判文书个数为：%d' % (len(list_3)))
file_3 = open(filename_path + '/03_生产销售.txt', 'w+', encoding='utf-8')
for file in list_3:
    file_3.write(file + '\n')

'''
6. 走私贩卖运输制造毒品罪裁判书名称提取并保存
'''
list_4 = [file for file in file_list if ('走私贩卖运输制造毒品罪' in file)]
file_list = [file for file in file_list if file not in list_4]
print('走私贩卖运输制造毒品罪裁判文书个数为：%d' % (len(list_4)))
file_4 = open(filename_path + '/04_走私贩卖运输制造毒品罪.txt', 'w+', encoding='utf-8')
for file in list_4:
    file_4.write(file + '\n')

'''
7. 非法吸收公众存款罪裁判书名称提取并保存
'''
list_5 = [file for file in file_list if ('非法吸收公众存款罪' in file)]
file_list = [file for file in file_list if file not in list_5]
print('非法吸收公众存款罪裁判文书个数为：%d' % (len(list_5)))
file_5 = open(filename_path + '/05_非法吸收公众存款罪.txt', 'w+', encoding='utf-8')
for file in list_5:
    file_5.write(file + '\n')

'''
8. 信用卡诈骗罪裁判书名称提取并保存
'''
list_6 = [file for file in file_list if ('信用卡诈骗罪' in file)]
file_list = [file for file in file_list if file not in list_6]
print('信用卡诈骗罪裁判文书个数为：%d' % (len(list_6)))
file_6 = open(filename_path + '/06_信用卡诈骗罪.txt', 'w+', encoding='utf-8')
for file in list_6:
    file_6.write(file + '\n')

'''
9. 合同诈骗罪裁判书名称提取并保存
'''
list_7 = [file for file in file_list if ('合同诈骗罪' in file)]
file_list = [file for file in file_list if file not in list_7]
print('合同诈骗罪裁判文书个数为：%d' % (len(list_7)))
file_7 = open(filename_path + '/07_合同诈骗罪.txt', 'w+', encoding='utf-8')
for file in list_7:
    file_7.write(file + '\n')

'''
10. 诈骗罪裁判书名称提取并保存
'''
list_8 = [file for file in file_list if ('诈骗罪' in file and '集资' not in file and '贷款' not in file and '票据' not in file
          and '金融凭证' not in file and '保险' not in file and '合同' not in file)]
file_list = [file for file in file_list if file not in list_8]
print('诈骗罪裁判文书个数为：%d' % (len(list_8)))
file_8 = open(filename_path + '/08_诈骗罪.txt', 'w+', encoding='utf-8')
for file in list_8:
    file_8.write(file + '\n')

'''
11. 逃税罪裁判书名称提取并保存
'''
list_9 = [file for file in file_list if ('逃税罪' in file)]
file_list = [file for file in file_list if file not in list_9]
print('逃税罪裁判文书个数为：%d' % (len(list_9)))
file_9 = open(filename_path + '/09_逃税罪.txt', 'w+', encoding='utf-8')
for file in list_9:
    file_9.write(file + '\n')

'''
12. 假冒注册商标罪裁判书名称提取并保存
'''
list_10 = [file for file in file_list if ('假冒注册商标罪' in file)]
file_list = [file for file in file_list if file not in list_10]
print('假冒注册商标罪裁判文书个数为：%d' % (len(list_10)))
file_10 = open(filename_path + '/10_假冒注册商标罪.txt', 'w+', encoding='utf-8')
for file in list_10:
    file_10.write(file + '\n')

'''
13. 组织领导传销活动罪裁判书名称提取并保存
'''
list_11 = [file for file in file_list if ('组织领导传销活动罪' in file)]
file_list = [file for file in file_list if file not in list_11]
print('组织领导传销活动罪裁判文书个数为：%d' % (len(list_11)))
file_11 = open(filename_path + '/11_组织领导传销活动罪.txt', 'w+', encoding='utf-8')
for file in list_11:
    file_11.write(file + '\n')

'''
14. 非法经营罪裁判书名称提取并保存
'''
list_12 = [file for file in file_list if ('非法经营罪' in file)]
file_list = [file for file in file_list if file not in list_12]
print('非法经营罪裁判文书个数为：%d' % (len(list_12)))
file_12 = open(filename_path + '/12_非法经营罪.txt', 'w+', encoding='utf-8')
for file in list_12:
    file_12.write(file + '\n')

'''
15. 过失致人死亡罪裁判书名称提取并保存
'''
list_13 = [file for file in file_list if ('过失致人死亡罪' in file)]
file_list = [file for file in file_list if file not in list_13]
print('过失致人死亡罪裁判文书个数为：%d' % (len(list_13)))
file_13 = open(filename_path + '/13_过失致人死亡罪.txt', 'w+', encoding='utf-8')
for file in list_13:
    file_13.write(file + '\n')

'''
16. 故意伤害罪裁判书名称提取并保存
'''
list_14 = [file for file in file_list if ('故意伤害罪' in file)]
file_list = [file for file in file_list if file not in list_14]
print('故意伤害罪裁判文书个数为：%d' % (len(list_14)))
file_14 = open(filename_path + '/14_故意伤害罪.txt', 'w+', encoding='utf-8')
for file in list_14:
    file_14.write(file + '\n')

'''
17. 强奸罪裁判书名称提取并保存
'''
list_15 = [file for file in file_list if ('强奸罪' in file)]
file_list = [file for file in file_list if file not in list_15]
print('强奸罪裁判文书个数为：%d' % (len(list_15)))
file_15 = open(filename_path + '/15_强奸罪.txt', 'w+', encoding='utf-8')
for file in list_15:
    file_15.write(file + '\n')

'''
18. 非法拘禁罪裁判书名称提取并保存
'''
list_16 = [file for file in file_list if ('非法拘禁罪' in file)]
file_list = [file for file in file_list if file not in list_16]
print('非法拘禁罪裁判文书个数为：%d' % (len(list_16)))
file_16 = open(filename_path + '/16_非法拘禁罪.txt', 'w+', encoding='utf-8')
for file in list_16:
    file_16.write(file + '\n')

'''
19. 侵犯公民个人信息罪裁判书名称提取并保存
'''
list_17 = [file for file in file_list if ('侵犯公民个人信息罪' in file)]
file_list = [file for file in file_list if file not in list_17]
print('侵犯公民个人信息罪裁判文书个数为：%d' % (len(list_17)))
file_17 = open(filename_path + '/17_侵犯公民个人信息罪.txt', 'w+', encoding='utf-8')
for file in list_17:
    file_17.write(file + '\n')

'''
20. 抢劫罪裁判书名称提取并保存
'''
list_18 = [file for file in file_list if ('抢劫罪' in file)]
file_list = [file for file in file_list if file not in list_18]
print('抢劫罪裁判文书个数为：%d' % (len(list_18)))
file_18 = open(filename_path + '/18_抢劫罪.txt', 'w+', encoding='utf-8')
for file in list_18:
    file_18.write(file + '\n')

'''
21. 盗窃罪裁判书名称提取并保存
'''
list_19 = [file for file in file_list if ('盗窃罪' in file)]
file_list = [file for file in file_list if file not in list_19]
print('盗窃罪裁判文书个数为：%d' % (len(list_19)))
file_19 = open(filename_path + '/19_盗窃罪.txt', 'w+', encoding='utf-8')
for file in list_19:
    file_19.write(file + '\n')

'''
22. 职务侵占罪裁判书名称提取并保存
'''
list_20 = [file for file in file_list if ('职务侵占罪' in file)]
file_list = [file for file in file_list if file not in list_20]
print('职务侵占罪裁判文书个数为：%d' % (len(list_20)))
file_20 = open(filename_path + '/20_职务侵占罪.txt', 'w+', encoding='utf-8')
for file in list_20:
    file_20.write(file + '\n')

'''
23. 挪用资金罪裁判书名称提取并保存
'''
list_21 = [file for file in file_list if ('挪用资金罪' in file)]
file_list = [file for file in file_list if file not in list_21]
print('挪用资金罪裁判文书个数为：%d' % (len(list_21)))
file_21 = open(filename_path + '/21_挪用资金罪.txt', 'w+', encoding='utf-8')
for file in list_21:
    file_21.write(file + '\n')

'''
24. 敲诈勒索罪裁判书名称提取并保存
'''
list_22 = [file for file in file_list if ('敲诈勒索罪' in file)]
file_list = [file for file in file_list if file not in list_22]
print('敲诈勒索罪裁判文书个数为：%d' % (len(list_22)))
file_22 = open(filename_path + '/22_敲诈勒索罪.txt', 'w+', encoding='utf-8')
for file in list_22:
    file_22.write(file + '\n')

'''
25. 故意毁坏财物罪裁判书名称提取并保存
'''
list_23 = [file for file in file_list if ('故意毁坏财物罪' in file)]
file_list = [file for file in file_list if file not in list_23]
print('故意毁坏财物罪裁判文书个数为：%d' % (len(list_23)))
file_23 = open(filename_path + '/23_故意毁坏财物罪.txt', 'w+', encoding='utf-8')
for file in list_23:
    file_23.write(file + '\n')

'''
26. 拒不支付劳动报酬罪裁判书名称提取并保存
'''
list_24 = [file for file in file_list if ('拒不支付劳动报酬罪' in file)]
file_list = [file for file in file_list if file not in list_24]
print('拒不支付劳动报酬罪裁判文书个数为：%d' % (len(list_24)))
file_24 = open(filename_path + '/24_拒不支付劳动报酬罪.txt', 'w+', encoding='utf-8')
for file in list_24:
    file_24.write(file + '\n')

'''
27. 妨害公务罪裁判书名称提取并保存
'''
list_25 = [file for file in file_list if ('妨害公务罪' in file)]
file_list = [file for file in file_list if file not in list_25]
print('妨害公务罪裁判文书个数为：%d' % (len(list_25)))
file_25 = open(filename_path + '/25_妨害公务罪.txt', 'w+', encoding='utf-8')
for file in list_25:
    file_25.write(file + '\n')

'''
28. 伪造变造买卖国家机关公文证件印章罪裁判书名称提取并保存
'''
list_26 = [file for file in file_list if ('伪造变造买卖国家机关公文证件印章罪' in file)]
file_list = [file for file in file_list if file not in list_26]
print('伪造变造买卖国家机关公文证件印章罪裁判文书个数为：%d' % (len(list_26)))
file_26 = open(filename_path + '/26_伪造变造买卖国家机关公文证件印章罪.txt', 'w+', encoding='utf-8')
for file in list_26:
    file_26.write(file + '\n')

'''
29. 聚众斗殴罪裁判书名称提取并保存
'''
list_27 = [file for file in file_list if ('聚众斗殴罪' in file)]
file_list = [file for file in file_list if file not in list_27]
print('聚众斗殴罪裁判文书个数为：%d' % (len(list_27)))
file_27 = open(filename_path + '/27_聚众斗殴罪.txt', 'w+', encoding='utf-8')
for file in list_27:
    file_27.write(file + '\n')

'''
30. 寻衅滋事罪裁判书名称提取并保存
'''
list_28 = [file for file in file_list if ('寻衅滋事罪' in file)]
file_list = [file for file in file_list if file not in list_28]
print('寻衅滋事罪裁判文书个数为：%d' % (len(list_28)))
file_28 = open(filename_path + '/28_寻衅滋事罪.txt', 'w+', encoding='utf-8')
for file in list_28:
    file_28.write(file + '\n')

'''
31. 赌博罪裁判书名称提取并保存
'''
list_29 = [file for file in file_list if ('赌博罪' in file)]
file_list = [file for file in file_list if file not in list_29]
print('赌博罪裁判文书个数为：%d' % (len(list_29)))
file_29 = open(filename_path + '/29_赌博罪.txt', 'w+', encoding='utf-8')
for file in list_29:
    file_29.write(file + '\n')

'''
32. 开设赌场罪裁判书名称提取并保存
'''
list_30 = [file for file in file_list if ('开设赌场罪' in file)]
file_list = [file for file in file_list if file not in list_30]
print('开设赌场罪裁判文书个数为：%d' % (len(list_30)))
file_30 = open(filename_path + '/30_开设赌场罪.txt', 'w+', encoding='utf-8')
for file in list_30:
    file_30.write(file + '\n')

'''
33. 拒不执行判决裁定罪裁判书名称提取并保存
'''
list_31 = [file for file in file_list if ('拒不执行判决裁定罪' in file)]
file_list = [file for file in file_list if file not in list_31]
print('拒不执行判决裁定罪裁判文书个数为：%d' % (len(list_31)))
file_31 = open(filename_path + '/31_拒不执行判决裁定罪.txt', 'w+', encoding='utf-8')
for file in list_31:
    file_31.write(file + '\n')

'''
34. 污染环境罪裁判书名称提取并保存
'''
list_32 = [file for file in file_list if ('污染环境罪' in file)]
file_list = [file for file in file_list if file not in list_32]
print('污染环境罪裁判文书个数为：%d' % (len(list_32)))
file_32 = open(filename_path + '/32_污染环境罪.txt', 'w+', encoding='utf-8')
for file in list_32:
    file_32.write(file + '\n')

'''
35. 非法捕捞水产品罪裁判书名称提取并保存
'''
list_33 = [file for file in file_list if ('非法捕捞水产品罪' in file)]
file_list = [file for file in file_list if file not in list_33]
print('非法捕捞水产品罪裁判文书个数为：%d' % (len(list_33)))
file_33 = open(filename_path + '/33_非法捕捞水产品罪.txt', 'w+', encoding='utf-8')
for file in list_33:
    file_33.write(file + '\n')

'''
36. 非法狩猎罪裁判书名称提取并保存
'''
list_34 = [file for file in file_list if ('非法狩猎罪' in file)]
file_list = [file for file in file_list if file not in list_34]
print('非法狩猎罪裁判文书个数为：%d' % (len(list_34)))
file_34 = open(filename_path + '/34_非法狩猎罪.txt', 'w+', encoding='utf-8')
for file in list_34:
    file_34.write(file + '\n')

'''
37. 非法占用农用地罪裁判书名称提取并保存
'''
list_35 = [file for file in file_list if ('非法占用农用地罪' in file)]
file_list = [file for file in file_list if file not in list_35]
print('非法占用农用地罪裁判文书个数为：%d' % (len(list_35)))
file_35 = open(filename_path + '/35_非法占用农用地罪.txt', 'w+', encoding='utf-8')
for file in list_35:
    file_35.write(file + '\n')

'''
38. 非法采矿罪裁判书名称提取并保存
'''
list_36 = [file for file in file_list if ('非法采矿罪' in file)]
file_list = [file for file in file_list if file not in list_36]
print('非法采矿罪裁判文书个数为：%d' % (len(list_36)))
file_36 = open(filename_path + '/36_非法采矿罪.txt', 'w+', encoding='utf-8')
for file in list_36:
    file_36.write(file + '\n')

'''
39. 滥伐林木罪裁判书名称提取并保存
'''
list_37 = [file for file in file_list if ('滥伐林木罪' in file)]
file_list = [file for file in file_list if file not in list_37]
print('滥伐林木罪裁判文书个数为：%d' % (len(list_37)))
file_37 = open(filename_path + '/37_滥伐林木罪.txt', 'w+', encoding='utf-8')
for file in list_37:
    file_37.write(file + '\n')

'''
40. 非法持有毒品罪裁判书名称提取并保存
'''
list_38 = [file for file in file_list if ('非法持有毒品罪' in file)]
file_list = [file for file in file_list if file not in list_38]
print('非法持有毒品罪裁判文书个数为：%d' % (len(list_38)))
file_38 = open(filename_path + '/38_非法持有毒品罪.txt', 'w+', encoding='utf-8')
for file in list_38:
    file_38.write(file + '\n')

'''
41. 容留他人吸毒罪裁判书名称提取并保存
'''
list_39 = [file for file in file_list if ('容留他人吸毒罪' in file)]
file_list = [file for file in file_list if file not in list_39]
print('容留他人吸毒罪裁判文书个数为：%d' % (len(list_39)))
file_39 = open(filename_path + '/39_容留他人吸毒罪.txt', 'w+', encoding='utf-8')
for file in list_39:
    file_39.write(file + '\n')

'''
42. 引诱容留介绍卖淫罪裁判书名称提取并保存
'''
list_40 = [file for file in file_list if ('引诱容留介绍卖淫罪' in file)]
file_list = [file for file in file_list if file not in list_40]
print('引诱容留介绍卖淫罪裁判文书个数为：%d' % (len(list_40)))
file_40 = open(filename_path + '/40_引诱容留介绍卖淫罪.txt', 'w+', encoding='utf-8')
for file in list_40:
    file_40.write(file + '\n')

'''
43. 贪污罪裁判书名称提取并保存
'''
list_41 = [file for file in file_list if ('贪污罪' in file)]
file_list = [file for file in file_list if file not in list_41]
print('贪污罪裁判文书个数为：%d' % (len(list_41)))
file_41 = open(filename_path + '/41_贪污罪.txt', 'w+', encoding='utf-8')
for file in list_41:
    file_41.write(file + '\n')

'''
44. 受贿罪裁判书名称提取并保存
'''
list_42 = [file for file in file_list if ('受贿罪' in file and "单位" not in file and "利用影响力" not in file)]
file_list = [file for file in file_list if file not in list_42]
print('受贿罪裁判文书个数为：%d' % (len(list_42)))
file_42 = open(filename_path + '/42_受贿罪.txt', 'w+', encoding='utf-8')
for file in list_42:
    file_42.write(file + '\n')

