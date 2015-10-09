from openpyxl import load_workbook

#point to the file to be read. Intuitive.
wb2 = load_workbook('sample-input.xlsx')

#convince your self that sheet names are retireved.
sheet_names = wb2.get_sheet_names()
print sheet_names

#work book is simply a list of sheets
sheet = wb2[sheet_names[0]]
print sheet

print "can iterate sheets, rows and columns intuitively"
for sheet in wb2:
   for row in sheet.rows:
      for cell in row:
         if None!=cell.value:
            print cell.value
