##TODO: FIX THE INTERFACE NAMING ISSUE. HAD TO HARDCODE wlan0mon HERE
import os
import subprocess
import time
import signal
def returnClientMAC(APMAC):
    devnull = open('/dev/null','w')
    p = subprocess.Popen(["airodump-ng","-w","output","--output-format","csv","-d",f"{APMAC}","wlan0mon"],stdout = devnull,shell=False)
    time.sleep(30)
    p.send_signal(signal.SIGINT)
    f = open("output-01.csv","r")
    lines = f.readlines()
    f.close()
    os.system("sudo rm output-01.csv")
    if "Station MAC" in lines[-2]:
        return 0
    else:
        return lines[-2].split(",")[0]




    