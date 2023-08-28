#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/8/28 22:10
# @Author  : wen
# @File    : pseudonyms.py
# @Software: PyCharm

"""
从两个独立的名字元组中速记选择玄素来生成有趣的假名
"""

import sys
import random


def gen_names():
    print("欢迎来到虚假名字生成器.")
    print("我们会为你生成类似 '张三' 这样的虚假名字.")
    first_name = ("张", "赵", "钱", "孙", "李", "周", "吴")
    last_name = ("淮西", "燕京", "西楼", "持盈", "问舟", "雪青", "临渊")
    while True:
        gen_first_name = random.choice(first_name)
        gen_last_name = random.choice(last_name)
        print("============")
        print("{}{}".format(gen_first_name, gen_last_name), file=sys.stderr)
        try_again = input("\n 是否再试一次? (按 enter 键) 输入 n 则结束\n")
        if try_again.lower() == "n":
            break
    input("\n 请按 enter 退出.")


if __name__ == '__main__':
    gen_names()
