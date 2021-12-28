import os
import shutil
from datetime import datetime

HOSTNAME = os.uname()[1]
DEFAULT_ARCHIVE_FOLDER = f'C:\\Users\\{HOSTNAME}\\AppData\\Romaing\\DarkSoulsIII\\'
DEFAULT_BACKUP_FOLDER = f'C:\\Users\\{HOSTNAME}\\AppData\\Romaing\\mybackup\\'


def new_backup():
    current_timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    archive_folder = DEFAULT_ARCHIVE_FOLDER
    target_folder = os.path.join(DEFAULT_BACKUP_FOLDER, current_timestamp)
    shutil.copytree(archive_folder, target_folder)
    print(f'new backup:{current_timestamp} generated')


def list_backup():
    all_backup_folders = os.listdir(DEFAULT_BACKUP_FOLDER)
    all_backup_folders.sort(reverse=True)
    return [(i + 1, x) for i, x in enumerate(all_backup_folders)]


def load_backup(backup_name: str):
    shutil.rmtree(DEFAULT_ARCHIVE_FOLDER)
    target_folder = os.path.join(DEFAULT_BACKUP_FOLDER, backup_name)
    shutil.copytree(target_folder, DEFAULT_ARCHIVE_FOLDER)
    print(f'use backup:{backup_name}')


def make_choice(min_value: int, max_value: int):
    while True:
        try:
            choice = input(f'input a number from {min_value} to {max_value} to make a choice:')
            choice = int(choice)
            if choice not in range(min_value, max_value + 1):
                raise Exception(f'unknown choice: {choice}')
        except Exception as e:
            print(e)
        else:
            print(choice)
            return choice


def quick_backup():
    print("make sure you've exit game already")
    new_backup()


def quick_load():
    print('these are latest backup:')
    current_backup = list_backup()
    if not current_backup:
        print('no available backup')
        return
    for backup in current_backup:
        print(f'[{backup[0]}]:{backup[1]}')
    choice = make_choice(1, len(current_backup))
    target_backup = current_backup[choice - 1]
    load_backup(target_backup[1])


def main():
    print('choose what you want:')
    print('[1] quick backup')
    print('[2] load a backup')
    things_to_do = make_choice(1, 2)
    if things_to_do == 1:
        quick_backup()
    else:
        quick_load()


if __name__ == '__main__':
    main()
