# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 506)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 541, 361))
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 539, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LabPicture = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.LabPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.LabPicture.setObjectName("LabPicture")
        self.verticalLayout_2.addWidget(self.LabPicture)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 860, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuPic = QtWidgets.QMenu(self.menuBar)
        self.menuPic.setObjectName("menuPic")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeFiles = QtWidgets.QTreeWidget(self.dockWidgetContents)
        self.treeFiles.setColumnCount(2)
        self.treeFiles.setObjectName("treeFiles")
        self.treeFiles.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeFiles.headerItem().setFont(0, font)
        self.treeFiles.headerItem().setTextAlignment(1, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeFiles.headerItem().setFont(1, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeFiles)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/15.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/open3.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/31.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_2.setIcon(0, icon2)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setIcon(0, icon2)
        self.treeFiles.header().setDefaultSectionSize(150)
        self.verticalLayout.addWidget(self.treeFiles)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actTree_AddFolder = QtWidgets.QAction(MainWindow)
        self.actTree_AddFolder.setIcon(icon1)
        self.actTree_AddFolder.setObjectName("actTree_AddFolder")
        self.actTree_AddFiles = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons/824.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actTree_AddFiles.setIcon(icon3)
        self.actTree_AddFiles.setObjectName("actTree_AddFiles")
        self.actZoomIn = QtWidgets.QAction(MainWindow)
        self.actZoomIn.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons/418.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomIn.setIcon(icon4)
        self.actZoomIn.setObjectName("actZoomIn")
        self.actZoomOut = QtWidgets.QAction(MainWindow)
        self.actZoomOut.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/icons/416.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomOut.setIcon(icon5)
        self.actZoomOut.setObjectName("actZoomOut")
        self.actZoomRealSize = QtWidgets.QAction(MainWindow)
        self.actZoomRealSize.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/icons/414.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomRealSize.setIcon(icon6)
        self.actZoomRealSize.setObjectName("actZoomRealSize")
        self.actZoomFitW = QtWidgets.QAction(MainWindow)
        self.actZoomFitW.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/icons/424.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomFitW.setIcon(icon7)
        self.actZoomFitW.setObjectName("actZoomFitW")
        self.actTree_DeleteItem = QtWidgets.QAction(MainWindow)
        self.actTree_DeleteItem.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/icons/delete1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actTree_DeleteItem.setIcon(icon8)
        self.actTree_DeleteItem.setObjectName("actTree_DeleteItem")
        self.actClose = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/icons/exit.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actClose.setIcon(icon9)
        self.actClose.setObjectName("actClose")
        self.actZoomFitH = QtWidgets.QAction(MainWindow)
        self.actZoomFitH.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/icons/426.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomFitH.setIcon(icon10)
        self.actZoomFitH.setObjectName("actZoomFitH")
        self.actTree_ScanItems = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/icons/fold.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actTree_ScanItems.setIcon(icon11)
        self.actTree_ScanItems.setObjectName("actTree_ScanItems")
        self.actDockVisible = QtWidgets.QAction(MainWindow)
        self.actDockVisible.setCheckable(True)
        self.actDockVisible.setChecked(True)
        self.actDockVisible.setIcon(icon6)
        self.actDockVisible.setObjectName("actDockVisible")
        self.actDockFloat = QtWidgets.QAction(MainWindow)
        self.actDockFloat.setCheckable(True)
        self.actDockFloat.setChecked(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/icons/814.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actDockFloat.setIcon(icon12)
        self.actDockFloat.setObjectName("actDockFloat")
        self.menuPic.addAction(self.actTree_AddFolder)
        self.menuPic.addAction(self.actTree_AddFiles)
        self.menuPic.addAction(self.actTree_DeleteItem)
        self.menuPic.addAction(self.actTree_ScanItems)
        self.menuPic.addSeparator()
        self.menuPic.addAction(self.actClose)
        self.menuView.addAction(self.actZoomIn)
        self.menuView.addAction(self.actZoomOut)
        self.menuView.addAction(self.actZoomRealSize)
        self.menuView.addAction(self.actZoomFitW)
        self.menuView.addAction(self.actZoomFitH)
        self.menuBar.addAction(self.menuPic.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.mainToolBar.addAction(self.actTree_AddFolder)
        self.mainToolBar.addAction(self.actTree_AddFiles)
        self.mainToolBar.addAction(self.actTree_DeleteItem)
        self.mainToolBar.addAction(self.actTree_ScanItems)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actZoomIn)
        self.mainToolBar.addAction(self.actZoomOut)
        self.mainToolBar.addAction(self.actZoomRealSize)
        self.mainToolBar.addAction(self.actZoomFitW)
        self.mainToolBar.addAction(self.actZoomFitH)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actDockFloat)
        self.mainToolBar.addAction(self.actDockVisible)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actClose)

        self.retranslateUi(MainWindow)
        self.actClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo3_9  QTreeWidget，QDockWidget"))
        self.LabPicture.setText(_translate("MainWindow", "待显示图片"))
        self.menuPic.setTitle(_translate("MainWindow", "目录树"))
        self.menuView.setTitle(_translate("MainWindow", "视图"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "图片目录树"))
        self.treeFiles.headerItem().setText(0, _translate("MainWindow", "节点"))
        self.treeFiles.headerItem().setText(1, _translate("MainWindow", "节点类型"))
        __sortingEnabled = self.treeFiles.isSortingEnabled()
        self.treeFiles.setSortingEnabled(False)
        self.treeFiles.topLevelItem(0).setText(0, _translate("MainWindow", "图片文件"))
        self.treeFiles.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "分组节点"))
        self.treeFiles.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "图片节点"))
        self.treeFiles.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "分组2"))
        self.treeFiles.topLevelItem(0).child(1).child(0).setText(0, _translate("MainWindow", "图片2"))
        self.treeFiles.setSortingEnabled(__sortingEnabled)
        self.actTree_AddFolder.setText(_translate("MainWindow", "添加目录..."))
        self.actTree_AddFolder.setToolTip(_translate("MainWindow", "添加目录"))
        self.actTree_AddFolder.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actTree_AddFiles.setText(_translate("MainWindow", "添加文件..."))
        self.actTree_AddFiles.setToolTip(_translate("MainWindow", "添加文件"))
        self.actTree_AddFiles.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actZoomIn.setText(_translate("MainWindow", "放大"))
        self.actZoomIn.setToolTip(_translate("MainWindow", "放大图片"))
        self.actZoomIn.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actZoomOut.setText(_translate("MainWindow", "缩小"))
        self.actZoomOut.setToolTip(_translate("MainWindow", "缩小图片"))
        self.actZoomOut.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actZoomRealSize.setText(_translate("MainWindow", "实际大小"))
        self.actZoomRealSize.setToolTip(_translate("MainWindow", "图片实际大小显示"))
        self.actZoomFitW.setText(_translate("MainWindow", "适合宽度"))
        self.actZoomFitW.setToolTip(_translate("MainWindow", "适合宽度显示"))
        self.actZoomFitW.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actTree_DeleteItem.setText(_translate("MainWindow", "删除节点"))
        self.actTree_DeleteItem.setToolTip(_translate("MainWindow", "删除节点"))
        self.actClose.setText(_translate("MainWindow", "退出"))
        self.actClose.setToolTip(_translate("MainWindow", "退出本系统"))
        self.actZoomFitH.setText(_translate("MainWindow", "适合高度"))
        self.actZoomFitH.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actTree_ScanItems.setText(_translate("MainWindow", "遍历节点"))
        self.actTree_ScanItems.setToolTip(_translate("MainWindow", "遍历节点"))
        self.actDockVisible.setText(_translate("MainWindow", "窗体可见"))
        self.actDockVisible.setToolTip(_translate("MainWindow", "窗体可见"))
        self.actDockFloat.setText(_translate("MainWindow", "窗体浮动"))
        self.actDockFloat.setToolTip(_translate("MainWindow", "窗体浮动"))

import res_rc
