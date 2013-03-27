# -*- coding: utf-8 -*-
from time import localtime,strftime
hourDig     = int(strftime("%H", localtime()))
minuteDig   = int(strftime("%M", localtime()))
workHour    = 7<hourDig<11 or 13<hourDig<17 or 18<hourDig<21
workMinute  = 0<=minuteDig<60
timeFlag    = not(workHour and workMinute)

hostsFile   = open(r"C:\Windows\System32\drivers\etc\hosts")
hostsList   = hostsFile.readlines()
hostsFile.close()

statusTime  = ['#work time','#rest time']
statusLabel = ['#work label','#rest label']
setIP       = {'renren':['0.0.0.0','#0.0.0.0'],
               'weibo' :['0.0.0.0','#0.0.0.0'],
               'tieba' :['0.0.0.0','#0.0.0.0'],
               'acfun' :['0.0.0.0','#0.0.0.0'],
              }

import re
findLabel   = [re.compile(r'#work label').search,re.compile(r'#rest label').search]
findURL     = {'renren':re.compile(r'www\.renren\.com').search,
               'weibo' :re.compile(r'weibo\.com').search,
               'tieba' :re.compile(r'tieba\.baidu\.com').search,
               'acfun' :re.compile(r'www\.acfun\.tv').search,
              }

if not (hostsList[0] == statusTime[timeFlag]):
    hostsList[0] = statusTime[timeFlag]+'\n'
    for i,hostsLine in enumerate(hostsList):
        if findLabel[not timeFlag](hostsLine):
            data = re.sub(statusLabel[not timeFlag],statusLabel[timeFlag],hostsLine)
            for key,value in findURL.items():
                if value(hostsLine):
                    data = re.sub(setIP[key][not timeFlag],setIP[key][timeFlag],data)
            hostsList[i] = data
        else:
            pass
else:
    pass

hostsFile   = open(r'C:\Windows\System32\drivers\etc\hosts', 'w')
hostsFile.write(''.join(hostsList))
hostsFile.close()
