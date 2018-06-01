#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 4/11/2018 5:22 PM 
# @Author : sunyonghai 
# @File : append_all_data.py 
# @Software: ZJ_AI
# =========================================================
from create_all_data import append_all_data

if __name__ == '__main__':
    dirs = ['data/train_data-2018-04-11']
    append_all_data(dirs)

"""
run this script,then run the create_all_Main.py to create the .txt file
"""