import importlib
import os
from datetime import datetime
import subprocess

# 检查命令行工具是否可用
def check_tool(tool_name):
    try:
        subprocess.run([tool_name, '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

# 检查文件是否存在，如果不存在则使用wget从指定URL下载
def check_file_with_wget(file_path, url):
    if not os.path.exists(file_path):
        now = datetime.now().strftime("%H:%M:%S")
        print(f" [LogCat|{now}] File \"{file_path}\" Does not exist, about to get from the Internet.")
        try:
            subprocess.run(['wget', '-O', file_path, url], check=True)
            now = datetime.now().strftime("%H:%M:%S")
            print(f" [LogCat|{now}] File \"{file_path}\" download complete.")
        except subprocess.CalledProcessError as e:
            now = datetime.now().strftime("%H:%M:%S")
            print(f" [ERROR|{now}] Occurs when a file is downloaded:{e}")
    else:
        pass

# List of modules to check and install
mods = ["requests", "tqdm", "flask"]

def isInstalled(module):
    try:
        importlib.import_module(module)
        return True
    except ModuleNotFoundError:
        return False

def install(module):
    # Try to install the module using pip
    shell = f"pip install {module}"
    os.system(shell)

def Install():
    # 获取当前时间
    now = datetime.now().strftime("%H:%M:%S")
    print(f" [LogCat|{now}] Self-test:Checking module installation status.")
    for mod in mods:
        if not isInstalled(mod):
            now = datetime.now().strftime("%H:%M:%S")
            print(f" [LogCat|{now}] Modules\"{mod}\"Not installed, please press Enter to install.")
            input("")
            install(mod)
        else:
            pass
    
    #检查各类文件的存在性，不存在到GitHub获取
    #这里检查几个必要的命令行工具和文件

    if not check_tool('git'):
        now = datetime.now().strftime("%H:%M:%S")
        print(f" [LogCat|{now}] alert:\"git\"Not installed, We will install it now.")
        os.system("pkg install git")
    else:
        pass
    
    if not check_tool('wget'):
        now = datetime.now().strftime("%H:%M:%S")
        print(f" [LogCat|{now}] alert:The \"wget\" does not exist, we will download it to continue with the installer.")
        os.system("pkg install wget")
    else:
        pass
    # 检查并下载 ./important.json 文件
    check_file_with_wget('./important.json', 'https://raw.githubusercontent.com/inaline/github.io/main/toolbox/important.json')
    
    now = datetime.now().strftime("%H:%M:%S")
    print(f" [LogCat|{now}] Self-test completed, welcome to continue.")