import csv
import os

def get_csv_test_data(fileName):
    testCasePath = os.path.dirname(os.path.dirname(__file__)) + "/api_test_data/"
    testCaseFile = testCasePath + fileName
    csv_reader = csv.reader(open(testCaseFile))
    testData=[]
    for row in csv_reader:
        #info = row[1:]
        testData.append(row)
    testData.pop(0)
    return testData

def get_csv_exp_res(fileName):
    csv_reader = csv.reader(open(fileName,encoding="utf-8"))
    expRes=[]
    for row in csv_reader:
        info = row[-1]
        expRes.append(info)
    expRes.pop(0)
    return expRes

def get_csv_test_case(fileName):
    csv_reader = csv.reader(open(fileName))
    testCase=[]
    for row in csv_reader:
        info = row[0]
        testCase.append(info)
    testCase.pop(0)
    return testCase


# testCaseFile = r'D:\PycharmProjects\DCCAutoTest\api_test_data\signUp_test_data.csv'
# print(get_csv_test_data(fileName=testCaseFile))