# python version = 3.10.0 64bit
from tkinter.messagebox import YES
from matplotlib.pyplot import autoscale
import wmi
import os
w = wmi.WMI()
global list
list=[]
def info():
    list.append("电脑信息:1")
    for BIOSs in w.Win32_ComputerSystem():
        list.append("电脑名称: %s" %BIOSs.Caption)
        list.append("使 用 者: %s" %BIOSs.UserName)
    for address in w.Win32_NetworkAdapterConfiguration(ServiceName = "e1dexpress"):
        list.append("IP地址: %s" % address.IPAddress[0])
        list.append("MAC地址: %s" % address.MACAddress)
    for BIOS in w.Win32_BIOS():
        list.append("使用日期: %s" %BIOS.Description)
        list.append("主板型号: %s" %BIOS.SerialNumber)
    for processor in w.Win32_Processor():
        list.append("CPU型号: %s" % processor.Name.strip())
    for memModule in w.Win32_PhysicalMemory():
        totalMemSize=int(memModule.Capacity)
        list.append("内存厂商: %s" %memModule.Manufacturer)
        list.append("内存型号: %s" %memModule.PartNumber)
        list.append("内存大小: %.2fGB" %(totalMemSize/1024**3))
    diski = 0
    for disk in w.Win32_DiskDrive(InterfaceType = "IDE"):
        diskSize=int(disk.size)
        diski +=1
        list.append("磁盘%d名称: %s" %(diski,disk.Caption))
        list.append("磁盘大小: %.2fGB" %(diskSize/1024**3))
    for xk in w.Win32_VideoController():
        list.append("显卡名称: %s" %xk.name)

def main():
    global path
    
    path= "D:/"
    for BIOSs in w.Win32_ComputerSystem():
        UserNames=BIOSs.Caption
    fileName=path+os.path.sep+'本电脑配置'+".txt"
    info()

    #判断文件夹（路径）是否存在
    if not os.path.exists(path):
        print("不存在")
        #创建文件夹（文件路径）
        os.makedirs(path)
        #写入文件信息
        
        with open(fileName,'w+') as f:
            for li in list:
                print(li)
                l=li+"\n"
                f.write(l)
    else:
        print("存在")
        with open(fileName,'w+') as f:
            for li in list:
                print(li)
                l=li+"\n"
                f.write(l)

main()

import tkinter
from tkinter import ttk
 
 
win = tkinter.Tk()
win.title("D:/本电脑配置.txt")    # #窗口标题
# win.geometry("600x500")   # #窗口位置500后面是字母x
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
  tree.insert("", index, text=each.split(':')[0], values=(each.split(':')[1],))    # #给第0行添加数据，索引值可重复

 
tree.pack(expand=YES)
win.mainloop()   # #窗口持久化