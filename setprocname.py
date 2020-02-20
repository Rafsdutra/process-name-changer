import os
import psutil


# Lists all processes
def get_procs():
    print('Listing all processes...')
    for proc in psutil.process_iter(['pid', 'name']):
        print('Processo:' + str(proc.info))
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


# Get a specific process and show its name
def get_process_by_name():
    print('Search process by its name!')
    process_name_input = str(input("Insert name process: "))
    process = []
    for p in psutil.process_iter([process_name_input]):
        if p.info[process_name_input] == process_name_input:
            process.append(p)
            print('Process found! Name: ' + str(process))

    else:
        print("Process not found!")

    # especific_proc = psutil.Process(6942)
    # especific_proc_name = especific_proc.name()
    # print("Nome do Processo: " + str(process))


if __name__ == '__main__':
    # get_procs()
    # os.system('clear')
    # check_if_process_exists()
    get_process_by_name()
