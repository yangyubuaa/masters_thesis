# dapt领域适应预训练的数据生成
---
根据预处理的数据集(按句号分句,按标点符号分句两种策略),按照pegasus论文中的分数计算方式进行score计算,得到["segment1_segment2_segment3_..._segmentn", "rougescore1_rougescore2_rougescore3_..._rougescoren","order1_order2_order3_..._ordern"]样本构成的数据集
