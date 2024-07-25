from public import *
import os
import json
from datetime import datetime

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
print(" - Installed Tool Mod List")
print("/" + "-" * (get_terminal_width()-2) + "\\")
print_list_item("ID","Name")
i = 0
results = read_init_json("./mods")
for mod_dir, data in results.items():
    name = data.get('name', 'Unknown Name')
    print_list_item(str(i), name)
    i += 1
print("\\" + "-" * (get_terminal_width()-2) + "/")
id = input("Please enter a serial number for operation:")
print("""
 [1] View details
 [2] Delete mod
""")
option = input("Please select:")