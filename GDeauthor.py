from listInterfaces import listInterfaces
from CheckMonitorMode import checkMonitor
from CheckPacketInjection import checkPacketInjection
from ActivateMonitorMode import activateMonitorMode
from listAccessPoints import listAccessPoints
from DeactivateMonitorMode import deactivateMonitorMode
from GetMACAddresses import getMACAddresses
def main():
    print("Welcome to GDeauthor! Select a Network Interface that supports Monitor Mode and Packet Injection. Here are the list of available interfaces:")
    interfaces = listInterfaces()
    for key in interfaces:
        print(str(key)+">" +interfaces[key])
    interfaceNum = int(input("[+]Enter Interface Num:"))
    if interfaceNum not in list(interfaces.keys()):
        print("[-]Choose a proper Interface")
        exit()
    else:
        interface = interfaces[interfaceNum]
    if(not checkMonitor(interface)):
       print("[-]Interface does not support monitor mode.")
       exit()
    if(checkMonitor(interface)==-1):
        deactivateMonitorMode(interface)
    if(not checkPacketInjection(interface)):
        print("Interface does not support packet injection")
        exit()
    print("[+]Activating Monitor Mode...\n\nHowever, before we do that")
    APlist = listAccessPoints()
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
    MACs = getMACAddresses(targetAP)
    if MACs["Client MAC"] == 0:
        print("No clients are connected to the AP. Cannot perform Deauthentication")
        exit()
    print("MAC Address of AP: ",MACs["AP MAC"])
    print("MAC Address of Client: ",MACs["Client MAC"])


    
main()

