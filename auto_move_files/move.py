from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import shutil
from custom import file

path_root = r'C:\PycharmProjects\move_files'
folder_to_track = r'C:\PycharmProjects\move_files\downloads'
file_json = r'C:\PycharmProjects\move_files\config.json'


def get_des_folder(filname):
    data_dict = file.read_json(file_json)
    for category, keywords_folder_dict in data_dict.items():
        keywords_dict = keywords_folder_dict.get('keywords', {})
        prefix_list = keywords_dict.get('prefix', [])
        suffix_list = keywords_dict.get('suffix', [])
        folder = keywords_folder_dict.get('folder', '')

        if not keywords_dict:
            continue
        if not folder:
            continue

        if not prefix_list:
            continue
        if not suffix_list:
            continue

        for prefix in prefix_list:
            if str(filname).startswith(prefix):
                folder_des = folder

        for suffix in suffix_list:
            if str(filname).endswith(suffix):
                folder_des = folder
    try:
        return folder_des
    except UnboundLocalError:
        folder_des = data_dict.get('other', {}).get('folder', '')
        return folder_des


def move_multiple_times(file_src, file_des):
    try:
        shutil.move(file_src, file_des)
    except PermissionError:
        time.sleep(1)
        move_multiple_times(file_src, file_des)


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        for filename in os.listdir(folder_to_track):
            file_src = os.path.join(folder_to_track, filename)

            folder = get_des_folder(filename)
            file_des = os.path.join(path_root, folder, filename)

            print(file_src)
            print(file_des)

            # if folder == 'movie':
            #     time.sleep(10)
            # if folder == 'pic':
            #     time.sleep(1)
            # if folder == 'novel':
            #     time.sleep(1)

            move_multiple_times(file_src, file_des)


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt as e:
    observer.stop()
    observer.join()

# def main():
#     filename = '1.txt'
#
#     print(file_des)
#
#
# if __name__ == '__main__':
#     main()
