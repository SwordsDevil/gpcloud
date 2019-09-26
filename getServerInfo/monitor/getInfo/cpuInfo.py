import psutil

def cpu():
    cpu = psutil.cpu_times_percent(interval=1)
    return cpu.user + cpu.system

