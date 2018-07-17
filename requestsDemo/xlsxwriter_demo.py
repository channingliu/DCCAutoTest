import xlsxwriter
import datetime

#创建Excel和sheet
workbook = xlsxwriter.Workbook("test_writer_excle.xlsx")
worksheet = workbook.add_worksheet("test")



#特定单元格写入
worksheet.write("A1","helloWorld")
worksheet.write(0,1,32)

#写入日期
worksheet.write(0,2,datetime.datetime.strptime("2018-11-11",'%Y-%m-%d'),workbook.add_format({'num_format':'yyyy-mm-dd'}))

#设置属性
worksheet.set_row(0,40) #设置行属性
worksheet.set_column('A:A',20) #设置列属

#插入图片
#worksheet.insert_image("A3",r"uploadTestFile.png",{'x_scale:0.2,"y_scale':0.2})

#批量写入
worksheet.write_column("A3",[1,2,3,4,])
worksheet.write_row("A4",[4,5,6,7,8])

workbook.close()