# Plugins
import sys
import psutil
import time
import getpass
import os

# Colors
os.system('color') 

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'
BLUE = '\033[34m'




#---------------------------------
#Startup
#---------------------------------
print(GREEN + "Welcome! " + getpass.getuser() + RESET)
time.sleep(1)

print(RED + "Running general tests:\n-----------------------------" + RESET)
print(RED + "Current System: " + sys.platform + RESET)
print(RED + "Current CPU Usage: " + str(psutil.cpu_percent()) + "%" + RESET)
print(RED + "Current Python Version: " + sys.version + RESET)

time.sleep(1)

# Icons

MALWAREBYTES_ICON = """                     
       &&                  &&       
     &&&&&                &&&&&     
    &&&&&&&&            &&&&&&&&    
   &&&&&&&&&&&        &&&&&&&&&&&   
  &&&&&&&&&&&&&&    &&&&&&&&&&&&&&  
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  
 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& 
 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& 
 &&&&&&&&   &&&&&&&&&&&&   &&&&&&&& 
  &&&&&&     &&&&&&&&&&    &&&&&&&  
  &&&&&&       &&&&&&       &&&&&&  
   &&&&&         &&         &&&&&   
     &&&&                  &&&&     
      &&&&                &&&       
         &&              &&        
"""

PROTON_VPN_ICON = """
██╗   ██╗██████╗ ███╗   ██╗
██║   ██║██╔══██╗████╗  ██║
██║   ██║██████╔╝██╔██╗ ██║
╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║
 ╚████╔╝ ██║     ██║ ╚████║
  ╚═══╝  ╚═╝     ╚═╝  ╚═══╝
  """

TRANSLUCENT_TB_ICON = """
████████╗██████╗ 
╚══██╔══╝██╔══██╗
   ██║   ██████╔╝
   ██║   ██╔══██╗
   ██║   ██████╔╝
   ╚═╝   ╚═════╝ 
   """

# Initialization message
print(YELLOW + "-----------------\nSuccussfully loaded\n------------------" + "\n Welcome to recommended PC Apps! This program was created to show\n users, like you! " + getpass.getuser() + " The best apps for their PC!" + RESET)
time.sleep(2)

# Licensing and credits
print(YELLOW + "Information such as licensing and credits are located at: https://github.com/gooblesGH/Recommened-Apps\n-------------------" + RESET)
time.sleep(2)

# App 1: Malwarebytes
print(BLUE + "Application #1: Malwarebytes\n"+ "https://www.malwarebytes.com/" + MALWAREBYTES_ICON + "" + RESET)
time.sleep(1)

# App 2: Proton VPN
print(BLUE + "--------------------\n Application #2: Proton VPN\nhttps://protonvpn.com/\n" + PROTON_VPN_ICON + "" + RESET)

# App 3: Translucent TB
print(BLUE + "--------------------\n Application #3: Translucent TB\nhttps://github.com/TranslucentTB/TranslucentTB\n" + TRANSLUCENT_TB_ICON + "" + RESET)

# Closing message
input(RED + "------------\nPress Enter to Close..." + RESET)

