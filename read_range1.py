import openpyxl as xl
import datetime as dat
book = xl.load_workbook("test100.xlsx")
sheet = book.active

r = []
for x in range(1,8):

    for y in range(2, 15):
        v = sheet.cell(row=y, column=x).value
        r.append(v)
print(r)
