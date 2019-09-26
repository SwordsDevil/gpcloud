import subprocess

result = subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
