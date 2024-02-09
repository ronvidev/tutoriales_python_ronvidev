import os
import win32com.client
import cv2
import time

py_path = os.path.dirname(__file__)
excelPath = os.path.join(py_path, 'doc.xlsx')
photosPath = r"F:\CarpetasW\Imágenes\WhatsApp"

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

workbook = excel.Workbooks.Open(excelPath)
sheet = workbook.ActiveSheet
cell = sheet.Cells(1, 1)
cell.ColumnWidth = 90.71 # 640
cell.RowHeight = 270 # 360

def print_frame(photo_path):
    # Imprimir el frame
    sheet.Shapes.AddPicture(
        photo_path,
        False,
        True,
        cell.Left,
        cell.Top,
        cell.Width,
        cell.Height,
    )
    
    # Borrar el frame anterior
    if len(sheet.Shapes) > 1:
        sheet.Shapes[0].Delete()
        
# for foto in os.listdir(photosPath):
#     photo_path = os.path.join(photosPath, foto)
#     print_frame(photo_path)

video = cv2.VideoCapture(1)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while video.isOpened():
    init = time.time()
    # time.sleep(0.02)
    frame = video.read()[1]
    
    frame_path = os.path.join(py_path, f"frame.jpg")
    params = [cv2.IMWRITE_JPEG_QUALITY, 50]
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # cv2.COLOR_BGR2BGRA
    cv2.imwrite(frame_path, image, params) 
    
    print_frame(frame_path)
    end = time.time()
    print(round(1/(end-init), 2), "FPS")
    
    
    # cv2.imshow(f'a', frame)
    # if cv2.waitKey(10) & 0xFF == ord('q'):
    #     break
    
    
video.release()
cv2.destroyAllWindows()