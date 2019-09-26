import psutil

def disk():
    disk = psutil.disk_usage('/')
    return disk.percent
