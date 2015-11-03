#!/usr/bin/env python
########################################################################
# 
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
'''
File: run.py
Author: xuzhouchuan(xuzhouchuan@gmail.com)
Date: 2015/11/03 06:28:08
'''
from app import app

app.run(debug=True, host="0.0.0.0")
