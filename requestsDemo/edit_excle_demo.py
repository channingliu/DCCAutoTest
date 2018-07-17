import xlrd
import xlutils.copy
import xlutils3.copy

xl = xlrd.open_workbook('test_writer_excle.xlsx')

workbook = xlutils.copy.copy(xl)

worksheet = workbook.get_sheet(0)

worksheet.write(0,0,"hello")

workbook.save(r"test_edit_excle.xls") #只支持xls格式