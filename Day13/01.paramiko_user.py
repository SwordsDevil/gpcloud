#paramiko connnect server with user and passwd
#2010/08/21

import  paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(
    hostname='192.168.40.141',
    port=22,
    username = 'root',
    password = '1'
)

stdin,stdout,stderr = client.exec_command(command='ls',timeout=1)
print(stdout.read().decode('utf-8'))

client.close()

