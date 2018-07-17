#! /usr/bin/env python
#coding:utf-8

import requests
import json

host = "https://httpbin.org/"
testApi='cookies/set/sessioncookie/123456789'#设置session
url= ''.join([host,testApi])
url1='https://httpbin.org/cookies' #此url的cookies为空

'''
访问url1是没有cookies的，访问url是设置cookies，
下面讲解如何通过访问url1获取cookies
'''
#保持会话的步骤
session = requests.Session() #初始化一个session对象
session.get(url) #cookies的信息存在了session中
r=session.get(url=url1)
print(r.json())

#通过session保存一些回话信息(如下添加headers)
header1 = {'test1':'aa'}
header2= {'test2':'bb'}
session1 = requests.Session()
session1.headers.update(header1)
r2 = session1.get(url="https://httpbin.org/headers",headers=header1)
print(r2.json())

#删除信息（直接设置值为None）
session1.headers['test1']=None
r3 = session1.get(url="https://httpbin.org/headers",headers=header2)
print(r3.text)