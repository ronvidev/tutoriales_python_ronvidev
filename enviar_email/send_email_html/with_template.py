import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from jinja2 import Template
from credentials import *

usuario = "Ronvidev [desde Python]"
asunto = "Mensaje enviado con Python"
destinatarios = ["villarrealronald1@gmail.com"]

# Abrimos la plantilla
with open("template.html", "r") as file:
    template = Template(file.read())

# Le pasamos los argumentos
html = template.render(
    titulo="ESTE CORREO ES UN HTML",
    mensaje="Sígueme para más tutoriales :D",
    imgId="firma_id",
)

# Creamos la instancia del mensaje
msg = MIMEMultipart()
msg["From"] = usuario
msg["Subject"] = asunto
msg["To"] = ", ".join(destinatarios)
msg.attach(MIMEText(html, "html"))  # Especificamos el tipo de texto en HTML

# Agregamos la firma como documento interno (no adjunto)
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
