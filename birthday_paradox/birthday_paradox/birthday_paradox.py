#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 10:38
# @Author  : wen
# @File    : birthday_paradox.py
# @Software: PyCharm

"""
探索生日悖论的概率
"""
import datetime
import random


def get_birthdays(number_of_birthdays):
    """返回一个随机的生日日期对象数字列表"""
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2023, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def get_math(birthdays):
    """返回生日列表中出现多次的日期"""
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a+1 : ]):
            if birthday_a == birthday_b:
                return birthday_a

if __name__ == '__main__':
    print("""
    ===生日悖论模拟实验===
    """)

    # 创建一个按照月份排序的元组
    MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    while True:
        print("请输入生日悖论问题实验次数: ")
        response = input(">>> ")
        if response.isdecimal() and (0 < int(response) <= 100):
            num_b_days = int(response)
            break
    print("""
    ===实验者已输入实验次数===
    """)

    print("-> 生成的生日", num_b_days, ": ")
    birthdays = get_birthdays(num_b_days)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(", ", end="")
        month_name = MONTHS[birthday.month - 1]
        date_text = "{} {}".format(month_name, birthday.day)
        print(date_text, end="")

    print()

    # 确定是否存在两个相同的生日
    match = get_math(birthdays)

    # 显示实验结果
    print("在这次实验中, ", end="")
    if match != None:
        month_name = MONTHS[match.month - 1]
        date_text = "{} {}".format(month_name, match.day)
        print("部分人拥有相同的生日是", date_text)
    else:
        print("没有匹配的生日")
    print()

    print("开始实验", num_b_days, "运行开始...")
    input("按下回车键开始...")
