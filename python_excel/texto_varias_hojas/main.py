import os
import win32com.client

py_path = os.path.dirname(os.path.realpath(__file__))
excel_path = os.path.join(py_path, 'doc.xlsx')

excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True

workbook = excel.Workbooks.Open(excel_path)

for sheet in workbook.sheets:
    sheet.Cells(5,4).Value = sheet.name

# workbook.Save()

# workbook.Close()

# excel.Quit()