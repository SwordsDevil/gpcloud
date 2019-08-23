import redis

#建立连接池
pool = redis.ConnectionPool(host='192.168.40.142',port=6379,db=0)
#连接客户端
client = redis.Redis(connection_pool=pool)

#string单个字符设置
client.set(name='chen',value='18')
result = str(client.get(name='chen'),'utf8')
print(result)

#string多个字符的设置
client.mset(mapping={'chen':18,'wen':16,'bin':14})
result = client.mget(keys=('chen','wen','bin'))
print(result)

#删除某些字符
client.delete('chen','wen')
result = client.mget(keys=('chen','wen','bin'))
print(result)

#修改字符（若字符不存在设置该字符，若已经存在修改其值）
client.set(name='chen',value=16)
result = client.get(name='chen')
print(result)