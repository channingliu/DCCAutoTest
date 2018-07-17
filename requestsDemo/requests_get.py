#! /usr/bin/env python
#coding:utf-8

import requests
import json

'''
Request 常见http请求方法：
requests.get(‘https://github.com/timeline.json’) #GET请求
requests.post(“http://httpbin.org/post”) #POST请求
requests.put(“http://httpbin.org/put”) #PUT请求
requests.delete(“http://httpbin.org/delete”) #DELETE请求
requests.head(“http://httpbin.org/get”) #HEAD请求
requests.options(“http://httpbin.org/get”) #OPTIONS请求

'''

host = "https://httpbin.org/"
testApi='get'
url= ''.join([host,testApi])
params={'show_env':1}
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, sdch, br","Accept-Language":"zh-CN,zh;q=0.8","Connection":"close","Cookie":"__guid=147723374.3219379882251579000.1527044426654.9976; monitor_count=1; _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1","Host":"httpbin.org","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

#无参数请求
r=requests.get(url)

print(r.url) #返回请求的url
print(r.status_code) #返回响应状态码
print(r.reason) #返回状态码具体解释
print(r.text)#字符串方式的响应体（Unicode型数据），主要取文本，会自动根据响应头部的字符编码进行解码
print(r.content)#字节方式的响应体，bytes型，二进制数据，取图片文件等。会自动为你解码 gzip 和 deflate 压缩
print(r.raw)#返回原始响应体(对象内存的中的位置)
print(r.json())#Requests中内置的JSON解码器
print(r.headers)#以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
print(r.encoding)#获取网页编码
print(r.raise_for_status())#失败请求(非200响应)抛出异常
print(r.request.method) #返回请求方法
print(r.cookies) #返回RequestCookieJar[]


#带参数请求
r2= requests.get(url,params=params)
print(r2.json())

#待heades请求
r3 = requests.get(url,params=params,headers=headers)
print(r3.json()["headers"]["User-Agent"])

r4 = requests.get(url)
print(r4.headers)