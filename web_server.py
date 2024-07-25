import subprocess
import os
import json
from flask import Flask
from datetime import datetime
from public import *

def start_web_server(ip, port):

    with open('./settings.json', 'r') as file:
        info = json.load(file)
    admin_user = info["web_server"]["admin_user"]
    admin_pwd = info["web_server"]["admin_pwd"]
    
    now = datetime.now().strftime("%H:%M:%S")
    print(f" [LogCat|{now}] Starting the Web_Server.")
    
    # 使用 nohup 在后台启动 Flask 服务器
    # 设置 FLASK_APP 环境变量来指向 Flask 应用文件
    command = f'nohup python -m flask run --host={ip} --port={port} > server.log 2>&1 &'
    # 设置 FLASK_APP 和 FLASK_ENV 环境变量
    env = os.environ.copy()
    env['FLASK_APP'] = 'app.py'  # 指定 Flask 应用文件
    env['FLASK_ENV'] = 'production'  # 设置为生产环境
    
    # 使用 subprocess.Popen 来在后台启动 Flask 服务器
    subprocess.Popen(command, shell=True, env=env)
    
    now = datetime.now().strftime("%H:%M:%S")
    print(f" [LogCat|{now}] Web_Server started successfully.")
    
    now = datetime.now().strftime("%H:%M:%S")
    print(f" [-Info-|{now}] Web_Server on IP:{ip} port:{port} \n ----------------- URL: http://{ip}:{port}")
    
    now = datetime.now().strftime("%H:%M:%S")
    print(f" [LogCat|{now}] Log information is output in the \"./server. Log.\"")
    
    url = "http://"+get_local_ip()+":"+port
    print("/" + "-" * (get_terminal_width()-2) + "\\")
    print_list_item("IP addr",get_local_ip())
    print_list_item("Port",port)
    print_list_item("URL",url)
    print_list_item("admin_user",admin_user)
    print_list_item("admin_pwd",admin_pwd)
    print_list_item("log_path","./server.log")
    print("\\" + "-" * (get_terminal_width()-2) + "/")