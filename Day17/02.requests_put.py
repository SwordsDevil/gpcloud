import requests
import json

token = 'adac656b42c272b2e62e5b4e1a0831e431b1bd8d7f23781160d6e856fd32cf3c'
api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)

header = {'Content-Type': 'application/json'}
data = {
    "msgtype": "text",
    "text": {
        "content": "测试发送测试信息至钉钉群"
    },
    'at': {
        'atMobiles': [
            '15779847379',
            '13153315260'
        ]
    },
    'isAtAll': False
}

sendData = json.dumps(data)
for i in range(3):
    requests.post(url=api, data=sendData, headers=header)
