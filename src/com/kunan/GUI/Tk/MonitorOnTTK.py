import threading
import time

import psutil
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
root = ttk.Window(
size=(350, 450)
)
# root.place_window_center()
# root.attributes('-topmost', True)
meter1 = ttk.Meter(
    master=root,
    bootstyle='success',
    # wedgesize=-1,
    metertype='semi',
    amounttotal=100,
    amountused=0,
    metersize=120,
    #showtext=True,
    #interactive=True,
   # textleft='左边',
   # textright='右边',
    textfont="-size 8",
    subtext="CPU使用率%",
    subtextstyle='success',
    subtextfont="-size 8"
    )
meter1.place(x=1, y=20)

labelText1 = ttk.Label(root, bootstyle='success', font=('黑体', 16), text='下载速率:')
labelText1.place(x=1, y=230)

def _():
    return 1

def getNet():
    recv_before = psutil.net_io_counters().bytes_recv
    time.sleep(1)
    recv_now = psutil.net_io_counters().bytes_recv
    recv = recv_now - recv_before
    return  getNetHigh(recv)


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

t = threading.Thread()
t.setDaemon(True)
t.start()
root.mainloop()
