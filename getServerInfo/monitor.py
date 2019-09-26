from monitorProgram import execute
import pymysql
import time
host = ['192.168.40.141']
for ip in host:
    execute('/root/.ssh/id_rsa',ip)

time.sleep(5)

client = pymysql.connect(host='192.168.40.142',user='Swords',passwd='(Swords..0908)',db='systemInfo')
with client.cursor() as cursors:
    sql = "select {} from {}"
    database= (('cpuPercent','cpu'),('memPercent','mem'),('diskPercent','disk'))
    for field,table in database:
        cursors.execute(sql.format(field,table))
        data = cursors.fetchall()
        if field == 'cpuPercent':
            if float(data[-1][0]) > 85:
                print('报警了')
        elif field =='memPercent':
            if float(data[-1][0]) >95:
                print('报警了')
        elif field == 'diskPercent':
            if float(data[-1][0]) >90:
                print('报警了')
client.close()