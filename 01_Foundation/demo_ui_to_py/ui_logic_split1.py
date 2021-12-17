# -*- coding:utf-8 -*-
"""
ui_logic_split1 用户界面与业务逻辑
方式一：多继承方法

这种多继承方式有其优点，也有其缺点，表现为以下两方面:
(1)界面上的组件都成为窗体业务逻辑类 QmyWidget 的公共属性，外界可以直接访问。
    优点是访问方便
    缺点是过于开放，不符合面向对象严格封装的设计思想。

(2)界面上的组件与 QmyWidget 类里新定义的属性混合在一起了，不便于区分。
    当窗体上的界面组件较多，且窗体业务逻辑类里定义的属性也很多时，
    就难以区分哪个属性是界面上的组件，哪个属性是在业务逻辑类里新定义的，
    这样是不利于界面与业务逻辑分离的。

:Author: kylin.smq@qq.com
:Last Modified by: kylin.smq@qq.com
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from formHello import Ui_Form


class QmyWidget(QWidget, Ui_Form):
    # 定义了一个类 QmyWidget，称这个类为窗体的业务逻辑类
    def __init__(self, parent=None):
        # 调用父类构造函数，创建QWidget窗体
        super().__init__(parent)
        # 在多继承时，使用 super()得到的是第一个基类，在这里就是QWidget
        # 执行这条语句后，self 就是一个QWidget对象

        self.lab = "多重继承的 QmyWidget" # 新定义的一个变量
        self.setupUi(self) # self 是 QWidget 窗体，可作为参数传给 setupUi()
        self.labeHello.setText(self.lab)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app
    myWidget = QmyWidget()
    myWidget.show()
    myWidget.pushButton.setText("不关闭了")
    sys.exit(app.exec_())


