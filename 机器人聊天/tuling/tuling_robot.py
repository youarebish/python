#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""tuling_robot.py
图灵机器人工具类"""

from urllib import request
import json

# region 基本参数设置

# 私有变量，不建议修改
__api_url = "http://openapi.tuling123.com/openapi/api/v2"  # 接口地址
__user_id = 'xiaoming'  # 用户编号：任意

# 重要的变量，用户需要通过创建应用后获取
key = '3c7f2d9802ce42dca15c7dfa26a7fc96'  # 网站 APIKEY

# 请求类型，受保护，默认是文本类型，一般不需要修改
_req_type = 0  # 输入类型：0-文本(默认)、1-图片、2-音频

# 请求的内容，一般配置文本即可
input_text = ''  # 输入的文本内容
input_image = ''  # 输入的图片地址
input_media = ''  # 输入的音频地址

# 用户所在地址，配置城市即可
city = '北京'  # 城市（必选）
province = '北京'  # 省份（可选）
street = '北三环西路甲18号'  # 街道（可选）


# endregion

def _generate_req():
    """
    生成请求对象
    :return: 请求对象的字节流
    """
    # 将请求的参数拼装成字典格式
    __req = {
        "reqType": _req_type,
        "perception": {
            "inputText": {
                "text": input_text
            },
            "inputImage": {
                "url": input_image
            },
            "selfInfo": {
                "location": {
                    "city": city,
                    "province": province,
                    "street": street
                }
            }
        },
        "userInfo": {
            "apiKey": key,
            "userId": __user_id
        }
    }

    __req = json.dumps(__req).encode()  # 将字典格式的 __req 编码为 utf8 的字节流
    return __req


def _generate_resp():
    """
    获取相应对象
    :return: 获取服务器端返回的响应（字节流）
    """
    req = _generate_req()  # 获取请求对象字节流，调用 _generate_req() 函数

    # 设置请求对象
    http_req = request.Request(
        __api_url,  # 请求地址
        data=req,  # 请求的内容（字节流）
        headers={'content-type': 'application/json'})  # 指定头（请求类型是JSON格式）

    response = request.urlopen(http_req)  # 发送请求并接收响应
    return response


def _generate_results():
    """
    解析响应对象的字节流，获取响应的内容（受保护类型函数）
    :return: 元组：(意图, 结果的列表）
    """
    resp = _generate_resp()  # 调用函数获取响应结果的字节流

    response_str = resp.read().decode('utf8')  # 将响应流解码为字符串

    response_dic = json.loads(response_str)  # 将字符串转换成字典

    intent_code = response_dic['intent']['code']  # 获取意图编码

    results = response_dic['results']  # 获取响应结果的列表
    return intent_code, results


def get_values():
    """
    解析响应结果
    :return:
    """
    intent_code, results = _generate_results()  # 通过调用函数获取意图编码和结果列表
    values = []
    for result in results:  # 遍历结果列表（列表中可能有多个字典类型的元素）
        values.append(result['values'][result['resultType']])  # 获取内容
    return  values[0]  # 获取意图名称和内容列表


# 定义字典，映射常见的意图编号和意图名称
code = {
    10004: '聊天',
    10008: '天气',
    10013: '科普',
    10015: '菜单',
    10019: '日期',
    10020: '翻译',
    10023: '网址',
    10034: '语义库',
}
