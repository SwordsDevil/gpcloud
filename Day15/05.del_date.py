import redis
import logging.config

logging.config.fileConfig('./logconfig.conf')
hashMap = input('input database and keys:')
pool = redis.ConnectionPool(host='192.168.40.142',port=6379)
client = redis.Redis(connection_pool=pool)

try:
    mapping = hashMap.split()
    for index in range(1,len(mapping)):
        if mapping[index] != 'system':
            client.hdel(mapping[0],mapping[index])
except Exception as  error:
    logging.getLogger('rotate')
    logging.error(error)
finally:
    print('Cached clear complete!')

print(client.hgetall('cpuInfo'))
