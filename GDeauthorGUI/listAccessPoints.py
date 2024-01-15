import os

def listAccessPoints():
    AP=set()
    cmd = f"nmcli -t device wifi list> APoutput.txt"
    os.system(cmd)
    with open("APoutput.txt","r") as f:
        lines = f.readlines()
    os.system("rm APoutput.txt")

    for line in lines:
        AP.add(line[25:].split(":")[0])
    AP.remove('')
    return AP
