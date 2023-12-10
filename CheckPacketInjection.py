import os

def checkPacketInjection(interface):
    cmd = f"sudo aireplay-ng -9 {interface} > packetInjectionOutput.txt "
    os.system(cmd)
    f  = open("packetInjectionOutput.txt","r")
    lines = f.readlines()
    f.close()
    os.system("rm packetInjectionOutput.txt")
    for line in lines:
        if "Injection is working" in line:
            return 1
    return 0


