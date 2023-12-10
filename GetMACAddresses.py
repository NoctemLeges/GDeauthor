import os
from GetClientPresence import returnClientMAC
def getMACAddresses(AP):
    MACs  = {}
    cmd = "nmcli -f BSSID,SSID device wifi list > nmcliOutput.txt"
    os.system(cmd)
    f = open("nmcliOutput.txt","r")
    lines = f.readlines()
    f.close()
    os.system("rm nmcliOutput.txt")
    for line in lines:
        if AP in line:
            MACs["AP MAC"] = line.split(" ")[0]
    MACs["Client MAC"] = returnClientMAC(MACs["AP MAC"])
    return MACs
