import os
import sys
import json
from public import *
from web_server import *
from datetime import datetime
from options import *

with open('./settings.json', 'r') as file:
    info = json.load(file)
port = info["web_server"]["default_port"]

now = datetime.now().strftime("%H:%M:%S")
print(f" [LogCat|{now}] Inaline Tool Box Starting.")

# sys.argv[0] 是脚本名称
args = sys.argv[1:]  # 获取除脚本名称外的所有参数
if len(args) > 0:
    if args[0] == "type=0":
        start_web_server(get_local_ip(),port)
        Options()
    elif args[0] == "type=1":
        os.system("python shell.py")
    elif args[0] == "type=2":
        start_web_server(get_local_ip(),port)
    elif args[0] == "type=3":
        Options()
    else:
        now = datetime.now().strftime("%H:%M:%S")
        print(f" [LogCat|{now}] {args}")
else:
    now = datetime.now().strftime("%H:%M:%S")
    print(f" [ERROR|{now}] No parameters passed in, aborted.")