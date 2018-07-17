import unittest
import requests,json,os
from ddt import ddt,data,unpack
from public.base import get_apiUrl,get_token,get_headers_with_token
import pymysql,time
from public.read_csv import get_csv_test_data

#获取接口地址与token
headers = get_headers_with_token()
aipUrl = get_apiUrl("/coupon/delete")
conpoAddUrl = get_apiUrl("/coupon/add")
testData = get_csv_test_data("CouPon_delete_test_data.csv")

couponData = {
  "amount": 100,
  "description": "接口优惠券",
  "expiredDay": 0,
  "expiredType": 1,
  "limitMinAmount": 100,
  "limitPerOrder": 1,
  "limitProductType": 1,
  "limitUserQuantity": 2,
  "mark": "asdfasdfassdfasdasdfasdfasdasdfaa",
  "mutex": "false",
  "name": "接口删除",
  "quantity": 100,
  "status": 1
}



#新增测试优惠券并获取id
r2 = requests.post(url=conpoAddUrl,json=couponData,headers=headers)
id= r2.json()["data"]["id"]

deleteId = {
    "id":id
}


@ddt
class CouPon_delete(unittest.TestCase):

    def test_coupon_delete1(self):
        response = requests.post(url=aipUrl, json=deleteId,headers=headers)
        result = response.json()
        self.assertEqual(result["msg"],"success")

    def test_coupon_delete1_without_auth(self):
        response = requests.post(url=aipUrl, json=deleteId)
        result = response.json()
        self.assertEqual(result["msg"],"fail")


    @data(*testData)
    @unpack
    def test_coupon_delete2(self,*testData):
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

    def setUp(self):
        self.db = pymysql.connect(
            host="cd-cdb-4xk2jt1c.sql.tencentcdb.com",
            port=63874,
            user="db_testing",
            password="Dcc@TeSting#123",
            database="coupon_dev")
        self.cursor = self.db.cursor()

    def tearDown(self):
        #self.setUp()
        sql = "select id from coupon where name like '%接口删除%';"
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            rs = self.cursor.fetchone()
            sql1 = "delete from coupon where id in %s;" % rs
            self.cursor.execute(sql1)
            self.db.commit()

        except:
            # 发生错误时回滚
            self.db.rollback()
        self.db.close()
        time.sleep(1)



if __name__ == '__main__':
    unittest.main()

