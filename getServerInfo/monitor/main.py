from getInfo import cpuInfo
from getInfo import memInfo
from getInfo import diskInfo
import pymysql
import time
import subprocess

hostname = subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
client = pymysql.connect(host='192.168.40.142',user='Swords',password='(Swords..0908)',db='systemInfo')
with client.cursor() as cursors:
    insert = "insert into cpu values ({},'{}',{});"
    cursors.execute(insert.format(
        time.strftime('%Y%m%d%H%M%S'),
        hostname.stdout.decode('utf-8'),
        cpuInfo.cpu()
    ))
    client.commit()

with client.cursor() as cursors:
    insert = "insert into mem values ({},'{}',{});"
    cursors.execute(insert.format(
        time.strftime('%Y%m%d%H%M%S'),
        hostname.stdout.decode('utf-8'),
        memInfo.mem()
    ))
    client.commit()

with client.cursor() as cursors:
    insert = "insert into disk values ({},'{}',{});"
    cursors.execute(insert.format(
        time.strftime('%Y%m%d%H%M%S'),
        hostname.stdout.decode('utf-8'),
        diskInfo.disk()
    ))
    client.commit()

client.close()