import openpyxl as xl
import datetime as dat
book = xl.load_workbook("uriage.xlsx")
sheet = book.active

rows = sheet["A1:F9"]
for row in rows:
    values = [cell.value for cell in row]
    print(values)

#全データ取得
it = sheet.iter_rows()
for row in it:
    r = []
    for cell in row:
        r.append(cell.value)
    print(r)
