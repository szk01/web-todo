from jinja2 import Environment, FileSystemLoader
import os.path
import time
import json


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('log.gua.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)

        
# 两个模块（class）分别负责不同的功能，需要交流信息（传递变量时），写在同一个主函数，逻辑处理流程中。
