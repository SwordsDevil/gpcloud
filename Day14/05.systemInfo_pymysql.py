import pymysql
import paramiko

#连接目标主机通过管道加密连接
private = paramiko.RSAKey.from_private_key_file('C:\\Users\陈文斌\.ssh\id_rsa')
transport = paramiko.Transport(('192.168.40.143',22))
transport.connect(username='root',pkey=private)
client = paramiko.SSHClient()
client._transport = transport

#通过相关shell命令获取系统信息
_,cpuUs,_ = client.exec_command(command="vmstat | awk 'NR==3{print $13}'",timeout=0.5)
_,cpuSy,_ = client.exec_command(command="vmstat | awk 'NR==3{print $14}'",timeout=0.5)
_,cpuId,_ = client.exec_command(command="vmstat | awk 'NR==3{print $15}'",timeout=0.5)
_,memTotal,_ = client.exec_command(command="free -mw | awk 'NR==2{print $2}'",timeout=0.5)
_,memUs,_ = client.exec_command(command="free -mw | awk 'NR==2{print $3}'",timeout=0.5)
_,memFree,_ = client.exec_command(command="free -mw | awk 'NR==2{print $4}'",timeout=0.5)
_,memCached,_ = client.exec_command(command="free -mw | awk 'NR==2{print $7}'",timeout=0.5)
_,diskRate,_ = client.exec_command(command="df -Th | awk 'NR==2{print $6}'",timeout=0.5)
cpuUs=int(cpuUs.read().decode('utf-8'))
cpuSy=int(cpuSy.read().decode('utf-8'))
cpuId=int(cpuId.read().decode('utf-8'))
memTotal=int(memTotal.read().decode('utf-8'))
memUs=int(memUs.read().decode('utf-8'))
memFree=int(memFree.read().decode('utf-8'))
memCached=int(memCached.read().decode('utf-8'))
memRate = ((memUs+memCached)/memTotal)*100
diskRate = int(diskRate.read().decode('utf-8')[0:2])

#连接数据库插入数据
clientA = pymysql.connect(host='192.168.40.143',port=3306,user='Swords',password='(Swords..0908)',db='systemInfo',charset='utf8')
cursors = clientA.cursor()
sql = "insert into info values({},{},{},{},{},{},{});"
cursors.execute(sql.format(cpuUs,cpuSy,cpuId,memUs,memFree,memRate,diskRate))
clientA.commit()
clientA.close()

transport.close()