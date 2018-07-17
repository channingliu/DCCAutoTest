import unittest
from ddt import ddt, data,unpack
from public.base import *
import pymysql
from public.read_csv import get_csv_test_data

#addCouponUrl = get_apiUrl("/coupon/add")
#grantCouponUrl = get_apiUrl("/coupon/grant")
takeCouponUrl = get_apiUrl("/coupon/take")
headers = get_headers_with_token()
cHeaders = get_Client_headers()
testData = get_csv_test_data("Coupon_take_test_data.csv")
print(cHeaders)
@ddt
class Coupon_take(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    @data(*testData)
    @unpack
    def test_takeCoupon(self,*testData):
        test_data = list(testData)
        datastr = test_data[1].replace("\n", "").strip()
        data = eval(datastr)
        response = requests.post(url=takeCouponUrl, json=data, headers=headers)
        result = response.json()
        try:
            (self.assertIn(test_data[2], result["msg"]))
        except AssertionError:
            print(" Fail-用例名称：", test_data[0], "\n", "测试参数：", datastr, "\n", " 实际返回结果：", result, "\n", " 用例期望结果：",
                  test_data[2], "\n")
        time.sleep(1)


