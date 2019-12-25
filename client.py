#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""client.py"""

import tuling_robot as robot

# 第01步：请在下方 '' 中填写 robot.key，不填写使用默认 APIKEY（有可能失效）
robot.key = '3c7f2d9802ce42dca15c7dfa26a7fc96' or robot.key
def hh():
    robot.input_text = input("我:")
def xx():
    result = robot.get_values()
    print(f"傻子：{result}")

def aa():
    while True:
        # 第02步：通过 input() 函数获取输入的内容，并赋值给机器人变量 robot.input_text
        hh()
        exit_word = ['88','886','白白','再见','拜拜','exit']
        if robot.input_text in exit_word:
            print(f"傻子：see you next time")
            break
        elif not robot.input_text:
            pass
        else:

            # 第03步：通过 robot.get_values() 函数获取机器人返回的结果，使用 print() 函数打印结果
            xx()
if __name__ == '__main__':

        aa()
