'''
Author: 王政乔 me@zhengqiao.wang
Date: 2022-09-19 18:42:28
LastEditors: 王政乔 me@zhengqiao.wang
LastEditTime: 2022-09-19 19:08:20
FilePath: /codesnippet/python/test_compare.py
Description: 对比ut
Website: https://www.zhengqiao.wang
'''
import pytest
import compare


@pytest.fixture
def getNormalDict1():
    return {
        1: "abc",
        2: "cde",
        3: "efg"
    }


@pytest.fixture
def getNormalDict2():
    return {
        1: "cde",
        4: "abc",
        3: "efg"
    }


@pytest.fixture
def getMixDict1():
    return {
        1: "abc",
        "2": None,
        int: 3.1415926
    }


def test_compare_normal(getNormalDict1, getNormalDict2):
    ret1, ret2, ret3 = compare.compareDict(getNormalDict1, getNormalDict2)
    assert(len(ret1) == 1)
    assert(len(ret2) == 1)
    assert(len(ret3) == 1)

    assert(ret1[0] == 2)
    assert(ret2[0] == 4)
    assert(len(ret3[0]) == 3)

    ret31, ret32, ret33 = ret3[0]
    assert(ret31 == 1)
    assert(ret32 == 'abc')
    assert(ret33 == 'cde')


def test_compare_mix(getNormalDict1, getMixDict1):
    ret1, ret2, ret3 = compare.compareDict(getNormalDict1, getMixDict1)
    assert(len(ret1) == 2)
    assert(len(ret2) == 2)
    assert(len(ret3) == 0)

    assert(ret1[0] == 2)
    assert(ret1[1] == 3)

    assert(ret2[0] == '2')
    assert(ret2[1] == int)
