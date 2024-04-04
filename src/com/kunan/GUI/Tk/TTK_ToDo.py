import re
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap import Window, WARNING, INFO, SUCCESS
from pathlib import Path
root = Window(
    size=(580, 450),
    resizable=(False, False),  # 禁止窗口缩放
    title='todo'  # 窗口标题
)
# 窗口居中
root.place_window_center()


xx = 50
tex_x = 55
# 日期
dt = ttk.DateEntry(width=10, dateformat="%Y-%m-%d")
dt.place(x=1, y=1)

# 文本
# todayText = ttk.Label(root, text=dt.entry.get() + "日任务", font=('宋体', 16, 'bold'))
# todayText.place(x=150, y=60)

# 获取当前电脑用户目录下文档目录 需先安装 pip install pathlib
home_directory = str(Path.home()) + '/Documents/'
root.title(dt.entry.get() + '日任务')

style = ttk.Style()
theme_names = style.theme_names()  # 以列表的形式返回多个主题名

# 创建一个主题筛选框将主题名放进去
theme_cob = ttk.Combobox(master=root,
                         values=theme_names,
                         width=7,
                         font=('Consolas', 12, 'bold')
                         )
theme_cob.place(x=380, y=1)
theme_cob.current(0)  # 默认筛选框为第一个主题

# 绑定选择主题后的方法
def chang_theme(event):
    theme_cob_value = theme_cob.get()
    style.theme_use(theme_cob_value)  # 设置主题为选中的主题


# 绑定选择主题后的执行的方法
theme_cob.bind('<<ComboboxSelected>>', chang_theme)

theme_cob_lab = ttk.Label(root, text='主题选择:', font=('微软雅黑', 12, 'bold'))
theme_cob_lab.place(x=290, y=1)

# 设置窗口置顶标识
top_flag = True


# 点击置顶窗口、取消置顶按钮触发事件
def TopWindow():
    global top_flag
    if top_flag:
        root.attributes('-topmost', True)  # 置顶窗口
        off_top_btn()
        top_flag = False
    else:
        root.attributes('-topmost', False)  # 取消置顶
        on_top_btn()
        top_flag = True

# 置顶窗口生成按钮
def on_top_btn():
    OnTopBtn = ttk.Button(root, text='置顶窗口', command=TopWindow)
    OnTopBtn.place(x=500, y=1)
# 取消置顶生成按钮
def off_top_btn():
    OffTopBtn = ttk.Button(root, text='取消置顶', command=TopWindow)
    OffTopBtn.place(x=500, y=1)


# 点击取消置顶按钮触发事件
# def OffWindow():
#    root.attributes('-topmost', False)


def save():
    print("保存按钮点击")
    # 获得所有组件名称
    children = root.winfo_children()
    index1 = 0
    index2 = 0
    mylist1 = []  # 存放任务
    mylist2 = []  # 存放任务状态
    # 遍历组件寻找文本框
    for child in children:
        # 如果组件为文本框 且不为日期文本框
        if re.search('entry', str(child)) and str(child) not in '.!dateentry':
            # print(str(child))
            get_entry = root.nametowidget(child)  # 获得文本框
            get_entry_text = re.sub("\\n", "", get_entry.get())  # 获得文本框文本且将换行符替换
            mylist1.insert(index1, get_entry_text)  # 将文本框内容插入列表1中
            index1 = index1 + 1
    # 遍历组件寻找组合框
    for child in children:
        if re.search('combobox', str(child)) and str(child) != '.!combobox':
            # print(str(child))
            get_cob = root.nametowidget(child)  # 获取组合框
            get_cob_status = get_cob.get()   # 获取组合框文本
            mylist2.insert(index2, get_cob_status + "\n")  # 将组合框文本内容加上换行插入列表2中
            index2 = index2 + 1

    # 生成新的列表3 如 '吃完,'进行中\n'
    mylist3 = [a + "," + b for a, b in zip(mylist1, mylist2)]
    print(mylist1)
    print(mylist2)
    print(mylist3)
    dt.focus_set()
    try:
        with open(home_directory + 'tasksave_' + dt.entry.get(), 'w') as file:
             file.writelines(mylist3)
    except:
        print("文件不存在")
        root.title(dt.entry.get() + '日任务')
    root.title(dt.entry.get() + '日任务')
    # 保存成功弹窗
    messagebox.showinfo('提示', '保存成功')

# 获取任务列表
def getTask():
    # print("获取任务")
    children = root.winfo_children()
    dt.focus_set()
    index1 = 0
    index2 = 0
    try:
        with open(home_directory + 'tasksave_' + dt.entry.get(), 'r') as file:  # 打开当前日期保存的任务列表文件
            lines = file.readlines()
            # 遍历组件寻找文本框
            for child in children:
                if re.search('entry', str(child)) and str(child) not in '.!dateentry':
                    get_entry = root.nametowidget(child)  # 获取文本框
                    get_entry.delete('0', 'end')  # 先删除文本框内容
                    get_entry.insert('0', lines[index1].split(',')[0])  # 读取文件一行按‘,’切分取数组第一个为任务名保存插入到文本框中
                    get_status = lines[index1].split(',')[1]            # 读取文件一行按‘,’切分取数组第二个为任务名对应的状态
                    # 分别按不同任务状态更改文本框主题
                    if get_status == '进行中\n':
                        child.configure(bootstyle=INFO)
                    elif get_status == '已完成\n':
                        child.configure(bootstyle=SUCCESS)
                    elif get_status == '未开始\n':
                        child.configure(bootstyle=WARNING)
                    index1 = index1 + 1
            # 遍历组件寻找组合框
            for CobChild in children:
                if re.search('combobox', str(CobChild)) and str(CobChild) != '.!combobox':  # 过滤掉第一个组合框 也就是主题选择主题框
                    get_status = lines[index2].split(',')[1]  # 读取文件一行按‘,’切分取数组第二个为任务名对应的状态
                    # 分别按不同任务状态更改组合框主题
                    if get_status == '进行中\n':
                        CobChild.configure(bootstyle=INFO)
                        CobChild.current(0)
                    elif get_status == '已完成\n':
                        CobChild.configure(bootstyle=SUCCESS)
                        CobChild.current(0)
                    elif get_status == '未开始\n':
                        CobChild.configure(bootstyle=WARNING)
                        CobChild.current(0)
                    index2 = index2 + 1
            root.title(dt.entry.get() + '日任务')
    # 如果当前日期任务列表文件不存在 在文本框中填默认文本 <空白>
    except:
        print("文件不存在")
        lines = []
        for i in range(10):
            lines.insert(i, '<空白>')
        print(lines)
        for child in children:
            if re.search('entry', str(child)) and str(child) not in '.!dateentry':
                get_entry = root.nametowidget(child)
                get_entry.delete('0', 'end')
                get_entry.insert('0', lines[index1])
                child.configure(bootstyle=WARNING)
                index1 = index1 + 1

        root.title(dt.entry.get() + '日任务')

# 按钮
# 置顶窗口按钮
ChangeBtn = ttk.Button(root, text='置顶窗口', width=8, command=TopWindow)
ChangeBtn.place(x=500, y=1)

# 保存、获取任务按钮
GetBtn = ttk.Button(root, text='获取任务', width=8, command=getTask)
GetBtn.place(x=120, y=1)

Savebtn = ttk.Button(root, text='保存任务', width=8, command=save)
Savebtn.place(x=205, y=1)


def ensure(arg1, arg2):
    def MyEnsure(event):
        if arg1.get() == '进行中':
            arg1.configure(bootstyle=INFO)
            arg2.configure(bootstyle=INFO)
        elif arg1.get() == '已完成':
            arg1.configure(bootstyle=SUCCESS)
            arg2.configure(bootstyle=SUCCESS)
        elif arg1.get() == '未开始':
            arg1.configure(bootstyle=WARNING)
            arg2.configure(bootstyle=WARNING)
    return MyEnsure


# 批量生成8个文本框、文本标签、组合框
for i in range(10):
    i = i + 1
    num = i
    tex = 't_' + str(i)
    tex = ttk.Label(root, text=str(num) + '.', font=('宋体', 14))
    tex.place(x=0, y=tex_x)
    cob1 = 'cob_' + str(i)
    ent = 'ent_' + str(i)
    ent = ttk.Entry(root, width=55, font=('宋体', 12))
    ent.place(x=25, y=xx)
    cob1 = ttk.Combobox(master=root, bootstyle=WARNING, font=('宋体', 12, 'bold'), values=['进行中', '已完成', '未开始'], width=6)
    cob1.current(2)
    cob1.place(x=480, y=xx)
    xx = xx + 38
    tex_x = tex_x + 38
    cob1.bind('<<ComboboxSelected>>', ensure(cob1, ent))
# 初始化获取当前日期的任务
getTask()
root.mainloop()
