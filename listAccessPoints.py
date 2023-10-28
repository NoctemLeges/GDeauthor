import os

def listAccessPoints(interface):
    AP=[]
    cmd = f"sudo iwlist {interface} scanning > APoutput.txt"
    os.system(cmd)
    with open("APoutput.txt","r") as f:
        lines = f.readlines()
    os.system("rm APoutput.txt")

    for line in lines:
        if "ESSID:" in line:
            AP.append(line.split("ESSID:")[1].strip('"').rstrip('"\n'))
    return AP
