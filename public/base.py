from public import config
from public import questsMethod,read_excle
import time,datetime,requests
import os
from public import read_csv
def get_apiUrl(aipName):
    host = config.get_host()
    aipName = aipName
    url = ''.join([host,aipName])
    return url

def get_request_rsp(url,method,**params):
    if method == "get":
        rsp = questsMethod.MyHttpRequest().get(url, **params)
    if method == "post":
        rsp = questsMethod.MyHttpRequest().post(url, **params)
    return rsp

def get_excle_data(fileName,sheetName):
    dataInof = read_excle.XLDatainfo(fileName)
    Data = dataInof.get_sheetinfo_by_name(sheetName)
    return Data

def get_token():
    loginUrl = get_apiUrl("/ucenter/signIn")
    userinfo = {
        "username": "15108398537",
        "password": "Decheche@Admin###"
    }

    r = requests.post(url=loginUrl, json=userinfo)
    headers = r.headers
    token = "Bearer " + r.json()["data"]["access_token"]
    headers = {"Authorization": token}
    return token

def get_headers_with_token():
    loginUrl = get_apiUrl("/ucenter/signIn")
    userinfo = {
        "username": "15108398537",
        "password": "Decheche@Admin###"
    }

    r = requests.post(url=loginUrl, json=userinfo)
    headers = r.headers
    token = "Bearer " + r.json()["data"]["access_token"]
    headers = {"Authorization": token}
    return headers

def get_Client_headers():
    sendSmsUrl = get_apiUrl("/ucenter/sendSms")
    wxloginUrl = get_apiUrl("/ucenter/signUp")
    userPhone = {
        "phone": "15108398536"
    }
    h_header = get_headers_with_token()

    r = requests.post(url=sendSmsUrl, headers=h_header,json=userPhone)
    smsKey = r.json()["data"]["smsKey"]
    signinfo = {
        "phone":"15108398536",
        "smsCode":"123456",
        "smsKey":smsKey
    }
    r2 = requests.post(url=wxloginUrl,json=signinfo)
    header= {
        "Authorization":"Bearer "+r2.json()["data"]["access_token"]
    }
    r2.headers=header
    #r2.headers["Authorization"]="Bearer "+r2.json()["data"]["access_token"]

    return r2.headers


def get_data_time(value):
    format = '%Y-%m-%d %H:%M'
    #format = '%Y-%m-%d'
    # format = '%Y-%m-%d %H:%M:%S'
    # value 为时间戳值,如:1460073600.0
    value = time.localtime(value)
    dt = time.strftime(format, value)
    print(dt)
    return dt


def get_unix_time(dt):
    time.strptime(dt, '%Y-%m-%d %H:%M')
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M'))
    print(s)
    return s


get_data_time(1531909800)



