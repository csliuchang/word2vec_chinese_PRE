"""
created on 2019.7.15
author：chang liu
"""

import jieba
import numpy as np
import csv

filePath = 'results.txt'
fileSegWordDonePath = 'sa_results.txt'

# 打印中文列表
def PrintListChinese(list):
    for i in range(len(list)):
        print(list[i])

    # 读取文件内容到列表


fileTrainRead = []
with open(filePath, 'r',encoding='utf-8') as fileTrainRaw:
    for line in fileTrainRaw:  # 按行读取文件
        fileTrainRead.append(line)

# jieba分词后保存在列表中
fileTrainSeg = []
for i in range(len(fileTrainRead)):
    fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i][9:-11], cut_all=False)))])
    if i % 100 == 0:
        print(i)

# 保存分词结果到文件中
with open(fileSegWordDonePath, 'w', encoding='utf-8') as fW:
    for i in range(len(fileTrainSeg)):
        fW.write(fileTrainSeg[i][0])
        fW.write('\n')


