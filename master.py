from listInterfaces import listInterfaces
from CheckMonitorMode import checkMonitor
from CheckPacketInjection import checkPacketInjection
from DeactivateMonitorMode import deactivateMonitorModeMain
mainInterface = "wlx1cbfce0d6a5b"
#print(listInterfaces())

#print(checkMonitor("wlx1cbfce0d6a5b"))

print(checkPacketInjection(mainInterface)) #Puts the interface in monitor mode. Undesirable

deactivateMonitorModeMain(mainInterface)

