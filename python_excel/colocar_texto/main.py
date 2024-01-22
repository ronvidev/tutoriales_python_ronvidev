import os
import win32com.client

folder_path = r"F:\test"

for name_doc in os.listdir(folder_path):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True
    
    excel_path = os.path.join(folder_path, name_doc)
    
    workbook = excel.Workbooks.Open(excel_path)
    worksheet = excel.ActiveSheet
    
    worksheet.Cells(1,2).Value = "=TODAY()"
    
    nro_doc = os.path.splitext(name_doc)[0].split("_")[1]
    
    worksheet.Cells(2,2).Value = nro_doc
    
    worksheet.Cells(3,2).Value = "donde seas feliz :)"
    
    workbook.Save()
    
    workbook.Close()