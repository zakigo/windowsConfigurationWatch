# python version = 3.10.0 64bit
from tkinter.messagebox import YES
import tkinter.messagebox
import wmi
import os
import tkinter as tk
from tkinter import ttk
w = wmi.WMI()
global list
list=[]

def info():
    # list.append("电脑信息:=1")
    for BIOSs in w.Win32_ComputerSystem():
        list.append("电脑名称:= %s" %BIOSs.Caption)
        list.append("使 用 者:= %s" %BIOSs.UserName)
    for address in w.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        list.append("网卡名称:= %s" % address.Description)
        list.append("IPv4地址:= %s" % address.IPAddress[0])
        list.append("IPv6地址:= %s" % address.IPAddress[1])
        list.append("MAC地址:= %s" % address.MACAddress)
    for BIOS in w.Win32_BIOS():
        list.append("BIOS:= %s" %BIOS.Description)
    for BaseBoard in    w.Win32_BaseBoard():
        list.append("主板制造商:= %s" %BaseBoard.Manufacturer)
        list.append("主板型号:= %s" %BaseBoard.Product)
    for processor in w.Win32_Processor():
        list.append("CPU型号:= %s" % processor.Name.strip())
    for count,memModule in enumerate(w.Win32_PhysicalMemory()):
        totalMemSize=int(memModule.Capacity)
        list.append("内存%d:= %s - %.2fGB - %sMhz" %(count+1,memModule.Manufacturer,totalMemSize/1024**3,memModule.Speed))
        # list.append("内存型号:= %s" %memModule.PartNumber)
        # list.append("内存大小:= %.2fGB" %(totalMemSize/1024**3))
        # list.append("内存速度:= %sMhz" %memModule.Speed)


    for count,disk in enumerate(w.Win32_DiskDrive(InterfaceType = "IDE")):
        diskSize=int(disk.size)
        list.append("磁盘%d:= %s" %(count,disk.Caption))
        list.append("磁盘%d大小:= %.2fGB" %(count, diskSize/1024**3))
    for count,xk in enumerate(w.Win32_VideoController()):
        list.append("显卡%d:= %s" %(count+1,xk.name))

def savefile(path):
    from datetime import datetime
    date = datetime.today()
    date2 =date.strftime("%Y%m%d_%H%M%S")
    print(date.strftime("%Y%m%d_%H%M%S"))
    fileName=path+os.path.sep+'本电脑配置'+date2+".txt"
    #判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        #创建文件夹（文件路径）
        try:
            os.makedirs(path)
        except:
            return False
        #写入文件信息
        
        with open(fileName,'w+') as f:
            for li in list:
                print(li)
                l=li+"\n"
                f.write(l)
    else:
        # print("存在")
        with open(fileName,'w+') as f:
            for li in list:
                print(li)
                l=li+"\n"
                f.write(l)
    return True
import time
win = tk.Tk()
win.title("撸大士")    # #窗口标题
status  = tk.StringVar()
def main():

    global path
    # 默认D盘保存，网吧电脑没有D盘则保存C盘
    path= "D:/"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames=BIOSs.Caption
    print(UserNames)

    if(savefile(path)):
        print("保存D盘成功")
        # time.sleep(10)
        status.set("Status: 保存D盘成功!'")
    else:
        path= "C:/"
        savefile(path)
        print("保存C盘成功")
        # time.sleep(10)
        # result = tkinter.messagebox.askokcancel(title = '标题~',message='保存C盘成功')


info()


main()
 

# win.geometry("600x800")   # #窗口位置500后面是字母x
'''
表格
'''
tree = ttk.Treeview(win,height=20)      # #创建表格对象
tree["columns"] = ("姓名", "年龄")     # #定义列
tree.column("姓名", width=300)          # #设置列
tree.column("年龄", width=300)

tree.heading("姓名", text="")        # #设置显示的表头名
tree.heading("年龄", text="")

for index,each in enumerate(list):
  # print(each.split(':')[0])
  # print(each.split(':')[1])
  tree.insert("", index, text=each.split(':=')[0], values=(each.split(':=')[1],))    # #给第0行添加数据，索引值可重复

# status.set("good")

statusbar = tk.Label(win, textvariable=status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

# statusbar = tkinter.Label(win, text="on the way…", bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
# statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
tree.pack(expand=YES)

win.mainloop()   # #窗口持久化
