#! /usr/bin/env python
#coding:utf-8

import requests
import json

#方法1：basic认证（采用base64加密方法）
r = requests.get(url="https://httpbin.org/basic-auth/user/passwd",auth=('user','passwd'))
print('Basic:',r.text)

#方法2:HTTPBasicAuth
from requests.auth import HTTPBasicAuth

r1 = requests.get(url="https://httpbin.org/basic-auth/user/passwd",auth=HTTPBasicAuth('user','passwd'))
print('HTTPBasicAuth',r1.text)

#方法3：HTTPDigestAuth(MD5加密)
from requests.auth import HTTPDigestAuth
r2 = requests.get(url="https://httpbin.org/digest-auth/auth/user/passwd/MD5",auth=HTTPDigestAuth('user','passwd'))
print('HTTPDigestAuth',r2.text)

#方法4：（第三方认证，比如token）
'''
headers = {'Authorization':'token 23kklkdfd12312312'}
r = requests.get(url,headers=headers)
'''
