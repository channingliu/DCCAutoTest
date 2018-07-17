import unittest
import requests,json,os
from ddt import ddt,data,unpack
from public.base import get_apiUrl,get_token,get_headers_with_token
import pymysql,time
from public.read_csv import get_csv_test_data

#获取接口地址与token
headers = get_headers_with_token()
aipUrl = get_apiUrl("/coupon/status/save")
testData = get_csv_test_data("CouPon_status_save_test_data.csv")


@ddt
class CouPon_status_save(unittest.TestCase):
    def setUp(self):
       pass

    def tearDown(self):
        pass

    def test_coupon_status_save_without_auth(self):
        response = requests.post(url=aipUrl, json=eval(testData[0][1]))
        result = response.json()
        self.assertEqual(result["msg"],"无效的token")

    @data(*testData)
    @unpack
    def test_status_save(self,*testData):
        test_data = list(testData)
        datastr = test_data[1].replace("\n", "").strip()
        data = eval(datastr)
        response = requests.post(url=aipUrl, json=data,headers=headers)
        result = response.json()
        try:
            (self.assertIn(test_data[2], result["msg"]))
        except AssertionError:
            print(" Fail-用例名称：", test_data[0], "\n", "测试参数：", datastr, "\n", " 实际返回结果：", result, "\n", " 用例期望结果：",
                  test_data[2], "\n")
        time.sleep(1)



if __name__ == '__main__':
    unittest.main()

