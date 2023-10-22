import os
def execIW():
    cmd = "ip link show | tee interfaces.txt"
    os.system(cmd)
    os.system("clear")
