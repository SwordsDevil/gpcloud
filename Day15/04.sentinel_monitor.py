import redis
import logging.config
from redis import sentinel

logging.config.fileConfig('./logconfig.conf')
stinel = sentinel.Sentinel([('192.168.40.142',26379)])

try:
    master = stinel.discover_master('mymaster')
    print(master)
except redis.sentinel.MasterNotFoundError as error:
    logging.getLogger('rotate')
    logging.error(error)
finally:
    master = stinel.discover_master('mymaster')
    if master != ('192.168.40.142',6380):
        logging.warning('master on {}'.format(master))
