'''
Author: 王政乔 me@zhengqiao.wang
Date: 2022-09-20 08:06:36
LastEditors: 王政乔 me@zhengqiao.wang
LastEditTime: 2022-09-20 08:30:59
FilePath: /codesnippet/python/shuffle.py
Description: 排序
Website: https://www.zhengqiao.wang
'''

import random


def randomShuffleWithScore(in_list: list, score_func):
    """Random shuffle list with scores. Higher scores value will have more opportunity to be the front.
    This function will copy multi-times.
    Introduction: https://www.zhengqiao.wang/algorithm/python/权重洗牌算法.html

    Args:
        in_list (list): value lists which will be random shuffled
        score_func (function): function to get value's score. must return an integer.

    Returns:
        list: random shuffled list
    """
    out_list = []
    tmp_list = in_list.copy()

    item_idx_list = []
    for idx, value in enumerate(tmp_list):
        item_idx_list += [idx] * score_func(value)

    random.shuffle(item_idx_list)

    for item_idx in item_idx_list:
        if tmp_list[item_idx] == None:
            continue
        out_list.append(tmp_list[item_idx])
        tmp_list[item_idx] = None
    return out_list
