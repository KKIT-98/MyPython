import re
import sys

from PyQt5.Qt import *


class StrChangeOnQt5(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle("文本转换")
        # 禁止调整窗口大小
        self.setFixedSize(530, 750)
        # 设置窗口大小 可调整窗口大小
        # self.resize(530, 750)


if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    # 创建一个空白控件(窗口)
    window = StrChangeOnQt5()
    # 显示窗口
    window.show()
    # 进入程序主循环，通过exit函数确保主循环安全结束
    sys.exit(app.exec_())