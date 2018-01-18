# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:16:47 2018

@author: chenzhiwei
"""
"""
#apriori算法学习
属于经典的亲和性算法，较apriori算法性能要好或者较之改进很多的算法有：Eclat and FP-growth(频繁项集挖掘算法)等
亲和性算法应用场景：欺诈检测|顾客区分|软件优化|推荐等。

"""

import os
import pandas as pd
data_folder = os.path.join(u'E:\【01】学习文档\Python数据挖掘入门与实践源码及数据\source_data\chapter4\ml-100k')
ratings_filename = os.path.join(data_folder,'u.data')

all_ratings = pd.read_csv(ratings_filename, sep = '\t', header=None, names= ['userid','movieid','rating','datetime'])
#解析时间戳数据
all_ratings['datetime'] = pd.to_datetime(all_ratings['datetime'],unit = 's')
#创建特征值
all_ratings['favorable'] = all_ratings['rating']>3
#创建训练集
rating = all_ratings[all_ratings['userid'].isin(range(200))]
favorable_rating = rating[rating['favorable']]
