from DetectInterface import execIW
import os
def listInterfaces():
    execIW()
    f = open("interfaces.txt",'r')
    lines = f.readlines()
    f.close()
    os.system("rm interfaces.txt")
    interfaces = []
    for line in lines:
        if ":" in line and "mode" in line:
            interfaces.append(line.split(":")[1].split(":")[0].strip())
    return interfaces