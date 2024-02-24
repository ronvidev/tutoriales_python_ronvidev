import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Usa las credenciales para autorizar tu cuenta
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Abre el Google Sheets con la URL
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1BUk6cl5NRr8D5wgPReQfeSCffovsYrddgxHRGNKTk9g/edit?usp=drive_link')

# Selecciona la hoja del documento
worksheet = sheet.get_worksheet(0)

# Ahora puedes editar la hoja de cálculo
worksheet.update_cell(1, 1, "Hola Mundo")
