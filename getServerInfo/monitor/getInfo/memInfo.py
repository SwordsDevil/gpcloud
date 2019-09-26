import psutil

def mem():
    memory = psutil.virtual_memory()
    return memory.percent
