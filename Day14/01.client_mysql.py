# import pymysql
#
# client = pymysql.connect(
#     host='192.168.40.143',
#     user='Swords',
#     password='(Swords..0908)',
#     db='pycloud'
# )
#
# cursors = client.cursor()
#
# sql = "insert into FirstStage values(1,'chenwenbin',31,42,11);"
# cursors.execute(sql)
#
# client.commit()
#
# client.close()
import pymysql

client = pymysql.connect(
    host='',
    username='',
    password='',
    db=''
)
try:
    with client.cursor() as cursors:
        sql = 'insert into cpu values();'
        cursors.execute(sql)
    client.commit()
finally:
    client.close()