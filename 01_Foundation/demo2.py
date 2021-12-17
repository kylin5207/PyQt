# -*- coding:utf-8 -*-
"""
demo1 Hello world

:Author: kylin.smq@qq.com
:Last Modified by: kylin.smq@qq.com
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui, QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建app，用QApplication类
    widgetHello = QtWidgets.QWidget()  # 创建窗体，用QWidget类
    widgetHello.resize(280, 150)   # 设置窗体的宽度和高度
    widgetHello.setWindowTitle("Demo2_1")  # 设置窗体的标题文字

    # 创建标签，父容器为widgetHello，这样标签LabHello 才会显示在窗体 widgetHello 上。
    LabHello = QtWidgets.QLabel(widgetHello)
    # 设置标签文字
    LabHello.setText("Hello World,PyQt5")
    # 创建字体对象
    font = QtGui.QFont()
    # 设置字体大小
    font.setPointSize(12)
    # 设置粗体
    font.setBold(True)
    # 设置字体
    LabHello.setFont(font)
    # 获取LabHello的合适大小，返回值是QSize对象
    size = LabHello.sizeHint()

    LabHello.setGeometry(70, 60, size.width(), size.height())
    widgetHello.show()  # 显示对话框 

    sys.exit(app.exec_())