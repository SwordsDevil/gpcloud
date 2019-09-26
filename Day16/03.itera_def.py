import os
import psutil


def showInfo(process):
    """
    The size of the memory occupied by the current program
    :param process: current program's name
    :return: memory's name and memory's size
    """
    pid = os.getpid()
    info = psutil.Process(pid)
    memory = info.memory_full_info()
    size = memory.uss / 1024 / 1024
    print('{} memory used: {} MB'.format(process, size))


def iterator():
    showInfo('Current Program')
    number = [i for i in range(1000000)]
    showInfo('After initial iterator')
    print(sum(number))
    showInfo('After sum number')


def generator():
    showInfo('Current Program')
    number = (i for i in range(1000000))
    showInfo('After initial iterator')
    print(sum(number))
    showInfo('After sum number')


iterator()
generator()