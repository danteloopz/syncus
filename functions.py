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

def get_syncus_version():
    ver = 1.0
    return ver

def modTime(file_path):
    '''Get the file modification time'''
    return os.path.getmtime(file_path)

def check_os(config):
    if config["os"] != os.name:
        log.error("this config is not for this os")
        exit(1)

def load_config():
    '''Load config from json file'''
    log_path = "./config.json"
    if os.path.exists(log_path):
        json_config_file = open(log_path)
        conf_content = json_config_file.read()
        json_config_file.close()
    else:
        new_content = {
            "os": os.name,
            "sync": 60,
            "paths": []
        }
        write_config(new_content)
        config = new_content
        check_os(config)
        return config

    config = json.loads(conf_content)
    check_os(config)
    return config

def write_config(content):
    '''write config to json file'''
    json_config_file = open("./config.json", "w")
    json_config_file.write(json.dumps(content))
    json_config_file.close()

def add_paths(orig_path, copy_path, config):
    paths = config["paths"]
    if not(os.path.isdir(copy_path)):
        log.error("given path is no a dir")
        return
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

def cp_file(src_path, copy_path):
    try:
        copy_file = open(copy_path)
    except:
        try:
            shutil.copyfile( src_path, copy_path, follow_symlinks=True)
        except:
            log.error("user doesn't have rights to: " + copy_path)
    else:    
        srcT = modTime(src_path)
        copyT = modTime(copy_path)
        if copyT > srcT:
            try:
                shutil.copyfile( src_path, copy_path, follow_symlinks=True)
                log.info("copying: " + src_path)
            except:
                log.error("user doesn't have rights to: " + copy_path)
        else:
            log.info("file wasn't modified: " + src_path)
            return

def sync(src, copy):
    src_name = os.path.basename(src)
    if os.path.isdir(src):
        copy = os.path.join(copy, src_name)
        os.makedirs(copy, exist_ok=True)
        try:
            dirlist = os.listdir(src)
        except PermissionError:
            log.error("user diesnt have premisions for: " + src)
            return
        for rec in dirlist:
            sync(src=os.path.join(src, rec),copy=copy)
    else:
        cp_file(src, os.path.join(copy, src_name))



def sync_start(config):
    paths = config["paths"]
    for rec in paths:
        thread = threading.Thread(target=sync, args=(rec[0],rec[1]))
        thread.run()
             
def main():
    log_dir = "./log"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(filename=os.path.join(log_dir, "syncus.log"), level=logging.INFO)
    log.info("started syncus")
    config = load_config()
    sync_start(config)


if __name__ == '__main__':
    main()
