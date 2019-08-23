import paramiko

private = paramiko.RSAKey.from_private_key_file('C:\\Users\陈文斌\.ssh\id_rsa')
transport = paramiko.Transport(('192.168.40.143',22))
transport.connect(username='root',pkey=private)
client = paramiko.SSHClient()
client._transport = transport

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put(localpath='./web_Info',remotepath='/tasks/webInfo')

stdin,stdout,stderr =client.exec_command(command="echo '00 00 */1 * * python3 /tasks/webInfo' >>/var/spool/cron/$(whoami)",timeout=1)

transport.close()