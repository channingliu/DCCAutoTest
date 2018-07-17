#! /usr/bin/env python
#coding:utf-8

import requests
import json


host = "https://httpbin.org/"
testApi='post'
url= ''.join([host,testApi])
params={'show_env':1}


file1={'file':open('uploadTestFile.txt','rb')} #普通上传
file2={'file':('EditName',open('uploadTestFile.txt','rb'))} #上传后修改文件名
file3={'file':('test.png',open('uploadTestFile.png','rb'),'image/png',{'refer':'localhost'})} #设置文件名，格式，header
file4=[
    ('file1',('test1.txt',open('uploadTestFile.txt','rb'))),
    ('file2',('test2.txt',open('uploadTestFile2.txt','rb')))
] #上传多个文件

#上传文件
r=requests.post(url=url,files=file4)
print(r.text)

#流式上传(通过二进制上传)
with open("uploadTestFile.txt")as f:
	r2=requests.post(url,data=f)

print(r2.json())
