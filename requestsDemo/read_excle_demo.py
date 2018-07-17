import xlrd,os

path = os.chdir(r'E:/PycharmProjects/DCCAutoTest/api_test_data')
fileName = 'Student.xlsx'
file= os.path.join(os.getcwd(),fileName) #os.getcwd() 方法用于返回当前工作目录。

# 1. 打开文件
workbook = xlrd.open_workbook(file,"r")

#2. 获取sheet
print(workbook.sheet_names()) #获取sheet name
print(workbook.nsheets)# 获取sheet 个数
print(workbook.sheets()) #获取sheet 对象
print(workbook.sheet_by_name("Sheet1"))
print(workbook.sheet_by_index(0))

#3.获取sheet中的数据
table1 = workbook.sheet_by_name("Sheet1")
print(table1.name)
print(table1.nrows)
print(table1.ncols)

#4.单元格批量获取
print(table1.row_values(0)) #获取第一行，合并单元格，首行显示值，其他行为空
print(table1.row_values(0,2,3)) #获取第一行的第3列
print(table1.col_values(0))
print(table1.row_types(0)) #获取值类型

#5后去单元格的值
print(table1.cell_value(2,1))


#6常用技巧（0,0）转换为A
print(xlrd.cellname(0,1))

#7.获取表哥内不同的类型的name
print(table1.cell_type(2,1)) #值类型

