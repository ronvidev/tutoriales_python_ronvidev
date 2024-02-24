import win32com.client
import os

# Abrir la aplicación Word
word_app = win32com.client.Dispatch("Word.Application")
word_app.Visible = True

# Abrir el documento
doc = word_app.Documents.Open(os.path.abspath("archivo.docx"))

# Reemplazar texto
word_to_replace = "María"
replacement_word = "Ronald"

doc.Content.Find.Execute(
    FindText=word_to_replace,
    MatchCase=False,
    MatchWholeWord=False,
    MatchWildcards=False,
    MatchSoundsLike=False,
    MatchAllWordForms=False,
    Forward=True,
    Wrap=1,
    Format=True,
    ReplaceWith=replacement_word,
    Replace=2,
)

# Agregar título
titulo = "Ejemplo con Python\n"
doc.Range().InsertBefore(titulo)
rango_texto = doc.Range(0, len(titulo))
rango_texto.Font.Size = 24
rango_texto.Font.Bold = True

# Agregar texto final
texto_final = "\n\nHecho con Python"
doc.Range().InsertAfter(texto_final)
texto_completo = doc.Range().Text
rango_texto = doc.Range(len(texto_completo) - len(texto_final), len(texto_completo))
rango_texto.Font.Size = 12
rango_texto.Font.Color = 8421504


# doc.Save()
# word_app.Quit()
