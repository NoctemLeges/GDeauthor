import os
def activateMonitorMode(interface):
    cmd = f"sudo airmon-ng start {interface}"
    try:
        os.system(cmd)
        os.system("clear")
        return 1
    except:
        return 0