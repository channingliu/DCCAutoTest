import unittest
import requests,json,os
from ddt import ddt,data,unpack
from public.base import get_apiUrl,get_token,get_headers_with_token
import pymysql,time
from public.read_csv import get_csv_test_data

#获取接口地址与token
headers = get_headers_with_token()
aipUrl = get_apiUrl("/coupon/list")
testData = get_csv_test_data("CouPon_list_test_data1.csv")


@ddt
class CouPon_list(unittest.TestCase):
    def setUp(self):

        self.db = pymysql.connect(
            host="cd-cdb-4xk2jt1c.sql.tencentcdb.com",
            port=63874,
            user="db_testing",
            password="Dcc@TeSting#123",
            database="ucenter_dev")
        self.cursor = self.db.cursor()

    def tearDown(self):
        self.db.close()


    def test_coupon_grant_without_auth(self):
        response = requests.post(url=aipUrl, json=eval(testData[0][1]))
        result = response.json()
        self.assertEqual(result["msg"],"无效的token")

    @data(*testData)
    @unpack
    def test_coupon_get2(self,*testData):
        test_data = list(testData)
        datastr = test_data[1].replace("\n", "").strip()
        data = eval(datastr)
        response = requests.post(url=aipUrl, json=data,headers=headers)
        result = response.json()

        try:
        # 执行sql语句
            self.cursor.execute(test_data[2])
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

        try:
            (self.assertIn(test_data[2], result["data"]['pager']['itemCount']))
        except AssertionError:
            print(" Fail-用例名称：", test_data[0], "\n", "    测试参数：", datastr, "\n", " 实际返回结果：", result, "\n", " 用例期望结果：",
                  test_data[2], "\n")
        time.sleep(1)



if __name__ == '__main__':
    unittest.main()

