import openpyxl as xl
book = xl.load_workbook("hello.xlsx")
sheet = book.worksheets[1]
cell = sheet['A1']
print(cell.value)
