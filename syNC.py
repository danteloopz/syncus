#!/usr/bin/python3

''' Script that allows you to sync your files in desired directories '''

import os
from os.path import isfile, join
import argparse
import tempfile
import shutil

# Set terminal ANSI code colors
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAILRED = '\033[91m'
ENDC = '\033[0m'

def get_all_files(path):
    '''Return list of all files from the directory'''
    return [f for f in os.listdir(path) if isfile(join(path, f))]


def modification_time(file_path):
    '''Get the file modification time'''
    stat = os.stat(file_path)
    try:
        return stat.st_birthtime
    except AttributeError:
        return stat.st_mtime

def compare_files(files1, files2):
    '''Compare files from input lists'''
    outdated = 0
    temp_dir = str(tempfile.mkdtemp())

    for file in files1:
        if file in files2:
            time1 = modification_time(files1[-1] + "/" + file)
            time2 = modification_time(files2[-1] + "/" + file)
            time_diff = time1 - time2
            print(f"File: {file}", end=" ")
            outdated += 1

            if time_diff > 0:
                print(WARNING + "[i] In path1 is newer" + ENDC)
                shutil.copy2(files1[-1] + "/" + file, temp_dir)
            elif time_diff < 0:
                print(WARNING + "[i] In path2 is newer" + ENDC)
                shutil.copy2(files2[-1] + "/" + file, temp_dir)
            else:
                print(OKGREEN + "[+] Both files are up to date" + ENDC)
                outdated -= 1
    if outdated:
        print(FAILRED + f"[!] There are {outdated} file(s)" + ENDC)
        print(OKGREEN + f"[+] Synced files in: {temp_dir}" + ENDC)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("p1", type=str, help="1st path")
    parser.add_argument("p2", type=str, help="2nd path")
    args = parser.parse_args()

    path1 = args.p1
    path2 = args.p2

    path1_files = get_all_files(path1)
    path2_files = get_all_files(path2)

    len_1 = len(path1_files)
    len_2 = len(path2_files)

    if len_1 == 0 or len_2 == 0:
        print(FAILRED + "[!] No files" + ENDC)
        return 1

    path1_files.append(path1)
    path2_files.append(path2)


    if len_1 > len_2:
        compare_files(path2_files, path1_files)
    else:
        compare_files(path1_files, path2_files)

    return 0

if __name__ == "__main__":
    main()
