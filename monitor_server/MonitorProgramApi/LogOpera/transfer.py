import paramiko

def transfer(RSApath,host,user):
    private = paramiko.RSAKey.from_private_key_file(RSApath)
    transport = paramiko.Transport((host,22))
    transport.connect(username=user,pkey=private)
    client = paramiko.SSHClient()
    client._transport = transport
    client.exec_command(command='tar -czf ServerCollectInfoApi.tar.gz ../../ServerCollectInfoApi')
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(localpath='../../ServerCollectInfoApi', remotepath='/opt/ServerCollectInfoApi.tar.gz')
    client.exec_command(command='tar xf /opt/ServerCollectInfoApi.tar.gz -C /opt/')
    transport.close()

def execute(RSApath,host,user,port=22):
    private = paramiko.RSAKey.from_private_key_file(RSApath)
    transport = paramiko.Transport((host,port))
    transport.connect(username=user,pkey=private)
    client = paramiko.SSHClient
    client._transport = transport
    client.exec_command(command="echo '*/5 * * * * python3 /opt/ServerCollectInfoApi/agent.py &' >>/var/spool/cron/$(whoami)")
    transport.close()
