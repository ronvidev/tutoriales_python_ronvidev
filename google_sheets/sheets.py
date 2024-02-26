import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",  # Obtener de google cloud
    scope,
)

client = gspread.authorize(creds)

# Abrir el documento
sheet = client.open("Ejemplo con Python").sheet1  # Por nombre de documento
# sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1Y0Jf5VdpVEZwnq7DOo8m2WxKqpossTQ4sWs6yhoYnBs").sheet1 # Por URL

# Abrir  hojas
# sheet = client.open("Ejemplo con Python").worksheet("Hoja 2") # Por nombre de hoja
# sheet = client.open("Ejemplo con Python").get_worksheet(1) # Por index de hoja

# Colocar valor en la celda C1
# sheet.update_cell(1, 3, "Hola desde Python")
# sheet.update_acell("C1", "Hola desde Python")

# Colocar valor en un rango de celdas
# for row in range(1, 6):
#     sheet.update_cell(row, 3, "Hola")

# cell_list = sheet.range('C1:C5')
# for cell in cell_list:
#     cell.value = 'Hola'

# cell_list_2 = sheet.range('D1:D5')
# for cell in cell_list_2:
#     cell.value = 'O_o'

# sheet.update_cells(cell_list+cell_list_2)

# Buscar una palabra
# cells = sheet.findall("Azul")
# for cell in cells:
#     print(cell.address)
#     formato = {
#         "backgroundColor": {
#             "red": 0.0,
#             "green": 1.0,
#             "blue": 0.0,
#         },
#         "textFormat": {"bold": True},
#     }
#     sheet.format(cell.address, formato)

# cell = sheet.find("Azul")
# print(cell.address)

# Obtener valores de una columna
# col_values = sheet.col_values(2)[1:]
# col_values = sheet.col_values(sheet.find("color").col)[1:]
# print(col_values)

# sheet.update_title("Tabla de colores")
