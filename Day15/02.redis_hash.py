import  redis

pool = redis.ConnectionPool(host='192.168.40.142',port=6379,db=0)
client = redis.Redis(connection_pool=pool)

client.hset(name='cpuInfo',key='user',value='33.03')
result = client.hget(name='cpuInfo',key='user')
print(str(result,'utf8'))

#批量的设置hash的键值和批量获取键值
client.hmset(name='cpuInfo',mapping={'user':'32.00','system':'24.00','idle':'46.00'})
result = client.hmget(name='cpuInfo',keys=('user','system','idle'))
print(result)

#获取hash中所有的键值对
result = client.hgetall(name='cpuInfo')
print(result)

#获取hash中所有的keys
result = client.hkeys(name='cpuInfo')
print(result)

#获取hash中所有的values
result = client.hvals(name='cpuInfo')
print(result)

#删除某个键值对
client.hdel('cpuInfo','user')
result = client.hget(name='cpuInfo',key='user')
print(result)

#删除整个字典
# client.delete('cpuInfo')
# result = client.hgetall('cpuinfo')
# print(result)

#检测hash内部的键值是否存在
if client.hexists('cpuInfo','user'):
    print(True)
else:
    print(False)

