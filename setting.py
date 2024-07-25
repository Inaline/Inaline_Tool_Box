import os
import json
from public import *  # 假设这是您项目中的一些公共模块

# 用于存储设置项名称及其在 JSON 中的路径
li = [
    ("Default port for web server", "[web_server][default_port]"),
    ("Admin username for web server", "[web_server][admin_user]"),
    ("Admin password for web server", "[web_server][admin_pwd]")
]

def get_setting_value(settings, path):
    """ 根据路径获取设置值 """
    keys = path.split('][')
    keys[0] = keys[0][1:]
    keys[-1] = keys[-1][:-1]
    setting = settings
    for key in keys:
        setting = setting.get(key)
    return setting

def set_setting_value(settings, path, value):
    """ 根据路径设置设置值 """
    keys = path.split('][')
    keys[0] = keys[0][1:]
    keys[-1] = keys[-1][:-1]
    setting = settings
    for key in keys[:-1]:
        setting = setting.setdefault(key, {})
    setting[keys[-1]] = value

def display_settings(settings):
    """ 显示所有设置项 """
    for idx, (name, path) in enumerate(li):
        value = get_setting_value(settings, path)
        print(f"{idx}: {name} - Current Value: {value}")

def modify_setting(settings):
    """ 允许用户选择并修改设置项 """
    display_settings(settings)
    choice = input("Select the number of the setting you want to modify (or 'q' to quit): ")
    if choice.isdigit() and int(choice) < len(li):
        idx = int(choice)
        name, path = li[idx]
        current_value = get_setting_value(settings, path)
        new_value = input(f"Enter the new value for '{name}' (current: {current_value}): ")
        set_setting_value(settings, path, new_value)
        print(f"The value of '{name}' has been updated to '{new_value}'.")
    else:
        print("Invalid choice.")

def main():
    try:
        with open('./settings.json', 'r') as file:
            settings = json.load(file)
    except FileNotFoundError:
        print("The settings.json file was not found.")
        return
    except json.JSONDecodeError:
        print("The settings.json file contains invalid JSON.")
        return

    while True:
        modify_setting(settings)
        save_changes = input("Do you want to save these changes to the file? (y/n): ")
        if save_changes.lower() == 'y':
            with open('./settings.json', 'w') as file:
                json.dump(settings, file, indent=4)
            print("Changes saved successfully.")
            break
        else:
            print("No changes were saved.")
            break

if __name__ == '__main__':
    main()