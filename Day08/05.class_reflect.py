#reflect
#2019/08/14

class Webopera:

    def __init__(self,url,token):
        self.url = url
        self.token = token

    def login(self):
        print('{}/{} login page'.format(self.url,self.token))

    def logout(self):
        print('{}/{} logout page'.format(self.url,self.token))

    @staticmethod
    def welcome(content):
        print('''welcome to webopera
        {}'''.format(content))

web = Webopera('www.baidu.com','login')
print(hasattr(web,'url'))

print(getattr(web,'token'))

setattr(web,'content','complete')
print(web.content)

url = input('请输入url:')
token = input('请输入token:')
web = Webopera(url=url,token=token)
if hasattr(web,token):
    func = getattr(web,token)
    if token == 'welcome':
        func('123')
    else:
        func()
else:
    print('fatal!')
