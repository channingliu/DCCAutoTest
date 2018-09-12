#coding:utf-8
import requests
import json


#封装requests请求
class MyHttpRequest(object):
    '''
     def __init__(self,url):
        self.url = url
    '''


    def get(self,url,**par):
        params = par.get("params")
        headers = par.get("headers")
        try:
            resp = requests.get(url=url,params=params,headers=headers,timeout = 3)
            text = resp.json()
            return text
        except Exception as e:
            print("get错误：s%" % e)

    def post(self,url,**par):
        params = par.get("params")
        headers = par.get("headers")
        data = par.get("data")
        json = par.get("json")
        files = par.get("files")
        try:
            resp = requests.get(url=url, params=params, headers=headers,data=data,json=json,files=files)
            text = resp.json()
            return text
        except Exception as e:
            print("post 错误：s%" % e)