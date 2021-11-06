# dapt训练脚本(未更新)
---
1. train_autoencoder是根据自编码器数据集来进行dapt
2. train_permutation是打乱数据顺序来进行dapt
3. train_principal是根据pegasus论文的ind/origin方式进行dapt

三个训练文件分别有对应的yaml配置文件
---
1. model_principal、model_permutation、model_autoencoder三种训练方法对应的模型文件
---
getdata.py里面包含了数据获取类，根据数据路径构建数据集类
---
evaluator.py里面包含了训练过程评估器,传入参数进行评估以及log打印
---
1. run_principal.sh
2. run_permutation.sh
3. run_autoencoder.sh
以上三个为运行脚本，会进行训练，并将训练日志输出到对应名称的log文件中
