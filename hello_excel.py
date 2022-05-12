import openpyxl as excel
book = excel.Workbook()
sheet = book.active
sheet["A1"] = "こんにてゃ"
book.save("hello.xlsx")