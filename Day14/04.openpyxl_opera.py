import openpyxl

excel = openpyxl.load_workbook('./fileExcel/grade.xlsx')
sheet = excel['abc']
# for i in range(2,11):
#     sheet['B' + str(i)] = i
sheet.append([1,2,3,4])
excel.save('./fileExcel/grade.xlsx')

