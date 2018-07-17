import xlrd

class XLDatainfo(object):
    def __init__(self,fileName):
        self.workbook = xlrd.open_workbook(fileName)

    def get_sheetinfo_by_name(self,sheetName):
         self.sheet = self.workbook.sheet_by_name(sheetName)
         return self.get_sheet_info()

    def get_sheet_info(self):
        infoList=[]
        for row in range(1,self.sheet.nrows):
            info = self.sheet.row_values(row)
            info1 = info[1:-1]
            infoList.append(info1)
        return infoList

if __name__ == "__main__":
    datainfo = XLDatainfo(r'D:\PycharmProjects\DCCAutoTest\api_test_data\Student.xlsx')
    allData = datainfo.get_sheetinfo_by_name("Sheet1")
    print(allData)