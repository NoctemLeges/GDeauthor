from DetectInterface import execIW
import os
def listInterfaces():
    execIW()
    f = open("interfaces.txt",'r')
    lines = f.readlines()
    f.close()
    os.system("rm interfaces.txt")
    interfaces = {}
    i = 0
    for line in lines:
        if ":" in line and "mode" in line:
            interfaces[i] = line.split(":")[1].split(":")[0].strip()
            i+=1
    return interfaces