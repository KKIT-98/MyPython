import re
import sys
from PyQt5.Qt import *

import ctypes


class StrChangeOnQt5(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle("文本转换")
        # 禁止调整窗口大小
        self.setFixedSize(530, 750)
        # 设置窗口大小 可调整窗口大小
        # self.resize(530, 750)

        # 创建文本标签控件: 待转换文本
        self.labelTex1 = QLabel(self)
        # 为控件设置文本 待转换
        self.labelTex1.setText("待转换文本")
        # 字体样式设置
        self.labelTex1.setFont(QFont)

if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    # 创建一个空白控件(窗口)
    window = StrChangeOnQt5()
    # 显示窗口
    window.show()
    # 进入程序主循环，通过exit函数确保主循环安全结束
    sys.exit(app.exec_())