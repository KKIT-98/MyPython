import re

import ttkbootstrap as ttk
from ttkbootstrap import Window, WARNING, INFO, SUCCESS

root = Window(
    size=(580, 450),
    resizable=(False, False)
)
# 窗口居中
root.place_window_center()

xx = 50 + 50
tex_x = 55 + 50
# 日期
dt = ttk.DateEntry(width=10, dateformat="%Y-%m-%d")
dt.place(x=170, y=1)

# 文本
todayText = ttk.Label(root, text=dt.entry.get() + "日任务", font=('宋体', 16, 'bold'))
todayText.place(x=150, y=60)


# 点击置顶窗口按钮触发事件
def TopWindow():
    root.attributes('-topmost', True)


# 点击取消置顶按钮触发事件
def OffWindow():
    root.attributes('-topmost', False)


def save():
    print("保存")
    children = root.winfo_children()
    index1 = 0
    index2 = 0
    mylist1 = []
    mylist2 = []

    for child in children:
        if re.search('entry', str(child)) and str(child) not in '.!dateentry':
            print(str(child))
            get_entry = root.nametowidget(child)
            get_entry_text = re.sub("\\n", "", get_entry.get())
            mylist1.insert(index1, get_entry_text)
            index1 = index1 + 1
    for child in children:
        if re.search('combobox', str(child)):
            print(str(child))
            get_cob = root.nametowidget(child)
            get_cob_status = get_cob.get()
            mylist2.insert(index2, get_cob_status + "\n")
            index2 = index2 + 1

    mylist3 = [a + "," + b for a, b in zip(mylist1, mylist2)]
    print(mylist1)
    print(mylist2)
    print(mylist3)
    dt.focus_set()
    try:
        with open('./tasksave_' + dt.entry.get() + '.txt', 'w') as file:
             file.writelines(mylist3)
    except:
        print("文件不存在")
        todayText.configure(text=dt.entry.get() + "日任务")
    todayText.configure(text=dt.entry.get() + "日任务")


def getTask():
    print("获取任务")
    children = root.winfo_children()
    dt.focus_set()
    index = 0
    try:
        with open('./tasksave_' + dt.entry.get() + '.txt', 'r') as file:
            lines = file.readlines()
            for child in children:
                if re.search('entry', str(child)) and str(child) not in '.!dateentry':
                    get_entry = root.nametowidget(child)
                    get_entry.delete('0', 'end')
                    get_entry.insert('0', lines[index].split(',')[0])
                    get_status = lines[index].split(',')[1]
                    if get_status == '进行中\n':
                        child.configure(bootstyle=INFO)
                    elif get_status == '进行中\n':
                        child.configure(bootstyle=SUCCESS)
                    elif get_status == '进行中\n':
                        child.configure(bootstyle=WARNING)
                    index = index + 1
    except:
        print("文件不存在")
        lines = []
        for i in range(9):
            lines.insert(i, '<空白>')
        print(lines)
        for child in children:
            if re.search('entry', str(child)) and str(child) not in '.!dateentry':
                get_entry = root.nametowidget(child)
                get_entry.delete('0', 'end')
                get_entry.insert('0', lines[index])
                child.configure(bootstyle=WARNING)
                index = index + 1
        todayText.configure(text=dt.entry.get() + "日任务")

# 按钮
# 置顶窗口按钮
ChangeBtn = ttk.Button(root, text='置顶窗口', width=8, command=TopWindow)
ChangeBtn.place(x=1, y=1)

# 取消置顶按钮
ChangeBtn = ttk.Button(root, text='取消置顶', width=8, command=OffWindow)
ChangeBtn.place(x=85, y=1)

# 保存、获取任务按钮
Savebtn = ttk.Button(root, text='保存任务', width=8, command=save)
Savebtn.place(x=360, y=1)

GetBtn = ttk.Button(root, text='获取任务', width=8, command=getTask)
GetBtn.place(x=440, y=1)


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
for i in range(9):
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

root.mainloop()
