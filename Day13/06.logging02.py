#logging logger handlers formatters
#2019/08/21

import logging.handlers

#设置日志记录格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(pathname)s - %(message)s')

#设置处理器
# rowHandler = logging.FileHandler(filename='./error.log')
#根据时间切割
# timeHanlers = logging.handlers.TimedRotatingFileHandler(
#     filename='./error.log',
#     when='D',
#     interval=2,
#     backupCount=5
# )
#根据日志的大小切割
rotateHnaler = logging.handlers.RotatingFileHandler(
    filename='./error.log',
    maxBytes=5*1024*1024,
    backupCount=5
)

#设置处理器处理日志的格式和最低处理级别
rotateHnaler.setFormatter(formatter)
rotateHnaler.setLevel(logging.WARNING)

#设置记录器的名字，最低记录级别和添加处理器
logger = logging.getLogger()
logger.setLevel(logging.WARNING)
logger.addHandler(rotateHnaler)

logger.error('this is a cuowu')