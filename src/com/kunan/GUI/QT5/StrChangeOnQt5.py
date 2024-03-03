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

        # 创建文本标签控件: 待转换文本
        self.labelTex1 = QLabel(self)
        # 为控件设置文本 待转换
        self.labelTex1.setText("待转换文本")
        # 字体样式设置
        self.labelTex1.setFont(QFont("黑体", 18, QFont.Bold))
        # 移动控件的位置
        self.labelTex1.move(50, 10)

        # 创建文本标签控件: 转换后文本
        self.labelTex2 = QLabel(self)
        # 为控件设置文本 待转换
        self.labelTex2.setText("转换后文本")
        # 字体样式设置
        self.labelTex2.setFont(QFont("黑体", 18, QFont.Bold))
        # 移动控件的位置
        self.labelTex2.move(350, 10)

        """多行文本框 待转换文本"""
        self.TextEdit1 = QTextEdit(self)
        # 设置字体颜色
        # self.TextEdit1.setTextColor(QColor(0, 0, 225))
        # 设置字体背景颜色
        # self.TextEdit1.setTextBackgroundColor(QColor(255, 0, 255))
        # 设置字体样式
        self.TextEdit1.setFont(QFont("TimesNewRoman", 14, QFont.Thin))
        # 水平滚动条
        # self.TextEdit1.setHorizontalScrollBar()
        # 移动控件的位置
        self.TextEdit1.move(20, 50)
        # 设置控件大小
        self.TextEdit1.resize(200, 600)

        """多行文本框 转换完文本"""
        self.TextEdit2 = QTextEdit(self)
        # 设置字体颜色
        # self.TextEdit2.setTextColor(QColor(0, 0, 225))
        # 设置字体背景颜色
        # self.TextEdit2.setTextBackgroundColor(QColor(255, 0, 255))
        # 设置字体样式
        self.TextEdit2.setFont(QFont("TimesNewRoman", 14, QFont.Thin))
        # 水平滚动条
        # self.TextEdit1.setHorizontalScrollBar()
        # 移动控件的位置
        self.TextEdit2.move(300, 50)
        # 设置控件大小
        self.TextEdit2.resize(200, 600)

        """转换按钮"""
        self.ChangeBtn = QPushButton(self)
        # 设置按钮文本
        self.ChangeBtn.setText("转 换")
        # 设置按钮位置
        self.ChangeBtn.move(20, 660)
        # 设置按钮大小
        self.ChangeBtn.resize(200, 50)
        # 设置按钮字体样式
        self.ChangeBtn.setFont(QFont("宋体", 14, QFont.Bold))

        """复制按钮"""
        self.CopyBtn = QPushButton(self)
        # 设置按钮文本
        self.CopyBtn.setText("复 制")
        # 设置按钮位置
        self.CopyBtn.move(300, 660)
        # 设置按钮大小
        self.CopyBtn.resize(200, 50)
        # 设置按钮字体样式
        self.CopyBtn.setFont(QFont("宋体", 14, QFont.Bold))



if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    # 创建一个空白控件(窗口)
    window = StrChangeOnQt5()
    # 显示窗口
    window.show()
    # 进入程序主循环，通过exit函数确保主循环安全结束
    sys.exit(app.exec_())