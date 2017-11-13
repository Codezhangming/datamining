# -*- coding:utf-8 -*-
'''
  作    者   : 张茗
'''
from config.constant_conf import users

# 曼哈顿距离
def manhattan(rating1, rating2):
    result = 0
    for i in rating1:
        result += abs(rating1[i] - rating2[i])
    return result

# 闵科夫斯基距离
def minkowski(rating1, rating2, r):
    result = 0
    for i in rating1:
        result += abs(rating1[i] - rating2[i]) ** r if i in rating2 else 0
    return pow(result, 1 / r)

if __name__ == '__main__':
    print manhattan(users['Angelica'],users['Bill'])






