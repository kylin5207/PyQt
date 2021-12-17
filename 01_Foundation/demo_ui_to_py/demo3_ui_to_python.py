# -*- coding:utf-8 -*-
"""
demo3_ui_to_python
使用UIDesigner设计好窗体并保存为文件formHello.ui后，要在Python里使用这个窗体，
需要使用 PyQt5 的工具软件 pyuic5.exe 将这个ui文件编译转换为对应的Python语言程序文件。
附录：pyuic.exe是将Qt Designer(或 Qt Creator 内置的 UI Designer)可视化设计的界面文件(.ui 文件)
编译转换为Python程序文件的工具软件，是使用PyQt5设计GUI程序最常用到的工具软件。
:Author: kylin.smq@qq.com
:Last Modified by: kylin.smq@qq.com
"""
# 方法一：直接通过命令行
# python3 -m PyQt5.uic.pyuic formHello.ui(ui文件名) -o formHello.py(目标文件名)

# 方法二：直接调用pyuic
# 找到pyuic命令所在的位置，然后调用pyuic5命令，进行代码编译
# 建议，将pyuic5命令加入到外部工具中，便于使用
# /Library/Frameworks/Python.framework/Versions/3.6/bin/pyuic5 formHello.ui -o formHello2.py

