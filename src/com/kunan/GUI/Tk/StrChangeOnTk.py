import re
import tkinter as tk
from tkinter import messagebox, INSERT

# 设置窗口居中
def center_window(window, width, height):
    # 获取显示屏宽度
    screenwidth = window.winfo_screenwidth()
    # 获取显示屏高度
    screenheight = window.winfo_screenheight()
    # 设置窗口居中参数
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    # 设置窗口位置
    window.geometry(size)


# 实例化object 建立窗口window
window = tk.Tk()
# 窗口标题
window.title("文本转换")
# 设置窗口大小且居中
center_window(window, 530, 750)

# 设置禁止缩放
window.resizable(False, False)

# 设置文本标签1 待转换文本
labelText1 = tk.Label(window, text='待转换文本', font=('黑体', 16, 'bold'))
# 放置文本标签1
labelText1.place(x=50, y=10)

# 设置文本标签2 转换完文本
labelText1 = tk.Label(window, text='转换完文本', font=('黑体', 16, 'bold'))
# 放置文本标签2
labelText1.place(x=350, y=10)

# 文本框1 待转换文本
# width 一行可见的字符数  height显示的行数
text1 = tk.Text(window, width=20, height=30, font=('TimesNewRoman', 14))
# 创建Scrollbar对象
scroll1 = tk.Scrollbar(window, orient='vertical')
scroll1.place(x=220, y=50, height=580)
text1.place(x=20, y=50)
scroll1.config(command=text1.yview)
text1.config(yscrollcommand=scroll1.set)

# 文本框2 转换完文本
# width 一行可见的字符数  height显示的行数
text2 = tk.Text(window, width=20, height=30, font=('TimesNewRoman', 14))
# 创建Scrollbar对象
scroll2 = tk.Scrollbar(window, orient='vertical')
scroll2.place(x=515, y=50, height=580)
text2.place(x=320, y=50)
scroll2.config(command=text2.yview)
text2.config(yscrollcommand=scroll2.set)


# 点击转换按钮触发事件
def ChangeTex():
    print("转换按钮被点击")
    gettext1 = text1.get('1.0', 'end').strip()
    if len(gettext1) == 0:
        print("输入 为空")
        messagebox.showinfo("提示", "请输入文本")
    else:
        print(gettext1)
        subtext = "('" + re.sub("\\n", "','", gettext1) + "')"
        # 先清空内容再插入实现覆盖操作
        text2.delete('1.0', 'end')
        text2.insert(INSERT, subtext)
        # 设置焦点选中效果
        text2.focus_set()
        text2.tag_add('sel', '1.0', 'end')
        print(subtext)


# 点击复制按钮触发事件
def CopyTex():
    gettext2 = text2.get('1.0', 'end').strip()
    # 复制到剪切板
    text2.clipboard_clear()
    text2.clipboard_append(gettext2)


# 点击置顶窗口按钮触发事件
def TopWindow():
    window.attributes('-topmost', True)


# 点击取消置顶按钮触发事件
def OffWindow():
    window.attributes('-topmost', False)


# 点击清空文本按钮触发事件
def ClearText():
    text1.delete('1.0', 'end')
    text2.delete('1.0', 'end')


# 转换按钮
ChangeBtn = tk.Button(window, text='转 换', font=('宋体', 16, 'bold'), width=16, height=2, command=ChangeTex)
ChangeBtn.place(x=20, y=660)

# 复制按钮
ChangeBtn = tk.Button(window, text='复 制', font=('宋体', 16, 'bold'), width=16, height=2, command=CopyTex)
ChangeBtn.place(x=320, y=660)

# 置顶窗口按钮
ChangeBtn = tk.Button(window, text='置顶窗口', font=('宋体', 10),  width=8, height=1, command=TopWindow)
ChangeBtn.place(x=240, y=50)

# 取消置顶按钮
ChangeBtn = tk.Button(window, text='取消置顶', font=('宋体', 10),  width=8, height=1, command=OffWindow)
ChangeBtn.place(x=240, y=100)

# 清空文本按钮
ChangeBtn = tk.Button(window, text='清空文本', font=('宋体', 10), width=8, height=1, command=ClearText)
ChangeBtn.place(x=240, y=150)

window.mainloop()