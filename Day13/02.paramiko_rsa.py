#paramiko connect server use id_rsa
#2019/08/21

import paramiko

private = paramiko.RSAKey.from_private_key_file(r'C:\Users\陈文斌\.ssh\id_rsa')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname='192.168.40.141',
    port=22,
    username='root',
    pkey=private
)

stdin,stdout,stderr = client.exec_command(command='sl',timeout=1)
print(stderr.read().decode('utf-8'))

client.close()

