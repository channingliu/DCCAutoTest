import unittest,os,requests
from ddt import ddt,data,unpack
from public.read_csv import get_csv_test_data
from public.base import *

aa = get_Client_headers()

data={
    "couponid":190,
    "phone":"15108398536"
}

r = requests.post(url=get_apiUrl("/coupon/take"),headers = aa,json=data)

print(r.json())