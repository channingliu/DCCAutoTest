#! /usr/bin/env python
#coding:utf-8

import requests
import json



host = "https://httpbin.org/"
testApi='post'
url= ''.join([host,testApi])
params={'show_env':1}
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, sdch, br","Accept-Language":"zh-CN,zh;q=0.8","Connection":"close","Cookie":"__guid=147723374.3219379882251579000.1527044426654.9976; monitor_count=1; _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1","Host":"httpbin.org","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
form_data={"a":"权哥软件测试","b":"form-data"}
json_data={"info":{"code":"1","sex":"男","id":100,"name":"quanquan"},
           "code":1,
           "name":"liuquan",
           'sex':'man',
           'data':[{"code":"1","sex":"男","id":100,"name":"quanquan"},{"code":"2","sex":"女","id":100,"name":"一羡"}],
           'id':1900
           }

#传递表单form-data
r=requests.post(url,params=params,data=form_data)
print(r.json()["form"])

#传递json(body-data)
r2=requests.post(url=url,json=json_data) #方法2：request.post(url=url,data=json.dumps(json_data))
print(r2.text)