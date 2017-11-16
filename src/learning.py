# -*- coding:utf-8 -*-
'''
  作    者   : 张茗 
'''
import os
import numpy as np
from conf.settings import LEARNING_DATA_DIR
from collections import defaultdict

item = ['面包', '牛奶', '奶酪', '苹果', '香蕉']


def get_data():
    data_filename = os.path.join(LEARNING_DATA_DIR, 'Chapter1', 'affinity_dataset.txt')

    X = np.loadtxt(data_filename)
    valid_rules = defaultdict(int)
    invalid_rules = defaultdict(int)
    num_occurances = defaultdict(int)

    for row in X:
        for premise in range(len(item)):
            if row[premise] == 1:
                num_occurances[premise] += 1
                for conclusion in range(len(item)):
                    if premise == conclusion:
                        continue
                    if row[conclusion] == 1:
                        valid_rules[(premise, conclusion)] += 1
                    elif row[conclusion] != 1:
                        invalid_rules[(premise, conclusion)] += 1

    confidence = defaultdict(float)
    for premise, conclusion in valid_rules.keys():
        rule = (premise, conclusion)
        confidence[rule] = valid_rules[rule] / num_occurances[premise]
    # print(valid_rules, invalid_rules)
    return valid_rules, invalid_rules, num_occurances, confidence


def print_rule(premise, conclusion, support, confidence, features):
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print("Rule: If a person buys {0} they will also buy {1}".format(premise_name, conclusion_name))
    print(" - Support: {0}".format(support[(premise, conclusion)]))
    print(" - Confidence: {0:.3f}".format(confidence[(premise, conclusion)]))


if __name__ == '__main__':
    valid_rules, invalid_rules, num_occurances, confidence = get_data()
    premise = 0
    conclusion = 1
    print_rule(premise, conclusion, valid_rules, confidence, item)
