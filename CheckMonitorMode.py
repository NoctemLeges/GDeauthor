import os
def checkMonitor(interface):
    cmd1 = f"sudo airmon-ng start {interface} > monitorOutput.txt"
    cmd2 = f"sudo airmon-ng stop wlan0mon > /dev/null"
    os.system(cmd1)
    os.system(cmd2)
    #os.system("clear")
    f = open("monitorOutput.txt",'r')
    lines = f.readlines()
    os.system("rm monitorOutput.txt")
    for line in lines:
        if "monitor mode vif enabled" in line:
            return 1
        elif "monitor mode already enabled" in line:
            return -1
    return 0
#print(checkMonitor("wlp1s0"))
