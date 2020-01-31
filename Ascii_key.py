#!/usr/bin/python
#-*- coding:utf-8 -*-
#python 2.7
import sys
import time
import urllib
#Email：758682207@qq.com
f = raw_input('\nAscii:')
lf = len(f)
print u"\n密文为：",f
print u'\n检测到长度为：',lf
x = 0
lis = []
def asc():
    global f,x,lf
    try:
        for y in range(0,lf):
            if int(f[x:x+2]) in range(36,127):
                # print chr(int(f[x:x + 2]))
                lis.append(chr(int(f[x:x + 2])))
                x = x + 2
                lf = lf - 2
                if lf==0:
                    break
            elif int(f[x:x + 3]) in range(48,58) or range(97,127):
                # print chr(int(f[x:x + 3]))
                lis.append(chr(int(f[x:x + 3])))
                x = x + 3
                lf = lf - 3
                if lf == 0:
                    break
    except:
        print ''
asc()
lis = "".join(lis)
lis = urllib.unquote(lis)
print u"\n解密为：",lis
print u"\n十秒后自动退出"
time.sleep(10)
sys.exit()