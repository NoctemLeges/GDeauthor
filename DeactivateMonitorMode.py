import os
def deactivateMonitorMode(interface):
    cmd = f"sudo airmon-ng stop {interface}mon > /dev/null"
    try:
        os.system(cmd)
        return 1
    except:
        return 0