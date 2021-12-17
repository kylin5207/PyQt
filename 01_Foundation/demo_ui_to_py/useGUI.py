# -*- coding:utf-8 -*-
"""
useGUI演示了使用 Ui_Form类创建GUI应用程序的基本框架

:Author: kylin.smq@qq.com
:Last Modified by: kylin.smq@qq.com
"""
import sys
from PyQt5 import QtWidgets
import formHello

app = QtWidgets.QApplication(sys.argv)
baseWidget = QtWidgets.QWidget()  # 创建窗体的基类 QWidget 的实例

ui = formHello.Ui_Form()

ui.setupUi(baseWidget)  # 以 baseWidget 作为传递参数，创建完整窗体
# 注意，这里不能使用ui.show()，因为ui是Ui_Form类的对象，
# 而Ui_FormHello的父类是object，根本就不是Qt的窗体界面类
baseWidget.show()

ui.labeHello.setText("Hello,被程序修改")  # 可以修改窗体上标签的文字
sys.exit(app.exec_())

