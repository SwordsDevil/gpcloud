import pymysql
import openpyxl

client = pymysql.connect(
    host='192.168.40.143',
    port=3306,
    user='Swords',
    password='(Swords..0908)',
    db='pycloud',
    charset='utf8'
)

cursors = client.cursor()
sql = "select * from {}"
cursors.execute(sql.format('FirstStage'))
data = cursors.fetchall()
file = openpyxl.Workbook()
sheet = file.active
sheet.append(['ID','Name','FirstExam','SecondExam','PointsDeffrence'])
for info in data:
    sheet.append(info)
file.save('./fileExcel/grade.xlsx')
client.close()
