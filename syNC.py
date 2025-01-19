#!/usr/bin/python3

''' Script that allows you to sync your files in desired directories '''

import os
from os.path import isfile, join, getmtime
import argparse
import tempfile
import shutil

# Set terminal ANSI code colors
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAILRED = '\033[91m'
ENDC = '\033[0m'

def get_files(path):
    '''Return list of all files from the directory'''
    return [f for f in os.listdir(path) if isfile(join(path, f))]

def modTime(file_path):
    '''Get the file modification time'''
    return getmtime(file_path)

def compare_files(files1, files2, all_files):
    '''Compare all files'''
    temp_dir = str(tempfile.mkdtemp())

    for file in all_files:
        print(f"File: {file}", end=" ")
        # check if the file is in both directories
        if file in files1 and file in files2:
            time1 = modTime(files1[-1] + "/" + file)
            time2 = modTime(files2[-1] + "/" + file)
            time_diff = time1 - time2

            if time_diff > 0:
                print(WARNING + "[i] In path1 is newer" + ENDC)
                shutil.copy2(files1[-1] + "/" + file, temp_dir)
            else:
                if time_diff < 0:
                    print(WARNING + "[i] In path2 is newer" + ENDC)
                shutil.copy2(files2[-1] + "/" + file, temp_dir)
        
        elif file in files1: # check if file is in files1
            print(WARNING + "[i] Found only in the first path" + ENDC)
            shutil.copy2(files1[-1] + "/" + file, temp_dir)
        else: # file is in files2
            print(WARNING + "[i] Found only in the second path" + ENDC)
            shutil.copy2(files2[-1] + "/" + file, temp_dir)

    print(OKGREEN + f"[+] Files synced successfully here's directory: {temp_dir}" + ENDC)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("p1", type=str, help="1st path")
    parser.add_argument("p2", type=str, help="2nd path")
    args = parser.parse_args()

    path1 = args.p1
    path2 = args.p2

    path1_files = get_files(path1)
    path2_files = get_files(path2)

    len_1 = len(path1_files)
    len_2 = len(path2_files)

    if len_1 == 0 or len_2 == 0:
        print(FAILRED + "[!] No files" + ENDC)
        return 1

    all_files = list(set(path1_files + path2_files))

    path1_files.append(path1)
    path2_files.append(path2)
    
    compare_files(path1_files, path2_files, all_files)

    return 0

if __name__ == "__main__":
    main()
