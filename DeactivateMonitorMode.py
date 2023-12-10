import os
def deactivateMonitorModeAir(interface):
    cmd = f"sudo airmon-ng stop {interface}mon > /dev/null"
    try:
        os.system(cmd)
        return 1
    except:
        return 0

def deactivateMonitorModeMain(interface):
    cmd1 = f"sudo ifconfig {interface} down"
    cmd2 = f"sudo iwconfig {interface} mode managed"
    cmd3 = f"sudo ifconfig {interface} up"
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)