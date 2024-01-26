import os
import win32com.client as win32
from functions import dibujar_mapa, paint_cell_rgb, key_pressed
from player import Player


# OBTENER LA RUTA DEL EXCEL (doc.xlsx)
py_path = os.path.dirname(__file__)
excelPath = os.path.join(py_path, 'doc.xlsx')


# ABRIR LA APLICACIÓN DE EXCEL
excel = win32.Dispatch("Excel.Application")
excel.Visible = True


# ABRIR EL DOCUMENTO Y OBTENER LA HOJA ACTIVA
workbook = excel.Workbooks.Open(excelPath)
sheet = workbook.ActiveSheet


# DEFINIR LAS DIMENSIONES DE NUESTRA PANTALLA
start_cell = sheet.Cells(1, 1)
end_cell = sheet.Cells(20, 20)
range_cells = sheet.Range(start_cell, end_cell)


# DEFINIR EL TAMAÑO DE LAS CELDAS
range_cells.ColumnWidth = 4
range_cells.RowHeight = 25


# DEFINIR ELEMENTOS PRINCIPALES ESTÁTICOS
finish_cell = sheet.Cells(3,21)
finish_cell.Value = "META"
paint_cell_rgb(finish_cell, (0,250,20))
sheet.Cells(9,21).Value = "[R] Reiniciar"
sheet.Cells(10,21).Value = "Puntaje:"
score_cell = sheet.Cells(10,22)
win_cell = sheet.Cells(11,21)


# FUNCIONES BÁSICAS
def init_game():
    score_cell.Value = 0
    win_cell.Value = ""
    win_cell.Interior.ColorIndex = None
    pos_cell = sheet.Cells(1, 1)
    dibujar_mapa(range_cells)
    paint_cell_rgb(pos_cell, (0,0,0))
    
    return Player(1, 1, 0), pos_cell

def move_valid(pos_y, pos_x):
    next_cell_color = sheet.Cells(pos_y, pos_x).Interior.Color
    # SI EL COLOR ES IGUAL A PARED O NEGRO NO ES VALIDO
    if not (next_cell_color == 4613170 or next_cell_color == 0):
        return True

def there_move(pos_y, pos_x, pos_cell):
    next_cell = sheet.Cells(pos_y, pos_x)
    if next_cell.Interior.Color != pos_cell.Interior.Color:
        paint_cell_rgb(next_cell, (250,0,0))
        return True


# INICIAR EL JUEGO
player, pos_cell = init_game()


# BUCLE PRINCIPAL
while True:
    
    # RECONOCIMIENTO DE TECLAS
    if key_pressed('up'):
        if player.pos_y > 1 and move_valid(player.pos_y-1, player.pos_x):
            player.pos_y -= 1
    
    elif key_pressed('down'):
        if player.pos_y < 20 and move_valid(player.pos_y+1, player.pos_x):
            player.pos_y += 1
        
    elif key_pressed('left'):
        if player.pos_x > 1 and move_valid(player.pos_y, player.pos_x-1):
            player.pos_x -= 1
        
    elif key_pressed('right'):
        if player.pos_x < 20 and move_valid(player.pos_y, player.pos_x+1):
            player.pos_x += 1
        
    elif key_pressed('r'):
        player, pos_cell = init_game()
        
    elif key_pressed('esc'):
        break
    
    # SI HAY MOVIMIENTO...
    if there_move(player.pos_y, player.pos_x, pos_cell):
        paint_cell_rgb(pos_cell, (0,0,0))
        pos_cell = sheet.Cells(player.pos_y, player.pos_x)
        
        # AUMENTA LA CUENTA DEL PUNTAJE
        player.score += 1
        score_cell.Value = player.score
        
        # SI LLEGÓ A LA META...
        if player.pos_x == 20 and player.pos_y == 3:
            win_cell.Value = "GANASTE!"
            paint_cell_rgb(win_cell, (0, 255, 20))