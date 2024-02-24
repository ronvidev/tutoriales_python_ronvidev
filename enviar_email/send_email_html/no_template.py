import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from bs4 import BeautifulSoup
from credentials import *

usuario = "Ronvidev [desde Python]"
asunto = "Mensaje enviado con Python"
destinatarios = ["villarrealronald1@gmail.com"]

# Creamos el cuerpo del mensaje en HTML
html = BeautifulSoup(features="html.parser")
p = html.new_tag("p")
p['style'] = 'color: red; font-size: 16px;'
p.string = "Este es un mensaje de prueba usando HTML."
html.append(p)
img = html.new_tag("img", src="cid:firma_id", alt="Firma")
img['style'] = 'width: 250px'
html.append(img)
html_string = html.prettify()

# Creamos la instancia del mensaje
msg = MIMEMultipart()
msg["From"] = usuario
msg["Subject"] = asunto
msg["To"] = ", ".join(destinatarios)
msg.attach(MIMEText(html_string, "html"))

# Agregamos la firma al mensaje
with open("firma.png", "rb") as imagen:
    firma = MIMEImage(imagen.read(), name="firma.png")
    firma.add_header("Content-ID", "<firma_id>")
    msg.attach(firma)

# Crea la conexión y envía el correo
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(USER_MAIL, PASSWORD)
    server.sendmail(USER_MAIL, destinatarios, msg.as_string())
    print(f"Correo enviado.")
