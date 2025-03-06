import os
import shutil
import json
import logging
log = logging.getLogger(__name__)
config_path = "./config.json"


# Set terminal ANSI code colors
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAILRED = '\033[91m'
ENDC = '\033[0m'

def ok(mess):
    print(OKGREEN + "[+] " + mess + ENDC)

def warn(mess):
    print(WARNING + "[!] " + mess + ENDC)

def fail(mess):
    print(FAILRED + "[-] " + mess + ENDC)

def load_config(config_file=config_path):
    """
    Loads the configuration from a JSON file. If the file does not exist, it creates one with
    default content.

    Parameters:
    - config_file (str): The path to the config JSON file.

    Returns:
    - dict: The configuration data as a dictionary.
    """
    if os.path.exists(config_file):
        with open(config_file, 'r') as json_config_file:
            conf_content = json_config_file.read()
    else:
        new_content = {
            "sync_on": True,
            "sync_freq": 60,  # Default sync frequency in seconds
            "sync_type": "duplicate",
            "paths": []  # Default empty list of directory pairs
        }
        save_config(new_content)  # Save the new config
        return new_content

    config = json.loads(conf_content)
    return config

def save_config(config, config_file=config_path):
    """
    Save the updated configuration to a JSON file.

    Parameters:
    - config (dict): The configuration data to be saved.
    - config_file (str): The path to the config JSON file.
    """
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)

# Get the list of files from source dir that are newer than in destination dir
def get_newer_files(src_dir, dest_dir):
    """
    Returns a list of files from src_dir that are newer than in dest_dir.
    """
    newer_files = []
    for src_file in os.listdir(src_dir):
        src_file_path = os.path.join(src_dir, src_file)
        dest_file_path = os.path.join(dest_dir, src_file)

        # Check if the file exists in dest_dir and compare timestamps
        if os.path.exists(dest_file_path):
            if os.path.getmtime(src_file_path) > os.path.getmtime(dest_file_path):
                newer_files.append(src_file)
        else:
            # If file doesn't exist in dest_dir, it's considered newer
            newer_files.append(src_file)

    return newer_files

def sync_merge(dir_a, dir_b):
    """
    Sync files and directories from dir_a to dir_b by copying newer files from dir_a to dir_b.
    Copies all directories and files, maintaining the structure.
    """
    for dirpath, dirnames, filenames in os.walk(dir_a):
        # Determine the corresponding destination directory
        rel_path = os.path.relpath(dirpath, dir_a)
        dest_dir = os.path.join(dir_b, rel_path)

        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for file in filenames:
            src_file_path = os.path.join(dirpath, file)
            dest_file_path = os.path.join(dest_dir, file)

            # Check if it's a file and copy if it's newer
            if os.path.isfile(src_file_path):
                if not os.path.exists(dest_file_path) or os.path.getmtime(src_file_path) > os.path.getmtime(dest_file_path):
                    shutil.copy(src_file_path, dest_file_path)

def sync_duplicate(dir_a, dir_b):
    """
    Sync all files and directories from dir_a to dir_b, adding version suffix to duplicates.
    Copies all directories and files, maintaining the structure.
    """
    for dirpath, dirnames, filenames in os.walk(dir_a):
        # Determine the corresponding destination directory
        rel_path = os.path.relpath(dirpath, dir_a)
        dest_dir = os.path.join(dir_b, rel_path)

        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for file in filenames:
            src_file_path = os.path.join(dirpath, file)
            dest_file_path = os.path.join(dest_dir, file)

            # Check if it's a file and handle duplicates by adding a version suffix
            if os.path.isfile(src_file_path):
                if os.path.exists(dest_file_path):
                    base, ext = os.path.splitext(file)
                    version = 1
                    # Generate a new file name with a version suffix until it's unique
                    while os.path.exists(os.path.join(dest_dir, f"{base}_ver_{version}{ext}")):
                        version += 1
                    dest_file_path = os.path.join(dest_dir, f"{base}_ver_{version}{ext}")

                shutil.copy(src_file_path, dest_file_path)


def sync_start(config):
    """
    Start the sync process based on the given config and sync_type.
    sync_type can be either "merge" or "duplicate".
    """
    for pair in config["paths"]:
        dir_a = pair["dir_a"]
        dir_b = pair["dir_b"]
        
        if config["sync_type"] == "merge":
            sync_merge(dir_a, dir_b)
        elif config["sync_type"] == "duplicate":
            sync_duplicate(dir_a, dir_b)
        else:
            return

# Function to add a new directory pair to the config
def add_paths(dir_a, dir_b, config):
    """
    Adds a new directory pair (dir_a, dir_b) to the config.
    """
    # Check if the directory pair already exists
    for pair in config["paths"]:
        if pair["dir_a"] == dir_a and pair["dir_b"] == dir_b:
            return

    if not(os.path.isdir(dir_a)):
        return
    
    # Add the new pair to the directory list
    config["paths"].append({"dir_a": dir_a, "dir_b": dir_b})
    
    # Save the updated config
    save_config(config)

# Function to delete a directory pair from the config
def del_paths(dir_a, dir_b, config):
    """
    Deletes a directory pair (dir_a, dir_b) from the config.
    """
    # Find and remove the pair from the directories list
    for pair in config["paths"]:
        if pair["dir_a"] == dir_a and pair["dir_b"] == dir_b:
            config["paths"].remove(pair)
            # Save the updated config
            save_config(config)
            return

def change_sync_type(sync_type, config):
    """
    Change sync_type
    """
    config["sync_type"] = sync_type
    save_config(config)

def change_sync_freq(sync_freq, config):
    """
    Change sync_freq
    """
    config["sync_freq"] = sync_freq
    save_config(config)

def change_sync_status(sync_status, config):
    """
    Change sync_freq
    """
    config["sync_on"] = sync_status
    save_config(config)


