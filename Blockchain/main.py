# -*- coding: utf-8 -*-
from scrapy.cmdline import execute

import sys
import os

# 将项目根目录加入系统环境变量中。
# os.path.abspath(__file__)为当前文件所在绝对路径
# os.path.dirname() 获取文件的父目录。

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))


# 调用execute函数执行scrapy命令，相当于在控制台cmd输入该命令
# 可以传递一个数组参数进来:
# execute(["scrapy", "crawl" , "jinse"])

execute(["scrapy", "crawl" , "eightbtc"])

# execute(["scrapy", "crawl" , "btc798"])

# execute(["scrapy", "crawl" , "bitkan"])

