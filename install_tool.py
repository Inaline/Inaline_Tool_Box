import os
import json
import requests
from public import *  # Assuming print_list_item is a valid function in the public module

url = "https://inaline.github.io/mods.json"

# Step 1: Use requests library to get the content from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the JSON content
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Failed to parse JSON data.")
        exit()

    # Step 3: Extract the 'name' from each item
    names = [item['name'] for item in data.values()]

    # Step 4: Print the names using the print_list_item function
    print(" - List of all tool mod")
    print("/" + "-" * (get_terminal_width()-2) + "\\")
    print_list_item("ID","Name")
    for index, name in enumerate(names, start=0):
        print_list_item(str(index), name)
    print("\\" + "-" * (get_terminal_width()-2) + "/")

    id = input("Enter a sequence number to continue:")

    res = get_nth_key_value_pair(data, int(id))

    if res:
        # Assuming the format of res is [["key", {"name": "value", ...}], ...]
        # We need to extract the "name" and "url" from the dictionary
        _, info_dict = res[0]  # Assuming there's only one element in res
        nam = info_dict.get("name")
        url = info_dict.get("url")

        if nam and url:
            input("Carriage return alignment for a download.")
            clone_dir = f"./mods/{nam}/"
            os.makedirs(clone_dir, exist_ok=True)
            os.system(f"wget {url} -P {clone_dir}")
            
            # Create info.json file
            info_json_path = os.path.join(clone_dir, "init.json")
            with open(info_json_path, 'w') as json_file:
                json.dump(info_dict, json_file, indent=4)
        else:
            print("URL or name not found in the data.")
    else:
        print("Failed to retrieve the key-value pair.")
else:
    print("Failed to retrieve data from URL.")