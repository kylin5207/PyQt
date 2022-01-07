# -*- coding:utf-8 -*-
"""
myDialog
与UI窗体类对应的业务逻辑类

:Author: kylin.smq@qq.com
:Last Modified by: kylin.smq@qq.com
"""
import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QDialog
from ui_dialog import Ui_Dialog


class QmyDialog(QDialog):
    def __init__(self, parent=None):
      super().__init__(parent)
      self.ui = Ui_Dialog()
      self.ui.setupUi(self)
      # 将3个radioButton按钮的clicked()信号与同一个槽函数关联
      self.ui.radioBlack.clicked.connect(self.do_setTextColor)
      self.ui.radioRed.clicked.connect(self.do_setTextColor)
      self.ui.radioBlue.clicked.connect(self.do_setTextColor)

    def on_btnClear_clicked(self):
        self.ui.textEdit.clear()

    def on_chkBoxBold_toggled(self, checked):
        font = self.ui.textEdit.font()
        font.setBold(checked)  # 根据checked判断选择状态
        self.ui.textEdit.setFont(font)

    def on_chkBoxUnder_clicked(self):
        checked = self.ui.chkBoxUnder.isChecked()  # 读取勾选状态
        font = self.ui.textEdit.font()
        font.setUnderline(checked)
        self.ui.textEdit.setFont(font)

    @pyqtSlot(bool)  # 修饰符指定参数类型，用于 overload 型的信号
    def on_chkBoxItalic_clicked(self, checked):
        font = self.ui.textEdit.font()
        font.setItalic(checked)
        self.ui.textEdit.setFont(font)

    # =========自定义槽函数========
    def do_setTextColor(self):  ##设置文本颜色
        plet = self.ui.textEdit.palette()  # 获取 palette
        # 获取三个RadioButton的选中状态
        if (self.ui.radioBlack.isChecked()):
            plet.setColor(QPalette.Text, Qt.black)
        elif (self.ui.radioRed.isChecked()):
            plet.setColor(QPalette.Text, Qt.red)
        elif (self.ui.radioBlue.isChecked()):
            plet.setColor(QPalette.Text, Qt.blue)
        self.ui.textEdit.setPalette(plet)


if  __name__ == "__main__":
   app = QApplication(sys.argv)
   form=QmyDialog()
   form.show()
   sys.exit(app.exec_())

