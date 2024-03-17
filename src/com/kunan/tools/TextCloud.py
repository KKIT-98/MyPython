import os
from datetime import datetime
from tkinter import filedialog, messagebox
import wordcloud
import jieba
import ttkbootstrap as ttk
from PIL import Image, ImageTk

window = ttk.Window(title='词云生成器', size=(800, 600))
# 设置窗口居中
window.place_window_center()
# 设置窗口禁止缩放
window.resizable(False, False)
# 图形界面设定标签用来存放生成的词云图
labelText1 = ttk.Label(window)
# 在指定位置放置标签
labelText1.place(x=5, y=50)
# 图形界面设定标签用来存放读取文件路径
labelText2 = ttk.Label(window)
# 在指定位置放置标签
labelText2.place(x=50, y=580)

# 文本标签3
labelText3 = ttk.Label(window)
# 在指定位置放置标签
labelText3.place(x=1, y=580)
label_text = ttk.StringVar()
global photo


# 打开文件操作
def openFile():
    filepath = filedialog.askopenfilename(title='请选择文件', filetypes=[('txt文本', '.txt'), ('所有文件', '.')])
    print('打开路径:' + filepath)
    labelText3.configure(text='打开文件')
    label_text.set(filepath)
    labelText2.configure(textvariable=label_text)
    CreateTextCloud(filepath)



# 初始化词云
def InitTextCloud():
    global photo
    # 创建词云对象，设置云图的宽、高、字体、背景颜色等参数
    wc = wordcloud.WordCloud(width=790, height=530, background_color='white', font_path='msyh.ttc', scale=1)
    text = '欢迎\n使用\n词云\n生成器\nWelcome\nWorldCloud'

    # 调用jieba的lcut()方法对原始文本进行中文分词得到string
    textlist = jieba.lcut(text)
    string = " ".join(textlist)
    # 调用词云对象的generate方法，将文本传入
    wc.generate(string)
    # 将生成的词云保存为output_textCloud图片文件且保存到当前文件夹中
    wc.to_file("./welcome.jpg")
    img = Image.open("./welcome.jpg")
    photo = ImageTk.PhotoImage(img)

    labelText1.config(image=photo)
    print("放置成功")


InitTextCloud()


# 创建词云
def CreateTextCloud(filepath):
    global photo
    print("CreateTextCloud")
    # 创建词云对象，设置云图的宽、高、字体、背景颜色等参数
    wc = wordcloud.WordCloud(width=790, height=530, background_color='white', font_path='msyh.ttc', scale=1)
    # 从外部txt文件中读取文本存入变量
    if label_text.get() == '':
        messagebox.showinfo("提示", "请先选择文件")
    else:

        try:
            file = open(label_text.get(), encoding='utf-8')
            text = file.read()
        except:
            file = open(label_text.get())
            text = file.read()

        # 调用jieba的lcut()方法对原始文本进行中文分词得到string
        textlist = jieba.lcut(text)
        string = " ".join(textlist)
        # 调用词云对象的generate方法，将文本传入
        wc.generate(string)
        # 将生成的词云保存为output_textCloud图片文件且保存到当前文件夹中
        wc.to_file('output_textCloud.png')
        img = Image.open('output_textCloud.png')
        photo = ImageTk.PhotoImage(img)
        labelText1.configure(image=photo)

# 刷新词云
def ReloadTextCloud():
    global photo
    print("CreateTextCloud")
    # 创建词云对象，设置云图的宽、高、字体、背景颜色等参数
    wc = wordcloud.WordCloud(width=790, height=530, background_color='white', font_path='msyh.ttc', scale=1)
    # 从外部txt文件中读取文本存入变量
    if label_text.get() == '':
        messagebox.showinfo("提示", "请先选择文件")
    else:

        try:
            file = open(label_text.get(), encoding='utf-8')
            text = file.read()
        except:
            file = open(label_text.get())
            text = file.read()

        # 调用jieba的lcut()方法对原始文本进行中文分词得到string
        textlist = jieba.lcut(text)
        string = " ".join(textlist)
        # 调用词云对象的generate方法，将文本传入
        wc.generate(string)
        # 将生成的词云保存为output_textCloud图片文件且保存到当前文件夹中
        wc.to_file('output_textCloud.png')
        img = Image.open('output_textCloud.png')
        photo = ImageTk.PhotoImage(img)
        labelText1.configure(image=photo)


def SaveTextCloud():
    print("保存词云")
    FileNewPath = filedialog.asksaveasfilename(
        initialfile='词云_' + datetime.now().strftime("%Y%m%d%H%M"),
        filetypes=[("png图像", ".png")],
        defaultextension='.png'
    )
    if FileNewPath == '':
        print("保存取消")
    else:
        img = Image.open("./output_textCloud.png")
        print("保存路径:" + FileNewPath)
        FileNewName.set(FileNewPath)
        img.save(str(FileNewName.get()))


FileNewName = ttk.StringVar()


# 全屏按钮
def FullScreen():
    print("全屏展示")
    global photo

    # 创建词云对象，设置云图的宽、高、字体、背景颜色等参数
    wc = wordcloud.WordCloud(width=950, height=515, background_color='white', font_path='msyh.ttc', scale=2)

    # 从外部txt文件中读取文本存入变量
    if label_text.get() == '':
        messagebox.showinfo("提示", "请先选择文件")
    else:

        try:
            file = open(label_text.get(), encoding='utf-8')
            text = file.read()
        except:
            file = open(label_text.get())
            text = file.read()

        # 调用jieba的lcut()方法对原始文本进行中文分词得到string
        textlist = jieba.lcut(text)
        string = " ".join(textlist)
        # 调用词云对象的generate方法，将文本传入
        wc.generate(string)
        labelText3.configure(text='')
        labelText2.pack()
        labelText2.pack_forget()
        # 将生成的词云保存为output_textCloud图片文件且保存到当前文件夹中
        wc.to_file('output_textCloud.png')
        img = Image.open('output_textCloud.png')
        photo = ImageTk.PhotoImage(img)
        labelText1.configure(image=photo)
        window.attributes("-fullscreen", True)


def FullScreen2():
    print("全屏展示")
    global photo
    try:
        img = Image.open('output_textCloud.png')
        new_size = (1900, 1030)
        result_img = img.resize(new_size, resample=Image.BICUBIC)
        result_img.save('new_output_textCloud.png')
        photo = ImageTk.PhotoImage(Image.open('new_output_textCloud.png'))
        labelText1.configure(image=photo)
        # 打开全屏隐藏其他按钮
        OpenFileBtn.pack()
        OpenFileBtn.pack_forget()
        CreateTexCloudBtn.pack()
        CreateTexCloudBtn.pack_forget()
        SaveTexCloud.pack()
        SaveTexCloud.pack_forget()
        FullScreenBtn.pack()
        FullScreenBtn.pack_forget()
        OffFullScreenBtn.place(x=1850, y=0)
        labelText3.configure(text='')
        labelText2.pack()
        labelText2.pack_forget()
        window.attributes("-fullscreen", True)
    except:
        messagebox.showinfo("提示", "请先生成词云")


def OffFullScreen():
    print("退出全屏")
    global photo
    img = Image.open('output_textCloud.png')
    photo = ImageTk.PhotoImage(img)
    labelText1.configure(image=photo)
    # 打开文件按钮
    OpenFileBtn.place(x=0, y=0)
    # 生成词云按钮
    CreateTexCloudBtn.place(x=100, y=0)
    # 保存词云按钮
    SaveTexCloud.place(x=200, y=0)
    # 全屏按钮
    FullScreenBtn.place(x=300, y=0)
    # 退出全屏按钮
    OffFullScreenBtn.pack()
    OffFullScreenBtn.pack_forget()
    labelText3.configure(text='打开文件')
    labelText2.place(x=50, y=580)

    window.attributes("-fullscreen", False)


# 关闭窗口时删除没有保存的词云
def on_closing():
    # 处理关闭窗口事件的代码
    print("窗口关闭")
    try:
        os.remove('./output_textCloud.png')
        os.remove('./new_output_textCloud.png')
        window.destroy()
    except FileNotFoundError:
        window.destroy()



# 打开文件按钮
OpenFileBtn = ttk.Button(window, text='打开文件', width=8, command=openFile)
OpenFileBtn.place(x=0, y=0)

# 生成词云按钮
CreateTexCloudBtn = ttk.Button(window, text='刷新词云', width=8, command=ReloadTextCloud)
CreateTexCloudBtn.place(x=100, y=0)

# 保存词云按钮
SaveTexCloud = ttk.Button(window, text='保存图片', width=8, command=SaveTextCloud)
SaveTexCloud.place(x=200, y=0)

# 全屏按钮
FullScreenBtn = ttk.Button(window, text='全屏展示', width=8, command=FullScreen2)
FullScreenBtn.place(x=300, y=0)

# 退出全屏按钮
OffFullScreenBtn = ttk.Button(window, text='退出全屏', width=8, command=OffFullScreen)
OffFullScreenBtn.pack()
OffFullScreenBtn.pack_forget()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
