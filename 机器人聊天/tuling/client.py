#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""client.py"""

import tuling_robot as robot
import logging

# 第01步：请在下方 '' 中填写 robot.key，不填写使用默认 APIKEY（有可能失效）
robot.key = '3c7f2d9802ce42dca15c7dfa26a7fc96' or robot.key
logging.basicConfig(
    filename="../tulingrobot/chat.log",
    filemode='a',
    #输出日志
    format="%(asctime)s %(name)s:%(levelname)s %(message)s",
    #输出时间
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)
def hh(username):
    robot.input_text = input(f"{username}:")
    logging.debug(f"{username}:{robot.input_text}")
def xx(robot_name):
    result = robot.get_values()
    logging.debug(f"{robot_name}:{result}")
    print(f"{robot_name}：{result}")

def aa(username,robot_name):
    while True:
        # 第02步：通过 input() 函数获取输入的内容，并赋值给机器人变量 robot.input_text
        hh(username)
        exit_word = ['88','886','白白','再见','拜拜','exit']
        if robot.input_text in exit_word:
            logging.debug(f"{robot_name}：see you next time")
            print(f"{robot_name}：see you next time")
            break
        elif not robot.input_text:
            pass
        else:

            # 第03步：通过 robot.get_values() 函数获取机器人返回的结果，使用 print() 函数打印结果
            xx(f"{robot_name}")
if __name__ == '__main__':

        aa("wao","hh")
