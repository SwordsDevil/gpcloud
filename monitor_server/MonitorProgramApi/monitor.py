from LogOpera import transfer
from LogOpera import logAnalysis
from LogOpera import AlarmSystem

transfer.transfer('/root/.ssh/id_rsa','192.168.40.140','root')
transfer.execute('/root/.ssh/id_rsa','192.168.40.140','root')
logAnalysis.getLog
