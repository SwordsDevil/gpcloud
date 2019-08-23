#log handle modul
#2019/08/21

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(pathname)s -%(message)s',
    datefmt='%a %Y-%m-%d %H:%M:%S',
    level = logging.WARNING,
    filename='./error.log',
    filemode='a'
)
logging.warning('this is a warning')