#! -*- coding: utf-8 -*-

from __future__ import print_function
import json
import numpy as np
from tqdm import tqdm
from bert4keras.backend import keras, K
from bert4keras.layers import Loss
from bert4keras.models import build_transformer_model
from bert4keras.tokenizers import SpTokenizer
from bert4keras.optimizers import Adam
from bert4keras.snippets import sequence_padding, open
from bert4keras.snippets import DataGenerator, AutoRegressiveDecoder
from keras.models import Model
from rouge import Rouge  # pip install rouge
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import os
from util.logging import init_logger, logger

# 基本参数
max_c_len = 512
max_t_len = 256
batch_size = 8
epochs = 100000

# 模型路径
config_path = '../mt5/mt5_small/mt5_small_config.json'
# config_path = './chinese_t5_pegasus_small/config.json'
checkpoint_path = '../mt5/mt5_small/model.ckpt-1000000'
# checkpoint_path = './chinese_t5_pegasus_small/model.ckpt'
spm_path = '../mt5/sentencepiece_cn.model'
keep_tokens_path = '../mt5/sentencepiece_cn_keep_tokens.json'
summ_result = './result'


def make_log_file_name():
    log_file_name = './log/train.log'
    return log_file_name


def load_data(filename):
    D = []
    with open(filename, encoding='utf-8')as f:
        for l in f:
            list = json.loads(l)
            source = list[0]
            target = list[1]
            D.append((target, source))
    return D


# 加载数据集
logger.info('starting to read data')
train_data = load_data("abstract.json")
# valid_data = load_data("dataset/valid_extract.json")
# test_data = load_data("dataset/test_extract.json")
# valid_data = [valid_data[i] for i in range(3500)]

# 加载分词器
tokenizer = SpTokenizer(spm_path, token_start=None, token_end='</s>')
keep_tokens = json.load(open(keep_tokens_path))


class data_generator(DataGenerator):
    """数据生成器
    """
    def __iter__(self, random=False):
        batch_c_token_ids, batch_t_token_ids = [], []
        for is_end, (title, content) in self.sample(random):
            c_token_ids, _ = tokenizer.encode(content, maxlen=max_c_len)
            t_token_ids, _ = tokenizer.encode(title, maxlen=max_t_len)
            batch_c_token_ids.append(c_token_ids)
            batch_t_token_ids.append([0] + t_token_ids)
            if len(batch_c_token_ids) == self.batch_size or is_end:
                batch_c_token_ids = sequence_padding(batch_c_token_ids)
                batch_t_token_ids = sequence_padding(batch_t_token_ids)
                yield [batch_c_token_ids, batch_t_token_ids], None
                batch_c_token_ids, batch_t_token_ids = [], []


class CrossEntropy(Loss):
    """交叉熵作为loss，并mask掉输入部分
    """
    def compute_loss(self, inputs, mask=None):
        y_true, y_pred = inputs
        y_true = y_true[:, 1:]  # 目标token_ids
        y_mask = K.cast(mask[1], K.floatx())[:, :-1]  # 解码器自带mask
        y_pred = y_pred[:, :-1]  # 预测序列，错开一位
        loss = K.sparse_categorical_crossentropy(y_true, y_pred)
        loss = K.sum(loss * y_mask) / K.sum(y_mask)
        return loss


logger.info('start building model')
t5 = build_transformer_model(
    config_path=config_path,
    checkpoint_path=checkpoint_path,
    keep_tokens=keep_tokens,
    model='t5.1.1',
    return_keras_model=False,
    name='T5',
)
encoder = t5.encoder
decoder = t5.decoder
model = t5.model
model.summary()

output = CrossEntropy(1)([model.inputs[1], model.outputs[0]])

model = Model(model.inputs, output)
model.compile(optimizer=Adam(2e-4))


class Evaluator(keras.callbacks.Callback):
    """保存
    """
    def on_epoch_end(self, epoch, logs=None):
        model.save_weights('./save/best_model.weights')  # 保存模型


if __name__ == '__main__':
    init_logger(make_log_file_name())
    evaluator = Evaluator()
    train_generator = data_generator(train_data, batch_size)

    model.fit(
        train_generator.forfit(),
        steps_per_epoch=len(train_generator),
        epochs=epochs,
        callbacks=[evaluator]
    )

else:

    model.load_weights('./best_model.weights')
