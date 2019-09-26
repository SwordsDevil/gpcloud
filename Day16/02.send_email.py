import yagmail

sendClient = yagmail.SMTP(
    user='SwordsDevil@163.com',
    password='cwb0908',
    host='smtp.163.com'
)

contents = [
    'this is test message.'
]
sendClient.send(
    to=['274262321@qq.com','dreamtomeandyou@gmail.com'],
    subject='[python]test',
    contents=contents,
    # attachments=[]
)
