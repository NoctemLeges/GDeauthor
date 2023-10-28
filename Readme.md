## How it works
- The entry point is master.py, which displays all the possible options.
- First option is to display all the available interfaces. In order to do this, master.py calls **listInterfaces** function which in turn calls DetectInterface.py with its execIW() function. The execIW() function runs ``ip link show`` to list all the available interfaces and stores the output in an ephemeral file **interfaces.txt**. **listInterfaces()** then does some string manipulation to carve out the interface names and deletes the **interfaces.txt** file. It also returns the interfaces list to master.py which is then displayed.


## Errors to fix
1. If interface is already in monitor mode, do not return "Interface does not support monitor mode". Instead deactivate it, then resume normal operation