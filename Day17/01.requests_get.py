import requests
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s -%(levelname)s - %(pathname)s - %(message)s',
    datefmt='%Y%m%d%H%M%S',
    level=logging.DEBUG,
    filename='./website.log',
    filemode='a'
)

website = ('www.baidu.com','www.43s99s.com','www.alisysun.com',
           'www.douban.com','news.baidu.com')

for urls in website:
    try:
        response = requests.get(url='http://{}'.format(urls), timeout=0.3)
        if response.status_code in [code for code in range(200,210)]:
            logging.info('{} check successfuly,status_code is {}'.format(urls,response.status_code))
        elif response.status_code in [code for code in range(400,410)] or response.status_code in [code for code in range(500,510)]:
            logging.error('{} check failed, status_code: {}, timeout None'.format(urls, response.status_code))
    except requests.exceptions.ConnectTimeout as error:
        logging.error(error)
    except requests.exceptions.ConnectionError as error:
        logging.error(error)
    except requests.exceptions.BaseHTTPError as error:
        logging.error(error)
