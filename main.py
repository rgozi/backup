import os
import pathlib
import shutil
from datetime import datetime

HOSTNAME = os.uname()[1]
DEFAULT_ARCHIVE_FOLDER = f'C:\\Users\\{HOSTNAME}\\AppData\\Romaing\\DarkSoulsIII\\'
DEFAULT_BACKUP_FOLDER = f'C:\\Users\\{HOSTNAME}\\AppData\\Romaing\\mybackup\\'


def new_backup():
    current_timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    archive_folder = DEFAULT_ARCHIVE_FOLDER
    target_folder = pathlib.Path.joinpath(DEFAULT_BACKUP_FOLDER, current_timestamp)
    shutil.copytree(archive_folder, target_folder)


def list_backup():
    all_backup_folders = os.listdir(DEFAULT_BACKUP_FOLDER)
    all_backup_folders.sort(reverse=True)
    return [(i + 1, x) for i, x in enumerate(all_backup_folders)]


def load_backup(backup_name: str):
    shutil.rmtree(DEFAULT_ARCHIVE_FOLDER)
    target_folder = pathlib.Path.joinpath(DEFAULT_BACKUP_FOLDER, backup_name)
    shutil.copytree(target_folder, DEFAULT_ARCHIVE_FOLDER)


if __name__ == '__main__':
    pass
