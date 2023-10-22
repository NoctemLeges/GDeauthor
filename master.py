from listInterfaces import listInterfaces
from CheckMonitorMode import checkMonitor
from ActivateMonitorMode import activateMonitorMode
def main():
    print("Welcome to GDSDeauthor! Choose your next move:\n1.Display Available Interfaces\n2.Check Monitor Mode on an interface\n3.Activate Monitor Mode\n4.Exit")
    run = 1
    while(run):
        choice = int(input("Enter choice:"))
        match choice:
            case 1:
                interfaces = listInterfaces()
                print("Available Interfaces:")
                for interface in interfaces:
                    print(interface)
            case 2:
                interfaces = listInterfaces()
                interface = input("Enter the interface:")
                if interface not in interfaces:
                    print("Choose an available interface, please")
                else:
                    result = checkMonitor(interface)
                    if(result==0):
                        print("Interface does not support monitor mode!")
                    elif(result==1):
                        print("Interface supports monitor mode!")
            case 3:
                interfaces = listInterfaces()
                interface = input("Enter the interface:")
                if interface not in interfaces:
                    print("Choose an available interface, please")
                else:
                    result = checkMonitor(interface)
                    if(result==0):
                        print("Interface does not support monitor mode!")
                    elif(result==1):
                        print("Interface supports monitor mode!")
                        if(activateMonitorMode(interface)):
                            print(f"Monitor Mode activated on interface {interface}")    

            case 4:
                run = 0
            case _:
                print("Incorrect input, dummy")

main()

