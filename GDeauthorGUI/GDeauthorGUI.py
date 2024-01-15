#Required Widgets: Frames,Open File Dialog Box,Sliders to specify time for which Deauth will occur etc, Dropdown Menus
from tkinter import *
import os
import time
from listInterfaces import listInterfaces
from listAccessPoints import listAccessPoints
from GetMACAddresses import getMACAddresses
from ActivateMonitorMode import activateMonitorMode
from CrackPassword import logPackets
from CheckMonitorMode import checkMonitor
from PIL import Image,ImageTk
#Preruntime stuff
os.system("sudo service NetworkManager restart && sudo airmon-ng stop wlan0mon")
time.sleep(5)
#Global Variables defined here
globalAPSet = listAccessPoints()
globalReqdInfo = dict()
#Callback Functions defined here
def listAccessPointsGUI():  #callback funtion for the Choose Interface Button
    APset = listAccessPoints()
    if(not checkMonitor(interface=interface.get())):
        resultLabel.config(text="[-]Interface Does not Support Monitor Mode. Choose Another.")
        return
    resultLabel.config(text="[+]Interface Supports Monitor Mode and Packet Injection. Proceed.")
    activateMonitorMode(interface.get())
    availableAP = "[+]Available APs:\n"
    for AP in APset:
        availableAP = availableAP+'\n'+AP
    availableAPLabelText.set(availableAP)
    APLabel.config(text=availableAPLabelText.get())
def getReqdInfo():
    MACs = getMACAddresses(target.get())
    if(MACs['Client MAC']==0):
        resultLabel.config(text="[-]The Access Point has no clients connected. Cannot Deauthenticate")
        return
    global globalReqdInfo
    globalReqdInfo = MACs
    macText = ""
    for key in MACs:
        macText = macText + "\n" + key + ":"+ str(MACs[key])
    infoLabel.config(text=macText)
def crack():
    try:
        resultLabel.config(text="Attacking...")
    except:
        print("")
    key = logPackets(globalReqdInfo['AP Channel'],globalReqdInfo['AP MAC'],globalReqdInfo['Client MAC'])
    keyLabel.config(text=key)
#----------------------------------------------------------------
root = Tk()
root.title("GDeauthor")
root.geometry("1920x1080")
root.resizable(False,False)
#Define the grid
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=20)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
interfaces = listInterfaces()
#Creating the Setup Options Frame
setupOptionsFrame = LabelFrame(root,text="Setup Options",width=960,height=1000,bg="white",fg="green")
setupOptionsFrame.grid(sticky="nsew",row=0,column=0,rowspan=2)
#Creating grid for setup options frame
setupOptionsFrame.columnconfigure(0,weight=1)
setupOptionsFrame.columnconfigure(1,weight=1)
setupOptionsFrame.rowconfigure(0,weight=1)
setupOptionsFrame.rowconfigure(1,weight=1)
setupOptionsFrame.rowconfigure(2,weight=1)
setupOptionsFrame.rowconfigure(3,weight=1)
setupOptionsFrame.rowconfigure(4,weight=5)
    #Creating the ASCII Art
gdeauthorImage = Image.open("AsciiArtImgSmall.png")
gdeauthorImagetest = ImageTk.PhotoImage(gdeauthorImage)
gdeauthorImageLabel = Label(setupOptionsFrame,image=gdeauthorImagetest,bg="black")
gdeauthorImageLabel.grid(sticky="nsew",row=0,column=0,columnspan=2)
    #Creating the Drop Down for the interface
interface = StringVar()
interface.set("Select an Interface")
drop = OptionMenu(setupOptionsFrame,interface,*interfaces)
drop.grid(row=1,column=0,padx=10,pady=10,sticky="e")
listAccessPointsbutton = Button(setupOptionsFrame,text="Select",command=listAccessPointsGUI)
listAccessPointsbutton.grid(row=1,column=1,padx=10,pady=10,sticky="w")
    #Create the Available Access Points Label
availableAPLabelText = StringVar()
availableAPLabelText.set("[+]Available APs:")
APLabel = Label(setupOptionsFrame,bg='black',text=availableAPLabelText.get(),fg="green",anchor="w",justify="left",font=("Ariel 15"))
APLabel.grid(row=2,column=0,sticky="nsew",pady=20,padx=10)
    #Creating the Options menu for the Target Access Point
target = StringVar()
target.set("Select the Target")
drop = OptionMenu(setupOptionsFrame,target,*globalAPSet)
drop.grid(row=3,column=0,sticky="ne",padx=10,pady=10)
getReqdInfobutton = Button(setupOptionsFrame,text="Select",command=getReqdInfo)
getReqdInfobutton.grid(row=3,column=1,padx=10,pady=10,sticky="nw")
    #Creating the RequiredInfo Label
reqdInfoLabelText=StringVar()
reqdInfoLabelText.set("Additional Info:")
infoLabel = Label(setupOptionsFrame,bg="black",text=reqdInfoLabelText.get(),fg="green",anchor="w",justify="left",font=("Ariel 20"))
infoLabel.grid(row=2,column=1,sticky="nsew",pady=20,padx=10)
    #GDSC Logo
gdsc = Image.open("gdsc logo-2 (1).png")
gdscTest = ImageTk.PhotoImage(gdsc)
gdscImageLabel = Label(setupOptionsFrame,image=gdscTest,bg="white",anchor="n")
gdscImageLabel.grid(sticky="n",row=4,column=0,columnspan=2)
#-------------------------------------------------------------------------------
#Creating the Result Console Frame
resultConsleFrame = LabelFrame(root,text="Result Console",width=960,height=540,bg="white",fg="green")
resultConsleFrame.grid(sticky="nsew",row=0,column=1)
resultConsleFrame.columnconfigure(0,weight=1)
resultConsleFrame.rowconfigure(0,weight=20)
resultConsleFrame.rowconfigure(1,weight=1)
consoleText = StringVar()
resultLabel = Label(resultConsleFrame,bg="black",fg="green",text=consoleText.get(),font=("Ariel 10 bold"))
resultLabel.grid(sticky = "nsew",column=0,row=0)
clearConsoleButton = Button(resultConsleFrame,text="clear Console")
clearConsoleButton.grid(row=1,column=0)
#--------------------------------------------------------------------------------
#Creating the Execute Frame
executeFrame = LabelFrame(root,text="Start Attack",width=960,height=540,bg="white",fg="green")
executeFrame.columnconfigure(0,weight=1)
executeFrame.columnconfigure(1,weight=1)
executeFrame.rowconfigure(0,weight=1)
executeFrame.grid(sticky="nsew",row=1,column=1)
executeButton = Button(executeFrame,text="Attack",command=crack)
executeButton.grid(column=1,row=0)
keyLabelText = StringVar()
keyLabelText.set("WiFi Password Will Appear Here:")
keyLabel = Label(executeFrame,bg="black",fg="green",text=keyLabelText.get(),font=('Ariel 15 bold'))
keyLabel.grid(sticky="ew",row=0,column=0)
#---------------------------------------------------------------------------------


root.mainloop()


