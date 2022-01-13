# -*- coding:utf-8 -*-
"""
myDialog
与UI窗体类对应的业务逻辑类

:Author: kylin
:Last Modified by: kylin.smq@qq.com
"""
import sys

from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QObject
from PyQt5.QtGui import QPalette, QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from ui_widget import Ui_Widget

class Human(QObject):
    # pyqtSignal为一个类定义新的信号，types=str
    nameChanged = pyqtSignal(str)
    ageChanged = pyqtSignal([int], [str])

    def __init__(self, name="Mike", age=10, parent=None):
        super().__init__(parent)
        self.setAge(age)
        self.setName(name)

    def setAge(self, age):
        self.__age = age
        # 发射int参数信号
        self.ageChanged.emit(self.__age)
        if age <= 18:
            ageInfo = "少年👶"
        elif (18 < age <= 35):
            ageInfo = "年轻人👧"
        elif (35 < age <= 55):
            ageInfo = "中年人👨"
        elif (55 < age <= 80):
            ageInfo = "老人👴"
        else:
            ageInfo = "🤶"

        self.ageChanged[str].emit(ageInfo)  # 发射 str 参数信号

    def setName(self, name):
        self.__name = name
        # 通过emit发射信号
        self.nameChanged.emit(self.__name)


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.boy = Human("boy", 12)
        self.boy.nameChanged.connect(self.do_nameChanged)
        self.boy.ageChanged.connect(self.do_ageChanged_int)
        self.boy.ageChanged[str].connect(self.do_ageChanged_str)

    def on_sliderSetAge_valueChanged(self, value):
        self.boy.setAge(value)

    def on_btnSetName_clicked(self):
        hisName = self.ui.editNameInput.text()
        self.boy.setName(hisName)

    @pyqtSlot(str)
    def do_nameChanged(self, name):
        print("Hello, " + name)

    @pyqtSlot(int)
    def do_ageChanged_int(self, age):
        self.ui.editAgeInt.setText(str(age))

    @pyqtSlot(str)
    def do_ageChanged_str(self, info):
        self.ui.editAgeStr.setText(info)


if  __name__ == "__main__":
   app = QApplication(sys.argv)
   # 从资源文件里提取了一个图标作为应用程序的图标
   icon = QIcon(":/icons/images/app.ico")
   app.setWindowIcon(icon)
   widget=QmyWidget()
   widget.show()
   sys.exit(app.exec_())

