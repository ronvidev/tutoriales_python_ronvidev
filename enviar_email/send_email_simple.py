import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import *

usuario = "Ronvidev"
asunto = "Mensaje enviado con Python"
destinatarios = ['']
mensaje = "Mensaje de prueba utilizando Python y Gmail"

# Crea la instancia del mensaje
msg = MIMEMultipart()
msg['From'] =  usuario
msg['Subject'] = asunto
msg['To'] = ', '.join(destinatarios)
msg.attach(MIMEText(mensaje))

# Crea la conexión y envía el correo
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(USER_MAIL, PASSWORD)
    server.sendmail(USER_MAIL, destinatarios, msg.as_string())
    print(f'Correo enviado.')
    