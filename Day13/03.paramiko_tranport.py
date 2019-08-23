#paramiko connect server use transport
#2019/08/21

import paramiko

private = paramiko.RSAKey.from_private_key_file('C:\\Users\陈文斌\.ssh\id_rsa')
transport = paramiko.Transport(('192.168.40.141',22))
transport.connect(username='root',pkey=private)
client = paramiko.SSHClient()
client._transport = transport

stdin,stdout,stderr = client.exec_command('vmstat',timeout=1)
print(stdout.read().decode('utf-8'))

transport.close()



#基于加密通道进行上下传文件
private = paramiko.RSAKey.from_private_key_file('C:\\Users\陈文斌\.ssh\id_rsa')
transport = paramiko.Transport(('192.168.40.141',22))
transport.connect(username='root',pkey=private)

sftp = paramiko.SFTPClient.from_transport(transport)

#get上传 put下传
# sftp.get(remotepath='/root/myname.txt',localpath='./file01.txt')
sftp.put(localpath='./file01.txt',remotepath='/root/file001.txt')

transport.close()
