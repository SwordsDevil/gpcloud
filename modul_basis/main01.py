from modul_basis.totaliii.logAnalysis import logAnalysis

code =logAnalysis.codeAnalysis('../Day03/txtFile/access_log')
print(code)


variable = __import__('modul_basis.totaliii.logAnalysis.logAnalysis',fromlist=True)
code = input('code:')
if hasattr(variable,code):
    page = getattr(variable,code)
    codes = page('../Day03/txtFile/access_log')
    print(codes)