import unittest
import requests,json,os
from ddt import ddt,data,unpack
from public.base import get_apiUrl,get_headers_with_token
import pymysql,time
from public.read_csv import get_csv_test_data



#获取接口地址
aipUrl = get_apiUrl("/coupon/add")

#获取接口测试数据
testData = get_csv_test_data("CouPon_add_test_data.csv")


#获取带token的header
headers = get_headers_with_token()


@ddt
class CouPon_add(unittest.TestCase):
    def setUp(self):
        pass
    #     self.db = pymysql.connect(
    #         host="cd-cdb-4xk2jt1c.sql.tencentcdb.com",
    #         port=63874,
    #         user="db_testing",
    #         password="Dcc@TeSting#123",
    #         database="ucenter_dev")
    #     self.cursor = self.db.cursor()


    def tearDown(self):
        pass
        # self.setUp()
        # sql = "delete from user where username = '15108398537';"
        # try:
        #     # 执行sql语句
        #     self.cursor.execute(sql)
        #     self.db.commit()
        # except:
        #     # 发生错误时回滚
        #     self.db.rollback()
        # self.db.close()

    def test_coupon_add_withno_token(self):
        test_data = list(testData[0])
        datastr = test_data[1].replace("\n", "").strip()
        data = eval(datastr)
        response = requests.post(url=aipUrl, json=data, headers=headers)
        result = response.json()
        try:
            (self.assertIn(test_data[2], result["msg"]))
        except AssertionError:
            print(" Fail-用例名称：", test_data[0], "\n", "测试参数：", datastr, "\n", " 实际返回结果：", result, "\n", " 用例期望结果：",
                  test_data[2], "\n")


    @data(*testData)
    @unpack
    def test_coupon_add(self,*testData):
        test_data = list(testData)
        datastr = test_data[1].replace("\n", "").strip()
        data = eval(datastr)
        response = requests.post(url=aipUrl, json=data,headers=headers)
        result = response.json()
        try:
            (self.assertIn(test_data[2], result["msg"]))
        except AssertionError:
            print(" Fail-用例名称：", test_data[0], "\n","测试参数：",datastr,"\n", " 实际返回结果：", result, "\n", " 用例期望结果：", test_data[2], "\n")
        time.sleep(1)




if __name__ == '__main__':
    unittest.main()

