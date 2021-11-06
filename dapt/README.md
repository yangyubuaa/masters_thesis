# dapt训练文件
---
1. dapt_data存放dapt_data_generation生成的pta数据
2. dapt_data_generation为一系列根据不同原则写的pta数据生成脚本
3. dapt_model为预训练的目标模型文件
4. dapt_train为训练所需要的脚本以及配置文件
5. log存放训练过程的log日志
---
其中dapt_data以及dapt_model由于文件过大，不存放在github中，整理完毕后会存放在网盘中，使用时单独下载放入即可,dapt_data以及dapt_model链接:https://bhpan.buaa.edu.cn:443/link/3AD744EBD635FF154C72C5E56A5AAF3F
有效期限：2022-06-30 23:59
---
dapt试验步骤
1. 使用全样本构建样本对，也就是训练一个自编码器（再最开始尝试，看对模型有没有提升）

此方法将t5模型看做自编码器

2. 使用TOP K的方式生成一个样本对（论文原始方法）

此方法进行数据的生成，对每个样本数据中的每个句子进行rank，选取GSR比率的top样本进行mask，mask使用mask1

3. 使用TOP K的方式将样本对的target全排列（我们的方法）

此方法对每个样本中的每个句子进行rank，选取GSR比率的top样本进行mask，使用mask1 mask2 。。。mask n，然后进行全排列，并将target进行全排列，进行训练，此方法能学会句子间的先后顺序

4. 尝试不同的GSR比率

5. 尝试掩盖45%的比率，然后将20%的mask还原

6. 分句策略采用两种,一个是句子粒度,一个是按照所有特殊符号分句,第二种策略可以降低模型预测难度
