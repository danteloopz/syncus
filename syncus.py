import os
import argparse
import shutil
import threading
import json
import logging
log = logging.getLogger(__name__)

# Set terminal ANSI code colors
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAILRED = '\033[91m'
ENDC = '\033[0m'

def modTime(file_path):
    '''Get the file modification time'''
    return os.path.getmtime(file_path)

def load_config():
    '''Load config from json file'''
    try:
        json_config_file = open("./config.json")
        conf_content = json_config_file.read()
        json_config_file.close()
    except:
        new_content = {
            "os": os.name,
            "sync": 60,
            "paths": []
        }
        write_config(new_content)
        conf_content = new_content
    config = json.loads(conf_content)
    if conf_content["name"] != os.name:
        log.error("this config is not for this os")
        exit(1)
    return config

def write_config(content):
    '''write config to json file'''
    json_config_file = open("./config.json", "w")
    json_config_file.write(json.dumps(content))
    json_config_file.close()

def add_paths(orig_path, copy_path, config):
    paths = config["paths"]
    paths.append([orig_path, copy_path])
    config["paths"] = paths
    write_config(config)

def del_paths(orig_path, copy_path, config):
    paths = config["paths"]
    paths.remove([orig_path, copy_path])
    config["paths"] = paths
    write_config(config)

def set_sync_time(sec, config):
    config["sync"] = sec
    write_config(config)

def sync(config):
    paths = config["paths"]
    for rec in paths:
        src = rec[0]
        copy = rec[1]


def main():
    logging.basicConfig(filename="syncus.log", level=logging.INFO)
    log.info("started syncus")

if __name__ == '__main__':
    main()