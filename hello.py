#!/usr/bin/env python
########################################################################
# 
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
'''
File: hello.py
Author: baidu(baidu@baidu.com)
Date: 2015/11/03 10:54:07
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
