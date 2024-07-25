import os
import json
from datetime import datetime
from public import *

def read_init_json(mods_directory):
    # 确保目录以斜杠结尾
    if not mods_directory.endswith(os.sep):
        mods_directory += os.sep

    # 存储结果的字典
    results = {}

    # 遍历mods目录下的每个子目录
    for mod_dir in os.listdir(mods_directory):
        mod_path = os.path.join(mods_directory, mod_dir)
        
        # 检查是否为目录
        if os.path.isdir(mod_path):
            init_json_path = os.path.join(mod_path, 'init.json')
            
            # 检查init.json是否存在
            if os.path.isfile(init_json_path):
                with open(init_json_path, 'r', encoding='utf-8') as file:
                    try:
                        data = json.load(file)
                        results[mod_dir] = data
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON in {init_json_path}")
    
    return results

def Options():
    now = datetime.now().strftime("%H:%M:%S")
    print(f" [LogCat|{now}] Starting Options")
    print("""
 [s] Open SSH server
 [c] Open Command_line mode
 --- Tool Mod List start---""")
    i = 0
    results = read_init_json("./mods")
    names = []
    for mod_dir, data in results.items():
        name = data.get('name', 'Unknown Name')
        names.append(name)
        print(" [" + str(i) + "]", name)
        i += 1
    print(" --- Tool Mod List end  ---")
    print(" [b] Back to superior Level.")
    
    option = input("Please select:")
    if option == "c":
        os.system("python shell.py")
    else:
        name = names[int(option)]
        shell = f"python ./mods/{name}/main.py"
        os.system(shell)