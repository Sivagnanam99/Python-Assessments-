from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sheet["A1"]="Siva"
sheet["A2"]="Surya"
sheet["A3"]="Venkat"
sheet["A4"]="Manickam"
sheet["A5"]="Nalini"


wb.save(filename="Python vs Xl .xlsx")
