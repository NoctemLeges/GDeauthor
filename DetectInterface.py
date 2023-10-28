import os
def execIW():
    cmd = "ip link show > interfaces.txt"
    os.system(cmd)
