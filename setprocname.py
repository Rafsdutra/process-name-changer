import os
import psutil


# Lists all processes
def get_procs():
    print('Listing all processes...')
    for proc in psutil.process_iter(['pid', 'name']):
        print('Process:' + str(proc.info))
        print('----------------------------------------------------')


# Search a process by its ID or name
def check_if_process_exists():
    pid_input = int(input("Insert a Process ID: "))
    process_all_info = psutil.Process(pid_input)
    process_name = process_all_info.name()
    check_process_exists = psutil.pid_exists(pid_input)

    print('Checking if the given process exists...')
    if check_process_exists:
        print("The process <" + str(process_name) + "> with ID <" + str(pid_input) + "> exists!")
    else:
        print('The given process does not exists!')


def find_procs_by_name():
    pname = input(str("Insert the process name: "))
    print(pname)
    arr = [pname]
    ls = []
    for p in psutil.process_iter(arr, ["exe", "cmdline"]):
        if pname == p.info(pname) or \
                p.info(pname) and os.path.basename(p.info['exe']) == pname or \
                p.info['cmdline'] and p.info['cmdline'][0] == pname:
            ls.append(p)
    print(ls)


if __name__ == '__main__':
    # get_procs()
    # os.system('clear')
    # check_if_process_exists()
    find_procs_by_name()
