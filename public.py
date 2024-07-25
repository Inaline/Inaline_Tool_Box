import os
import socket
import platform
import json


import json


import json


def get_nth_key_value_pair(json_string, n):
    """
    获取 JSON 字符串中第 n 个键值对。
    如果值是嵌套的 JSON 对象，则返回所有子键和它们对应的值的列表。
    
    :param json_string: JSON 格式的字符串
    :param n: 索引位置，从 1 开始计数
    :return: 第 n 个键值对的列表 [(key, value), ...]，如果索引超出范围则返回 None
    """
    try:
        # 将 JSON 字符串转换为字典
        json_dict = json_string
        
        # 将字典转换为列表，其中每个元素都是一个键值对的元组
        items = list(json_dict.items())
        
        # 获取第 n 个键值对
        n_th_key, n_th_value = items[n-1]  # 注意索引是从 0 开始的，所以 n-1
        
        # 如果值是一个嵌套的 JSON 对象，则展开所有子键和它们对应的值
        if isinstance(n_th_value, dict):
            key_value_list = []
            for sub_key, sub_value in n_th_value.items():
                key_value_list.append((sub_key, sub_value))
            return [(n_th_key, n_th_value)] + key_value_list
        else:
            return [(n_th_key, n_th_value)]
    except (json.JSONDecodeError, IndexError):
        return None


def calculate_length(s):
    length = 0
    for char in s:
        if '\u4e00' <= char <= '\u9fff':  # 汉字范围
            length += 2
        elif ord(char) > 127:  # 全角字符通常位于 ASCII 128 以上
            length += 2
        else:
            length += 1
    return length

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        # 如果无法获取终端尺寸，则返回一个默认值或 None
        return None

def get_terminal_height():
    try:
        return os.get_terminal_size().lines
    except OSError:
        # 如果无法获取终端尺寸，则返回一个默认值或 None
        return None

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 不需要真正连接到这个地址，只需用来触发本地 IP 的获取
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

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

def get_os_name():
    return platform.system()

def get_os_machine():
    return platform.machine()

def get_python_version():
    return platform.python_version()

def print_list_item(name,content):
    print("|" + name + " " * (15 - calculate_length(name)) + "|" + content + " " * (get_terminal_width()-18-calculate_length(content)) + "|")
    
# 创建并写入文件的简单程序

def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'