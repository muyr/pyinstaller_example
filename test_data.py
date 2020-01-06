#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2020.1
# Email : muyanru345@163.com
###################################################################
import sys
import os


def get_data_by___file__():
    bundle_dir = os.path.abspath(os.path.dirname(__file__)) if getattr(sys, 'frozen', False) else os.path.abspath(os.path.dirname(__file__))
    path_to_dat = os.path.join(bundle_dir, 'data', 'data.txt')
    return path_to_dat


def get_data_by_executable():
    bundle_dir = os.path.abspath(os.path.dirname(sys.executable)) if getattr(sys, 'frozen', False) else os.path.abspath(os.path.dirname(__file__))
    path_to_dat = os.path.join(bundle_dir, 'data', 'data.txt')
    return path_to_dat


def get_data_by_argv():
    bundle_dir = os.path.abspath(os.path.dirname(sys.argv[0])) if getattr(sys, 'frozen', False) else os.path.abspath(os.path.dirname(__file__))
    path_to_dat = os.path.join(bundle_dir, 'data', 'data.txt')
    return path_to_dat
