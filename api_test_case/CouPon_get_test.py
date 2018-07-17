import unittest
import requests,json,os
from ddt import ddt,data,unpack
from public.base import get_apiUrl,get_token,get_headers_with_token,get_Client_headers
import pymysql,time
from public.read_csv import get_csv_test_data

#获取接口地址与token
headers = get_headers_with_token()
c_headers = get_Client_headers()
aipUrl = get_apiUrl("/coupon/get")
testData = get_csv_test_data("CouPon_get_test_data.csv")

@ddt
class CouPon_get(unittest.TestCase):
    def setUp(self):
       pass

    def tearDown(self):
        pass

    def test_coupon_get_without_auth(self):
        response = requests.post(url=aipUrl, json=eval(testData[0][1]))
        result = response.json()
        self.assertEqual(result["msg"],"无效的token")

    # 客户端查询
    @data(*testData)
    @unpack
    def test_coupon_client_get(self,*testData):
        test_data = list(testData)
        datastr = test_data[1].replace("\n", "").strip()
        data = eval(datastr)
        response = requests.post(url=aipUrl, json=data,headers=c_headers)
        result = response.json()
        (self.assertIn(test_data[2], result["msg"]))

    #后台查询
    @data(*testData)
    @unpack
    def test_coupon_back_get(self, *testData):
        test_data = list(testData)
        datastr = test_data[1].replace("\n", "").strip()
        data = eval(datastr)
        response = requests.post(url=aipUrl, json=data, headers=headers)
        result = response.json()
        (self.assertIn(test_data[2], result["msg"]))



if __name__ == '__main__':
    unittest.main()

