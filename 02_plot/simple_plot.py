import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

"""
画图模版 pyqt和matplotlib联合
程序是用 PyQt5 的 GUI 应用程序框架创建的。
为了减少程序的复杂度，没有使用可视化方法设计 UI 窗体，而是采用纯代码的方式。
程序中定义了一个基于 QMainWindow 的窗口类 QmyMainWindow，
界面构造和绘图都是在 QmyMainWindow 的构造函数中实现的。
"""

class QmyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt5 matplotlib example')
        self.setGeometry(10, 10, 600, 400)

        mpl.rcParams['font.sans-serif'] = ['KaiTi']  # 设置中文
        mpl.rcParams['font.size'] = 12  # 字体大小
        mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号
        self.__iniFigure()  # 创建绘图系统，初始化窗口
        self.__drawFigure()  # 绘图

    def __iniFigure(self):  # 创建绘图系统，初始化窗口
        self.__fig = Figure(figsize=(8, 5))  # 单位英寸
        self.__fig.suptitle("plot in GUI application")   # 总的图标题
        figCanvas = FigureCanvas(self.__fig)  # 创建FigureCanvas对象
        naviToolbar = NavigationToolbar(figCanvas, self)  # 创建工具栏
        naviToolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(naviToolbar)  # 添加工具栏到主窗口
        self.setCentralWidget(figCanvas)

    def __drawFigure(self):
        t = np.linspace(0, 10, 40)
        y1 = np.sin(t)
        y2 = np.cos(2*t)

        # 三角函数
        plt.subplot(2, 1, 1)
        plt.plot(t, y1, 'r-o', label='$y=sinx$', linewidth=1, markersize=5)
        plt.plot(t, y2, 'b:', label='$y=cosin(2t)$', linewidth=2)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("triangle function")
        plt.xlim(0, 10)
        plt.ylim(-1.5, 1.5)
        plt.legend()

        # 柱状图
        plt.subplot(2, 1, 2)
        week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
        sales = np.random.randint(200, 400, 7)
        plt.bar(week, sales)
        plt.xlabel('week days')
        plt.ylabel('sales')
        plt.title('Sales of each day')

        plt.suptitle("plot show")
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QmyMainWindow()
    sys.exit(app.exec_())
