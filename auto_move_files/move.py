import os
import json
import time

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except:
    os.system('pip install watchdog')
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

import shutil


def get_config_data():
    with open('config.json', 'r') as f:
        config_dict = json.load(f)
    return config_dict


SOURCE_DIRS =  get_config_data()['source_dir']
DESTINATION_DIRS =  get_config_data()['source_dir']
CLASSIFICAITON_DIRS =  get_config_data()['classifications'].keys()


def create_classification_dir():
    for d in CLASSIFICAITON_DIRS:
        d = SOURCE_DIRS + '\\' + d
        try:
            os.mkdir(d)
            print('创建新文件夹%s' % d)
        except:
            # 忽略已存在文件夹
            pass


def classify_file(file_name):
    folder_des = 'others'
    for category, keywords in get_config_data()['classifications'].items():
        suffix_list = keywords['suffix']
        prefix_list = keywords['prefix']
        for suffix in suffix_list:
            if suffix != '' and file_name.endswith(suffix):
                folder_des = category
                #print('%s 属于分类 %s' % ( file_name, category))
                return folder_des

        for prefix in prefix_list:
            if prefix != '' and file_name.startswith(prefix):
                folder_des = category
                #print('%s 属于分类 %s' % (file_name, category))
                return folder_des

    #print(folder_des)
    return folder_des
    

def move_multiple_times(source_dir, destination_dir):
    try:
        shutil.move(source_dir, destination_dir)
    except PermissionError:
        time.sleep(1)
        move_multiple_times(source_dir, destination_dir)


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        for file_name in os.listdir(SOURCE_DIRS):
            # 过滤文件夹
            file_abs_dir = SOURCE_DIRS + '\\' + file_name
            if os.path.isdir(file_abs_dir):
                continue
            source_dir = os.path.join(DESTINATION_DIRS, file_name)
            folder = classify_file(file_name)
            destination_dir = os.path.join(DESTINATION_DIRS, folder, file_name)
            print('source_dir', source_dir)
            print('destination_dir', destination_dir)
            move_multiple_times(source_dir, destination_dir)


create_classification_dir()
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, DESTINATION_DIRS, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt as e:
    observer.stop()
    observer.join()