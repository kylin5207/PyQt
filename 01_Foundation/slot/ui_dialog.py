# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 317)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox1 = QtWidgets.QGroupBox(Dialog)
        self.groupBox1.setObjectName("groupBox1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.chkBoxBold = QtWidgets.QCheckBox(self.groupBox1)
        self.chkBoxBold.setObjectName("chkBoxBold")
        self.horizontalLayout_1.addWidget(self.chkBoxBold)
        self.chkBoxItalic = QtWidgets.QCheckBox(self.groupBox1)
        self.chkBoxItalic.setObjectName("chkBoxItalic")
        self.horizontalLayout_1.addWidget(self.chkBoxItalic)
        self.chkBoxUnder = QtWidgets.QCheckBox(self.groupBox1)
        self.chkBoxUnder.setObjectName("chkBoxUnder")
        self.horizontalLayout_1.addWidget(self.chkBoxUnder)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_1)
        self.verticalLayout.addWidget(self.groupBox1)
        self.groupBox2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox2.setObjectName("groupBox2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioBlue = QtWidgets.QRadioButton(self.groupBox2)
        self.radioBlue.setObjectName("radioBlue")
        self.horizontalLayout_4.addWidget(self.radioBlue)
        self.radioBlack = QtWidgets.QRadioButton(self.groupBox2)
        self.radioBlack.setObjectName("radioBlack")
        self.horizontalLayout_4.addWidget(self.radioBlack)
        self.radioRed = QtWidgets.QRadioButton(self.groupBox2)
        self.radioRed.setObjectName("radioRed")
        self.horizontalLayout_4.addWidget(self.radioRed)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox2)
        self.textEdit = QtWidgets.QPlainTextEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btnClear = QtWidgets.QPushButton(Dialog)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout_5.addWidget(self.btnClear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_5.addWidget(self.btnOK)
        self.btnClose = QtWidgets.QPushButton(Dialog)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_5.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        self.btnOK.clicked.connect(Dialog.accept)
        self.btnClose.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.chkBoxBold, self.chkBoxItalic)
        Dialog.setTabOrder(self.chkBoxItalic, self.chkBoxUnder)
        Dialog.setTabOrder(self.chkBoxUnder, self.textEdit)
        Dialog.setTabOrder(self.textEdit, self.btnClear)
        Dialog.setTabOrder(self.btnClear, self.btnOK)
        Dialog.setTabOrder(self.btnOK, self.btnClose)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox1.setTitle(_translate("Dialog", "GroupBox"))
        self.chkBoxBold.setText(_translate("Dialog", "Bold"))
        self.chkBoxItalic.setText(_translate("Dialog", "Italic"))
        self.chkBoxUnder.setText(_translate("Dialog", "Underline"))
        self.groupBox2.setTitle(_translate("Dialog", "GroupBox"))
        self.radioBlue.setText(_translate("Dialog", "Blue"))
        self.radioBlack.setText(_translate("Dialog", "Black"))
        self.radioRed.setText(_translate("Dialog", "Red"))
        self.textEdit.setPlainText(_translate("Dialog", "我是钱老板💰"))
        self.btnClear.setText(_translate("Dialog", "清空"))
        self.btnOK.setText(_translate("Dialog", "确认"))
        self.btnClose.setText(_translate("Dialog", "退出"))