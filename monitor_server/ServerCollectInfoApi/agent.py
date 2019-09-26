from ServerCollect import GetInfo
import time
import subprocess

subprocess.run('mkdir -p /var/Server/monitor.log',shell=True)
GetInfo.intoLog('/var/Server/monitor.log')
