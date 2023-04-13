import wmi
w = wmi.WMI()
for BIOS in w.Win32_BIOS():
    print(BIOS)

for BIOS in w.Win32_ComputerSystem():
    print(BIOS)
for BIOS in    w.Win32_Processor():
    print(BIOS)
for BaseBoard in    w.Win32_BaseBoard():
    print(BaseBoard)
for memModule in w.Win32_PhysicalMemory():
    print(memModule)