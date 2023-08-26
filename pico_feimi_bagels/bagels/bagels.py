#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 00:52
# @Author  : wen
# @File    : bagels.py
# @Software: PyCharm

"""
猜数字游戏
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def get_secret_num():
    """返回随机的猜测数字的字符串"""
    numbers = list("0123456789")
    random.shuffle(numbers)

    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """返回提示字符串"""
    if guess == secret_num:
        return "你猜对了!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("FERMI")
        elif guess[i] in secret_num:
            clues.append("PICO")

    if len(clues) == 0:
        return "BAGELS"
    else:
        clues.sort()
        return " ".join(clues)


def bagels():
    print("""
    ===猜数字游戏===
    -> 随机指定一个 {} 位的数字
    -> 尝试去猜测这个数字
    -> 下面是游戏规则:
        1. PICO: 数字正确但位置错误
        2. FERMI: 数字和位置都正确
        3. BAGELS: 全部错误
    -> 示例: 给出 248, 如果你猜测 843, 则结果为 PICO
    """.format(NUM_DIGITS))

    while True:
        secret_num = get_secret_num()
        print("已经设置好猜测的数字")
        print("你有 {} 次机会来猜测这个数字".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = " "
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("尝试猜测 #{}: ".format(num_guesses))
                guess = input(">>> ")
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # 玩家猜对了数字
            if num_guesses > MAX_GUESSES:
                print("你已经使用完了猜测次数")
                print("你的最终结果是: {}".format(secret_num))

        # 询问玩家是否再玩一次
        print("你还想再玩一次吗? (y/n)")
        if not input(">>> ").lower().startswith('y'):
            break
    print("下次再见!")


if __name__ == '__main__':
    bagels()