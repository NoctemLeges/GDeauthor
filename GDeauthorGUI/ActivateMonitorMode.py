import os
def activateMonitorMode(interface):
    cmd = f"sudo airmon-ng start {interface} > /dev/null"
    try:
        os.system(cmd)
        return 1
    except:
        return 0
#activateMonitorMode("wlp1s0")