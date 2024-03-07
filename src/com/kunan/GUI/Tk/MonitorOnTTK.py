import threading
import time

import psutil
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(
    size=(400, 400)
)
root.place_window_center()
root.attributes('-topmost', True)
meter1 = ttk.Meter(
    master=root,
    bootstyle='success',  # 仪表主题
    # wedgesize=-1, #
    metertype='semi',  # 设置仪表盘的样式semi为半圆型
    amounttotal=100,  # 仪表的最大值
    amountused=0,  # 仪表的当前值
    metersize=180,  # 仪表盘的大小
    # showtext=True, # 是否可以在仪表盘上显示左中右文本标签
    # interactive=True, # 是否可以手动调节数字大小
    # textleft='左边',  # 插入中心文本左侧字符
    # textright='右边',
    textfont="-size 16",  # 中间数字大小
    subtext="CPU使用率%",  # 中间文本
    subtextstyle='success',  # 显示值主题
    subtextfont="-size 16"  # 显示值的字体
)

# meter1.pack(side=ttk.LEFT, padx=5)
meter1.place(x=1, y=50)
labelText1 = ttk.Label(root, bootstyle='success', font=('黑体', 16), text='下载速率:')
labelText1.place(x=1, y=230)

labelText2 = ttk.Label(root, bootstyle='success', font=('黑体', 16))
labelText2.place(x=100, y=230)


def _():
    meter = ttk.Meter(
        metersize=180,
        # padding=50,
        amountused=0,
        metertype='semi',
        subtext='内存使用率%',
        subtextstyle=INFO,
        interactive=False,
        bootstyle=INFO,
        subtextfont='-size 16'
    )
    # meter.pack(side=ttk.LEFT, padx=5)
    meter.place(x=200, y=50)
    while True:
        if getCpuUse() > 60:
            meter1.configure(amountused=getCpuUse(), bootstyle=DANGER, subtextstyle=DANGER)
        else:
            meter.configure(amountused=int(getMemUse() * 100))
            meter1.configure(amountused=getCpuUse(), bootstyle=SUCCESS, subtextstyle=SUCCESS)
        labelText2.configure(text=getNet())


def getNet():
    recv_before = psutil.net_io_counters().bytes_recv
    time.sleep(1)
    recv_now = psutil.net_io_counters().bytes_recv
    recv = recv_now - recv_before
    return getNetHigh(recv)


def getNetHigh(net_bytes: int):
    if net_bytes < 1000:
        if net_bytes < 100:
            return " %sB/S" % str(net_bytes)
        else:
            return "%sB/S" % str(net_bytes)

    elif net_bytes >> 10 < 1000:
        if net_bytes // 1024 < 100:
            return "%.1fKB/S" % (net_bytes / 1024)
        else:
            return "%sKB/S" % (net_bytes // 1024)
    elif net_bytes >> 20 < 1000:
        if net_bytes // 1024 ** 2 < 100:
            return "%.1fMB/S" % (net_bytes / 1024 ** 2)
        else:
            return "%sMB/S" % (net_bytes // 1024 ** 2)
    elif net_bytes >> 30 < 1024:
        if net_bytes // 1024 ** 3 < 100:
            return "%.1fGB/S" % (net_bytes / 1024 ** 3)
        else:
            return "%sGB/S" % (net_bytes // 1024 ** 3)
    else:
        return "xx.xB/S"


def getMemUse():
    free = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2))
    total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2))
    return int(psutil.virtual_memory().total - psutil.virtual_memory().free) / float(psutil.virtual_memory().total)


def getCpuUse():
    return psutil.cpu_percent(interval=1)


t = threading.Thread(target=_)
t.setDaemon(True)
t.start()
root.mainloop()
