import os
import psutil


def get_procs():
    print('Listing all processes...')
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)


def process_exists():
    print('Checking if the given process exists...')
    check_process_exists = psutil.pid_exists(6942)
    if check_process_exists:
        print(check_process_exists)
    else:
        print('The given process does not exists!')


def get_specific_proc():
    print('Showing given process...')
    especific_proc = psutil.Process(6942)
    especific_proc_name = especific_proc.name()
    print(especific_proc_name)


if __name__ == '__main__':
    get_procs()
    os.system('clear')
    process_exists()
    get_specific_proc()


