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

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

