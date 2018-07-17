import unittest
import requests,json,os
from ddt import ddt,data,unpack
from public.base import get_apiUrl
import pymysql
from public.read_csv import get_csv_test_data


#获取接口地址
testUrl = get_apiUrl("/ucenter/signUp")

#获取接口测试数据
testPath = os.path.dirname(os.path.dirname(__file__))+"\\api_test_data\\"
testCaseFile = testPath+"signUp_test_data.csv"
testData = get_csv_test_data(fileName=testCaseFile)


#获取smsKey
# smsKeyUrl = get_apiUrl("/sendSms")
# smsData = {"phone":"15108398537"}
# r = requests.post(url=smsKeyUrl,json=smsData)
# smsKey1 = r.json()["data"]["smsKey"]
# print(smsKey1)

@ddt
class signUp(unittest.TestCase):
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


    @data(*testData)
    @unpack
    def test_signUp(self,*testdata):
        print(testdata)
        testcase=testData["testcase"]
        expRes=testData["expRes"]
        testdata.pop("testcase")
        testdata.pop("expRes")

        r = requests.post(url=testUrl,json=testdata)
        result = r.json()
        try:
            (self.assertIn(expRes,result["msg"]))
        except AssertionError:
            print(" Fail-用例名称：",testcase,"\n"," 实际返回结果：",result,"\n"," 用例期望结果：",expRes,"\n")




if __name__ == '__main__':
    unittest.main()

