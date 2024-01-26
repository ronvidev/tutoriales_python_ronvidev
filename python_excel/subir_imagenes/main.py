import os
import win32com.client

#################################################################
# OBTENER LAS RUTAS
#################################################################

py_path = os.path.dirname(__file__)
excelPath = os.path.join(py_path, 'doc.xlsx')
photosPath = os.path.join(py_path, 'fotos')

#################################################################
# INICIALIZAR EXCEL Y ABRIR DOCUMENTO
#################################################################

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True  # (False) para ejecutar en segundo plano

workbook = excel.Workbooks.Open(excelPath)
worksheet = workbook.ActiveSheet

#################################################################
# OBTENER LAS CELDAS PARA COLOCAR LAS FOTOS
#################################################################

num_rows = worksheet.UsedRange.Rows.Count
num_cols = worksheet.UsedRange.Columns.Count

photo_cells = {}
for row in range(1, num_rows + 1):
    for col in range(1, num_cols + 1):
        cell_value = worksheet.Cells(row, col).Value

        if cell_value and "foto" in str(cell_value).lower():
            cell_direction = worksheet.Cells(row + 1, col).Address
            photo_cells[cell_value] = cell_direction

# {'FOTO 1': 'A2', 'FOTO 2': 'C2', 'FOTO 3': 'A5', 'FOTO 4': 'C5'}

#################################################################
# COLOCAR LAS FOTOS EN LAS CELDAS OBTENIDAS
#################################################################

for name, cell in photo_cells.items():
    img_path = rf"{photosPath}\{name}.png"
    worksheet.Shapes.AddPicture(
        img_path,
        False,
        True,
        worksheet.Range(cell).Left,
        worksheet.Range(cell).Top,
        worksheet.Range(cell).Width,
        worksheet.Range(cell).Height,
    )

#################################################################
# GUARDAR Y CERRAR EXCEL
#################################################################

workbook.Save()
workbook.Close()

#################################################################
# DEVOLVER MENSAJE DE CONCLUSIÓN A FLUTTER
#################################################################

print("Listo!")
