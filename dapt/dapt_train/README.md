# dapt训练脚本
---
1. train_one_stage.py 为不含autoencoder的训练过程
2. train_two_stage.py 为含autoencoder的训练过程
3. train_one_stage.yaml 为训练过程超参数配置文件
4. train_two_stage.yaml 为训练过程超参数配置文件
5. run_train_one_stage.sh & run_train_two_stage.sh 为启动脚本
---
model_principal.py & model_principal.yaml 为模型代码以及配置文件
---
getdata.py 从score_corpus.json中根据不同试验策略构建训练样本
getdata.yaml 为策略配置文件
---
evaluator.py为训练过程评估器
