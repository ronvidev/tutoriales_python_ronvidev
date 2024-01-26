import keyboard

def dibujar_mapa(cell):
    campo = [
        [0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1],
        [1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0],
        [1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,1],
        [0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,0,0,0],
        [1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,1,0],
        [1,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0],
        [1,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1],
        [0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,0,0],
        [1,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1],
        [0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1],
        [1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0],
        [1,0,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0],
        [0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0],
        [1,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,1],
        [1,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0],
        [0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1],
        [1,1,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,1,0],
        [1,0,0,1,1,0,1,0,1,0,0,1,0,0,0,0,1,1,1,0],
    ]
    
    paint_cell_rgb(cell, (50, 200, 100))
    
    for i in range(len(campo)):
        for j in range(len(campo[0])):
            if campo[i][j] == 1:
                red, green, blue = (50,100,70)
                cell.Offset(i+1, j+1).Interior.Color = (blue << 16) + (green << 8) + red

def paint_cell_rgb(cell, rgb):
    red, green, blue = rgb
    cell.Interior.Color = (blue << 16) + (green << 8) + red

teclas_presionadas = {
    'up': False,
    'down': False,
    'left': False,
    'right': False,
    'esc': False,
    'r': False,
}

def key_pressed(key):
    if keyboard.is_pressed(key) and not teclas_presionadas[key]:
        teclas_presionadas[key] = True
        return True
        
    elif not keyboard.is_pressed(key):
        teclas_presionadas[key] = False
        return False



