import openpyxl as xl

book = xl.Workbook()
sheet = book.active

for y in range(1,101):
    for x in range(1,101):
        cell = sheet.cell(y,x)
        cell.value = cell.coordinate
book.save("test100.xlsx")