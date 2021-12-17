# -*- coding:utf-8 -*-
"""
ui_logic_split2 用户界面与业务逻辑
方式二：单继承与界面独立封装方法，更有利于实现界面与逻辑分离
实际上， 在 Qt C++应用程序中默认就是采用的单继承方法

由于 self.__ui 是 QmyWidget 类的私有属性，
因此在应用程序中创建的 QmyWidget对象myWidget不能直接访问 myWidget.__ui，
也就无法直接访问窗体上的界面组件。

特点：
(1)可视化设计的窗体对象被定义为 QmyWidget 类的一个私有属性 self.__ui，
在 QmyWidget类的内部对窗体上的组件的访问都通过这个属性实现，
而外部无法直接访问窗体上的对象，
这更符合面向对象封装隔离的设计思想。
(2)窗体上的组件不会与QmyWidget里定义的属性混淆

:Author: kylin.smq@qq.com
:Last Modified by: kylin.smq@qq.com
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from formHello import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        # 调用父类构造函数，创建 QWidget 窗体
        super().__init__(parent)

        # 创建ui对象
        # 私有属性 self.__ui 包含了可视化设计的 UI 窗体上的所有组件
        self.__ui = Ui_Form()

        # 构造UI
        self.__ui.setupUi(self)

        self.Lab = "单继承的 QmyWidget"
        #
        self.__ui.labeHello.setText(self.Lab)

    def setBtnText(self, aText):
        # 为了访问窗体上的组件，可以在 QmyWidget 类里定义接口函数
        self.__ui.pushButton.setText(aText)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = QmyWidget()
    myWidget.show()
    myWidget.setBtnText("间接设置")
    sys.exit(app.exec_())
#创建app，用QApplication类

