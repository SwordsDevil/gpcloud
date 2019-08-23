# from modul_basis.totaliii.logAnalysis import logAnalysis
#
# ips = logAnalysis.ipsAnalysis('../../Day03/txtFile/access_log')
# print(ips)

variable = __import__('modul_basis.totaliii.logAnalysis.logAnalysis',fromlist=True)
userInfo = input('input:')
if hasattr(variable,userInfo):
    ips = getattr(variable,userInfo)
    print(ips('../../Day03/txtFile/access_log'))

