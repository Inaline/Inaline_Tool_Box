import os
from install import *
from public import *


os.system("clear")

msg = """
 ______                    ___                                 
/\__  _\                  /\_ \    __                      TM  
\/_/\ \/     ___      __  \//\ \  /\_\    ___      __          
   \ \ \   /' _ `\  /'__`\  \ \ \ \/\ \ /' _ `\  /'__`\        
    \_\ \__/\ \/\ \/\ \L\.\_ \_\ \_\ \ \/\ \/\ \/\  __/        
    /\_____\ \_\ \_\ \__/.\_\/\____\\ \_\ \_\ \_\ \____\       
    \/_____/\/_/\/_/\/__/\/_/\/____/ \/_/\/_/\/_/\/____/       
  ______            __   ____                                  
 /_  __/___  ____  / /  / __ )____  _  __                      
  / / / __ \/ __ \/ /  / __  / __ \| |/_/                      
 / / / /_/ / /_/ / /  / /_/ / /_/ />  <                        
/_/  \____/\____/_/  /_____/\____/_/|_|   Version 1.0.0-bate   

Welcome to use the Inaline Tool Box.
 - Communities: http://forum.inaline.net/
 - IT.Blog    : http://blog.inaline.net/
 - ITB Website: http://tool.inaline.net/
"""
print(msg)

Install()

print("/" + "-" * (get_terminal_width()-2) + "\\")
print_list_item("IP addr",get_local_ip())
print_list_item("System",get_os_name())
print_list_item("machine",get_os_machine())
print_list_item("Python",get_python_version())
print("\\" + "-" * (get_terminal_width()-2) + "/")

print("""
 [1] Start Inaline Tool Box
 [2] Only Start Command_Lines
 [3] Only Start Web Server
 [4] Only Start options
 ----------------------------
 [5] Show All Tool
 [6] Install Tool
 ============================
 [s] Setting
 [e] Exit
""")
option = input("Please select:")

if option == "1":
    os.system("python start.py type=0")
elif option == "2":
    os.system("python start.py type=1")
elif option == "3":
    os.system("python start.py type=2")
elif option == "4":
    os.system("python start.py type=3")
elif option == "5":
    os.system("python show_tools.py")
elif option == "6":
    os.system("python install_tool.py")
elif option == "s":
    os.system("python setting.py")
elif option == "e":
    exit()
else:
    print("Option does not exist, please select again")