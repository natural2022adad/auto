import openpyxl as xl
import datetime as dat
book = xl.load_workbook("wareki2.xlsx")
sheet = book.active

print(sheet["A58"].value)

cell = sheet.cell(row=58, column=2)
print(cell.value)
