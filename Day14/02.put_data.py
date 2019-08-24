import pymysql

client = pymysql.connect(
    host='192.168.40.143',
    port=3306,
    user='Swords',
    password='(Swords..0908)',
    db='pycloud',
    charset='utf8'
)
cursors = client.cursor()


with open(file='grade.txt', mode='r', encoding='utf8') as file:
    ID = 0
    for lines in file.readlines():
        Name, FirstExam, SecondExam, PointsDifferent = lines.split()
        sql = "insert into FirstStage values ({}, '{}', {}, {}, {});"
        ID += 1
        cursors.execute(sql.format(ID, Name, int(FirstExam), int(SecondExam), int(PointsDifferent)))
client.commit()
client.close()
