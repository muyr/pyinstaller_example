#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2020.1
# Email : muyanru345@163.com
###################################################################

import sys, os
import test_data

def main():
    frozen = 'not'
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = os.path.abspath(sys._MEIPASS)
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    print('we are', frozen, 'frozen')
    print('bundle dir is', bundle_dir)
    print('sys.argv[0] is', sys.argv[0])
    print('sys.executable is', sys.executable)
    print('os.getcwd is', os.getcwd())
    print ()
    a = test_data.get_data_by___file__()
    b = test_data.get_data_by_executable()
    c = test_data.get_data_by_argv()
    print ('use __file__, ', a, os.path.isfile(a))
    print ('use executable, ', b, os.path.isfile(b))
    print ('use argv, ', c, os.path.isfile(c))


main()
