import openpyxl as xl
book = xl.Workbook()
sheet = book.active

for y in range(1,51):
    for x in range(1,51):
        cell = sheet.cell(y,x)
        cell.value = cell.coordinate
book.save("test50.xlsx")



