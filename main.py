# -*- coding: utf-8 -*-

import os
import shutil

output_folder = os.path.join(os.path.normpath(
    os.path.expanduser("~/Desktop")))
workDir = os.path.dirname(os.path.abspath(__file__))
extensions_list = os.path.join(workDir, r"instalation_files_extensions.txt")
folders_list = os.path.join(workDir, r"include_folders_list.txt")
exclude_files_list = os.path.join(workDir, r"exlude_files_list.txt")


def get_installation_files():
    folders = get_file(folders_list)
    folders_arr = []
    for folder in folders:
        folders_arr.append(folder.split(","))

    for folder in folders_arr:
        input, output = folder
        try:
            shutil.copytree(input, os.path.join(output_folder, "publish",output),dirs_exist_ok=True,ignore=shutil.ignore_patterns('*.pdb', 'tmp*'))
        except:
            print(f"Error: {input}")

def cleanup_files():
    extensions = get_file(extensions_list)
    for dirname, dirnames, filenames in os.walk(output_folder):
        for filename in filenames:
            try:
                if any(ext.lower() in filename.lower() for ext in extensions):
                    continue
                os.remove(os.path.join(dirname, filename))
                print(f"{filename}\n")
            except Exception as e:
                print(f"Error:{filename}. {e}")


def get_file(file):
    with open(file, newline='', encoding='utf8') as f:
        reader = f.read().splitlines()
    return reader


print(f'Program Start in {workDir} folder')
get_installation_files()
# cleanup_files()
print(f'Program end.')