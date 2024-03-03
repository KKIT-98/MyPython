import re
import sys
from PyQt5 import QtCore
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

        """按钮"""
        self.TopBtn = QPushButton(self)
        # 设置按钮文本
        self.TopBtn.setText("顶置窗口")
        # 设置按钮位置
        self.TopBtn.move(230, 50)
        # 设置按钮大小
        self.TopBtn.resize(60, 30)
        # 设置按钮字体样式
        self.TopBtn.setFont(QFont("宋体", 10, QFont.Thin))

        """取消顶置按钮"""
        self.OffTopBtn = QPushButton(self)
        # 设置按钮文本
        self.OffTopBtn.setText("取消顶置")
        # 设置按钮位置
        self.OffTopBtn.move(230, 100)
        # 设置按钮大小
        self.OffTopBtn.resize(60, 30)
        # 设置按钮字体样式
        self.OffTopBtn.setFont(QFont("宋体", 10, QFont.Thin))

        """清除文本按钮"""
        self.ClearBtn = QPushButton(self)
        # 设置按钮文本
        self.ClearBtn.setText("清空内容")
        # 设置按钮位置
        self.ClearBtn.move(230, 150)
        # 设置按钮大小
        self.ClearBtn.resize(60, 30)
        # 设置按钮字体样式
        self.ClearBtn.setFont(QFont("宋体", 10, QFont.Thin))

        # 设置按钮事件
        # 转换按钮事件
        self.ChangeBtn.clicked.connect(self.ChangeTex)
        # 复制按钮事件
        self.CopyBtn.clicked.connect(self.CopyTex)
        # 置顶窗口按钮事件
        self.TopBtn.clicked.connect(self.TopWindow)
        # 取消置顶按钮事件
        self.OffTopBtn.clicked.connect(self.OffTopWindow)
        # 清空按钮事件
        self.ClearBtn.clicked.connect(self.ClearText)

    """点击转换按钮触发事件"""

    def ChangeTex(self):
        print("转换按钮被点击")
        gettext = self.TextEdit1.toPlainText().strip()
        # QMessageBox.warning(self,"警告！ 文本为空！！")
        if len(gettext) == 0:
            self.TextEdit1.setPlaceholderText("请输入文本")
        else:
            print(gettext)
            subtext = "('" + re.sub("\\n", "','", gettext) + "')"
            print("转换完后文本:" + subtext)
            self.TextEdit2.setText(subtext)

    """复制按钮触事件"""

    def CopyTex(self):
        print("复制按钮被点击")
        gettext1 = self.TextEdit2.toPlainText()
        self.TextEdit2.setFocus()
        self.TextEdit2.selectAll()
        self.TextEdit2.copy()

    """置顶窗口按钮触发事件"""
    def TopWindow(self):
        # 设置窗口置顶
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setVisible(True)

    """取消置顶按钮触发事件"""
    def OffTopWindow(self):
        # 取消窗口置顶
        self.setWindowFlags(QtCore.Qt.Widget)
        self.setVisible(True)

    """清空文本按钮触发事件"""
    def ClearText(self):
        self.TextEdit1.clear()
        self.TextEdit2.clear()


if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    # 创建一个空白控件(窗口)
    window = StrChangeOnQt5()
    # 显示窗口
    window.show()
    # 进入程序主循环，通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
