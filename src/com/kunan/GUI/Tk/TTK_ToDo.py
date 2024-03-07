import ttkbootstrap as ttk
from ttkbootstrap import Window, WARNING, INFO, SUCCESS

root = Window(
    size=(600, 400),
    resizable=(False, False)
)

lab1 = ttk.Label(root, text="1.", font=('宋体', 14))
lab1.place(x=0, y=55)
xx = 50
tex_x = 55

# 文本框
text = ttk.Entry(root, width=55, font=('宋体', 12))
text.place(x=25, y=50)
# 组合框
cbo = ttk.Combobox(master=root, bootstyle=WARNING, font=('宋体', 12, 'bold'), values=['进行中', '已完成', '未开始'],
                   width=6)
cbo.current(2)
cbo.place(x=480, y=50)




def ensure1(event):
    if cbo.get() == '进行中':
        cbo.configure(bootstyle=INFO)
        text.configure(bootstyle=INFO)
    elif cbo.get() == '已完成':
        cbo.configure(bootstyle=SUCCESS)
        text.configure(bootstyle=SUCCESS)
    elif cbo.get() == '未开始':
        cbo.configure(bootstyle=WARNING)
        text.configure(bootstyle=WARNING)


cbo.bind('<<ComboboxSelected>>', ensure1)


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
for i in range(8):
    xx = xx + 38
    tex_x = tex_x + 38
    num = 2 + i
    tex = 't_' + str(i)
    ent = 'ent_' + str(i)
    cob1 = 'cob_' + str(i)

    tex = ttk.Label(root, text=str(num) + '.', font=('宋体', 14))
    tex.place(x=0, y=tex_x)

    ent = ttk.Entry(root, width=55, font=('宋体', 12))
    ent.place(x=25, y=xx)

    cob1 = ttk.Combobox(master=root, bootstyle=WARNING, font=('宋体', 12, 'bold'),
                        values=['进行中', '已完成', '未开始'], width=6)
    cob1.current(2)
    cob1.place(x=480, y=xx)
    cob1.bind('<<ComboboxSelected>>', ensure(cob1, ent))
# 点击置顶窗口按钮触发事件
def TopWindow():
    root.attributes('-topmost', True)


# 点击取消置顶按钮触发事件
def OffWindow():
    root.attributes('-topmost', False)


# 按钮
# 置顶窗口按钮
ChangeBtn = ttk.Button(root, text='置顶窗口', width=8, command=TopWindow)
ChangeBtn.place(x=1, y=1)

# 取消置顶按钮
ChangeBtn = ttk.Button(root, text='取消置顶', width=8, command=OffWindow)
ChangeBtn.place(x=85, y=1)




root.mainloop()
