#/usr/bin/env python3
# coding = utf-8
#
#author:SwordsDevil
#date:2019/08/06
#usage: find sign of zodiac and constellation when input date of birth


zodiac = ("🐵","🐤","🐶","🐖","🐭","🐮","🐅","🐰","🐉","🐍","🐎","🐏")

constellation = ('水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座',
                '狮子座','处女座','天秤座','天蝎座','射手座','魔羯座')
constelldate = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

year = int(input("please input year:"))
print(zodiac[year % 12])
month = int(input("please input month:"))
day = int(input("please input day:"))

for index in range(len(constellation)):
    if (month,day) >= constelldate[index] and (month,day) <constelldate[index + 1]:
        print(constellation[index])
    elif ((month,day) <(1,20) and (month,day >=(1,1))) or ((month,day) >= (12,22) and (month,day) <=(12,30)):
        print(constellation[11])
        break
    elif month >12 or day >31 :
        print('please input right date')
        break