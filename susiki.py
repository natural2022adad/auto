import openpyxl as xl
import datetime as dat
book = xl.Workbook()
sheet = book.active

t = dat.datetime.now()
sheet["A1"] = t.strftime('%Y年%m月%d日')
sheet["B1"] = '=TEXT(A1,"ggge年m月d日")'

book.save("susiki.xlsx")