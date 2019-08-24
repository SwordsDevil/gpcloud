import redis

pool = redis.ConnectionPool(host='192.168.40.142',port='6379',db=0)
client = redis.Redis(connection_pool=pool)

client.hset('pycloud', 'user', 'phone')
info = client.hget('pycloud', 'user')
print(str(info, 'utf8'))