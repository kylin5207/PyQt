# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_Age = QtWidgets.QGroupBox(Widget)
        self.groupBox_Age.setObjectName("groupBox_Age")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_Age)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_Age)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sliderSetAge = QtWidgets.QSlider(self.groupBox_Age)
        self.sliderSetAge.setMaximum(100)
        self.sliderSetAge.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSetAge.setObjectName("sliderSetAge")
        self.gridLayout.addWidget(self.sliderSetAge, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_Age)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.editAgeInt = QtWidgets.QLineEdit(self.groupBox_Age)
        self.editAgeInt.setObjectName("editAgeInt")
        self.gridLayout.addWidget(self.editAgeInt, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_Age)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.editAgeStr = QtWidgets.QLineEdit(self.groupBox_Age)
        self.editAgeStr.setObjectName("editAgeStr")
        self.gridLayout.addWidget(self.editAgeStr, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_Age)
        self.groupBox_Name = QtWidgets.QGroupBox(Widget)
        self.groupBox_Name.setObjectName("groupBox_Name")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_Name)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_Name)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.editNameInput = QtWidgets.QLineEdit(self.groupBox_Name)
        self.editNameInput.setObjectName("editNameInput")
        self.gridLayout_2.addWidget(self.editNameInput, 0, 1, 1, 1)
        self.btnSetName = QtWidgets.QPushButton(self.groupBox_Name)
        self.btnSetName.setObjectName("btnSetName")
        self.gridLayout_2.addWidget(self.btnSetName, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_Name)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.editNameHello = QtWidgets.QLineEdit(self.groupBox_Name)
        self.editNameHello.setObjectName("editNameHello")
        self.gridLayout_2.addWidget(self.editNameHello, 1, 1, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_Name)
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(159, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnClose = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/go.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        spacerItem2 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.groupBox_Age.setTitle(_translate("Widget", "年龄设置"))
        self.label.setText(_translate("Widget", "设置年龄(0~100)"))
        self.label_2.setText(_translate("Widget", "ageChanged(int)响应"))
        self.label_3.setText(_translate("Widget", "ageChanged(str)响应"))
        self.groupBox_Name.setTitle(_translate("Widget", "姓名设置"))
        self.label_4.setText(_translate("Widget", "输入姓名"))
        self.btnSetName.setText(_translate("Widget", "设置姓名"))
        self.label_5.setText(_translate("Widget", "nameChanged(str)响应"))
        self.label_6.setText(_translate("Widget", "LR"))
        self.btnClose.setText(_translate("Widget", "关闭"))
import res_rc
