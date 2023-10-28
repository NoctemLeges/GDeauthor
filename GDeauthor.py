from listInterfaces import listInterfaces
from CheckMonitorMode import checkMonitor
from ActivateMonitorMode import activateMonitorMode
from listAccessPoints import listAccessPoints
from DeactivateMonitorMode import deactivateMonitorMode
def main():
    print("Welcome to GDeauthor! Select a Network Interface that supports Monitor Mode and Packet Injection. Here are the list of available interfaces:")
    interfaces = listInterfaces()
    for interface in interfaces:
        print(interface)
    interface = input("[+]Enter Interface:")
    if interface not in interfaces:
        print("[-]Choose a proper Interface")
        exit()
    if(not checkMonitor(interface)):
       print("[-]Interface does not support monitor mode.")
       exit()
    if(checkMonitor(interface)==-1):
        deactivateMonitorMode(interface)
    print("[+]Activating Monitor Mode...\n\nHowever, before we do that")
    APlist = listAccessPoints(interface)
    print("[+]Choose your target:")
    for AP in APlist:
        print(AP)
    targetAP = input("[+]Target,please:")
    if targetAP not in APlist:
        print("Choose a proper target please!")
        deactivateMonitorMode(interface)
        exit()
    print("[+]Target Selected")
    print("Also,")
    activateMonitorMode(interface)
    print("[+]Monitor Mode Activated!Yay")

    
main()

