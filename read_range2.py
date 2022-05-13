import openpyxl as xl
import datetime as dat
book = xl.load_workbook("test100.xlsx")
sheet = book.active


for row in sheet["A1:U5"]:
    r = []
    for cell in row:
        r.append(cell.value)
    print(r)
print(r)
