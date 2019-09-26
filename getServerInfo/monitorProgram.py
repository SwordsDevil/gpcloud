import paramiko

def transfer(path,host):
    private = paramiko.RSAKey.from_private_key_file(path)
    transport = paramiko.Transport((host,22))
    transport.connect(username='root',pkey=private)
    client = paramiko.SSHClient()
    client._transport = transport
    client.exec_command(command='tar -czf monitor.tar.gz ./monitor')
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(localpath='./monitor.tar.gz', remotepath='/opt/monitor.tar.gz')
    client.exec_command(command='tar xf /opt/monitor.tar.gz -C /opt/')
    transport.close()

def execute(path,host):
    private = paramiko.RSAKey.from_private_key_file(path)
    transport = paramiko.Transport((host,22))
    transport.connect(username='root',pkey=private)
    client = paramiko.SSHClient()
    client._transport = transport
    client.exec_command(command='python3 /opt/monitor/main.py',timeout=1)
    transport.close()