import openpyxl

excel = openpyxl.load_workbook('./fileExcel/abc.xlsx')
sheet = excel['Sheet']
# sheet['A1'] = "123"
sheet.append(['1',2,3,4])
excel.save('./fileExcel/abc.xlsx')