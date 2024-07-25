from datetime import datetime
from public import *
import os

def remove_first_and_concatenate(lst):
    # 创建一个新的列表，排除第一个元素
    new_lst = lst[1:]
    # 将新列表转换为字符串
    return ' '.join(new_lst)

def RUN(command):
    if command == "exit":
        exit()
    elif command.startswith("cd"):
        os.chdir(command[3:])
    elif command.startswith("ina"):
        command = command[4:]
        s = command.split(" ")
        x = remove_first_and_concatenate(s)
        n = s[0]
        shell = f"python ./mods/{n}/main.py {x}"
        os.system(shell)
    else:
        os.system(command)


def Shell():
    now = datetime.now().strftime("%H:%M:%S")
    print(f" [LogCat|{now}] Starting Command_lines")
    
    print("┏━━("+ Colors.RED + "Message from ITB" + Colors.RESET + ")")
    print("┃Inaline Tool Box Command_lines Shell")
    print("┃ * 'ina help' to read the help document.")
    print("┗━━[Inaline@localhost]" + Colors.RESET)
    
    os_name = get_os_name()
    
    while True:
        path = os.getcwd()
        print("")
        print(Colors.BLUE + "┏━("+Colors.RED+"Inaline@"+os_name+Colors.BLUE+")-["+ Colors.RESET + path+Colors.BLUE+"]")
        RUN(input(Colors.BLUE + "┗━" + Colors.RED + "# " + Colors.RESET))
Shell()