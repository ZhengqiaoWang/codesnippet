'''
Author: 王政乔 me@zhengqiao.wang
Date: 2022-09-19 18:42:28
LastEditors: 王政乔 me@zhengqiao.wang
LastEditTime: 2022-09-20 08:29:09
FilePath: /codesnippet/python/test_sort.py
Description: 对比ut
Website: https://www.zhengqiao.wang
'''
import pytest
import shuffle


@pytest.fixture
def getNormalList():
    return [x for x in range(100)]


def getScore(value):
    return max(0, 100-value)


def test_random_shuffle(getNormalList):
    x = getNormalList
    y_s = [0] * len(x)
    for i in range(50):
        tmp_y = shuffle.randomShuffleWithScore(x,getScore)
        assert(len(tmp_y) == 100)
    for idx in range(len(x)):
        y_s[idx] += tmp_y[idx]
    y = [y / 50 for y in y_s]
    assert(y[0]<y[-1])