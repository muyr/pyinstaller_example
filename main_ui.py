#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2020.1
# Email : muyanru345@163.com
###################################################################
from PySide.QtCore import *
from PySide.QtGui import *
import os
import test_data

class MWidget(QDialog):
    def __init__(self, parent=None):
        super(MWidget, self).__init__(parent)
        line_edit = QTextEdit()
        frozen = 'not'
        if getattr(sys, 'frozen', False):
            # we are running in a bundle
            frozen = 'ever so'
            bundle_dir = os.path.abspath(sys._MEIPASS)
        else:
            # we are running in a normal Python environment
            bundle_dir = os.path.dirname(os.path.abspath(__file__))

        line_edit.append(u'we are\n'+ frozen + 'frozen')
        line_edit.append(u'bundle dir is\n'+ bundle_dir)
        line_edit.append(u'sys.argv[0] is\n'+ sys.argv[0])
        line_edit.append(u'sys.executable is\n'+ sys.executable)
        line_edit.append(u'os.getcwd is\n'+ os.getcwd())
        line_edit.append('\n')
        a = test_data.get_data_by___file__()
        b = test_data.get_data_by_executable()
        c = test_data.get_data_by_argv()
        line_edit.append(u'use __file__, \n{}, {}'.format(a,os.path.isfile(a)))
        line_edit.append(u'use executable, \n{}, {}'.format(b,os.path.isfile(b)))
        line_edit.append(u'use argv, \n{}, {}'.format( c,os.path.isfile(c)))

        main_lay = QVBoxLayout()
        main_lay.addWidget(line_edit)
        self.setLayout(main_lay)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    test = MWidget()
    test.show()
    sys.exit(app.exec_())

