import xlwings as xw

wb1 = xw.Book('doc1.xlsx')
wb2 = xw.Book('doc2.xlsx')

sheet1 = wb1.sheets[0]
sheet2 = wb2.sheets[0]

resaltado = (250, 150, 0)

for celda1, celda2 in zip(sheet1.used_range, sheet2.used_range):
    if celda1.value != celda2.value:
        print(f"Diferencia en la celda: {celda1.address}")
        celda1.color = resaltado
        celda2.color = resaltado