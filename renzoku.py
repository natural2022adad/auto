import openpyxl as xl
book = xl.Workbook()
sheet = book.active

for i in range(1,21):
    for j in range(1,21):
        cell = sheet.cell
    sheet.cell(row=3, column=(h+1), value=(h+1))
book.save("renzoku3.xlsx")



