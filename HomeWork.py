from openpyxl import Workbook, load_workbook

wb = load_workbook('C:\\Users\\FX505DT\\Desktop\\my1.csv')
ws = wb.active
print(ws)