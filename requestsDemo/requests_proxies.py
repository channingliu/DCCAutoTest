#! /usr/bin/env python
#coding:utf-8

import requests

#使用代理
proxies={
    'http':'http://10.10.1.10:1234',
    'https':'https://10.10.1.10:2345'
}
requests.get('http://example.org',proxies=proxies)

#设置环境变量
'''
$ export HTTP_PROXY='http://10.10.1.10:1234'
$ export HTTPS_PROXY='https://10.10.1.10:2345'
$ python
request.get('http://example.org')
'''

#若你的代理需要使用 HTTP Basic Auth，可以使用 http:user:passwd@host/语法
proxies={'http://user:pass@10.10.1.10:1234'}

#要为某个特定的连接方式或主机设置代理，使用scheme：//hostname作为key，他会针对制定的主机和链接方式进行匹配
proxies={'http://10.2..1.128':'http://10.10.1.10:1234'}

#socks
proxies={
    'http':'socks5://user:pass@host:port',
    'https':'socks5://user:pass@host:port'
}