#! /usr/bin/env python
#coding:utf-8

import requests
import json



host = "https://httpbin.org/"
testApi='cookies'
url= ''.join([host,testApi])
url1='http://www.baidu.com'

#获取cookies
r=requests.get(url=url1)
print(r.cookies) #获取cookies
d=requests.utils.dict_from_cookiejar(r.cookies) #将jar包转换字典
print(d)
#将jar包转化为字典，方法2
print({a.name:a.value for a in r.cookies})
#将jar包转化为元组
print(tuple(r.cookies))

#发送cookies到服务器
cookies={'cookies-name':'quanquan'}
r1=requests.get(url=url,cookies=cookies)
print (r1.text)

#发送cookies到服务器（常用）
s=requests.Session() #初始化一个session
c=requests.cookies.RequestsCookieJar() #初始化cookies
c.set('cookie-name','cookie-value',path='/',domain='.test.com') #设置cookies值
s.cookies.update(c) #发送cookies
print(s.cookies)