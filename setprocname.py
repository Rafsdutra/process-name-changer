import os
from random import randint

import psutil


def get_procs():
    print('Listing all processes...')
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)


def process_exists():
    print('Checking if the given process exists...')
    check_process_exists = psutil.pid_exists(randint(0, 9000))
    if check_process_exists:
        print(check_process_exists)
    else:
        print('The given process does not exists!')


def get_specific_proc():
    print('Showing given process...')
    especific_proc = psutil.Process(randint(0, 9000))
    especific_proc_name = especific_proc.name()
    print(especific_proc_name)


if __name__ == '__main__':
    get_procs()
    os.system('clear')
    process_exists()
    get_specific_proc()


