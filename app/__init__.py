#!/usr/bin/env python
########################################################################
# 
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
'''
File: __init__.py
Author: root(root@baidu.com)
Date: 2015/11/03 06:21:26
'''
from flask import Flask

app = Flask(__name__)
from app import views

