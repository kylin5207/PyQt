# -*- coding:utf-8 -*-
"""
appMain 程序 myDialog.py 可以当作主程序直接运行，但是建议单独编写一个主程序文件 appMain.py

appMain.py 的功能是创建应用程序和主窗体，然后显示主窗体，并开始运行应用程序。
它将 myDialog.py 文件的测试运行部分单独拿出来作为一个文件。
当一个应用程序有多个窗体，并且窗体之间有数据传递时，appMain.py 负责创建应用程序的主窗体并运行起来，这样使整个应用程序的结构更清晰。

:Author: Kylin
:Last Modified by: kylin.smq@qq.com
"""
import sys
from PyQt5.QtWidgets import QApplication
from myDialog import QmyDialog

# 创建GUI应用程序
app = QApplication(sys.argv)
# 创建主窗体
mainform = QmyDialog()
# 显示主窗体
mainform.show()
sys.exit(app.exec())


