import  logging.config

logging.config.fileConfig('./logconfig.conf')

logger = logging.getLogger('rotate')
logger.error('this is a error')
