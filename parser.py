import webbrowser
import os
from datetime import datetime

class ParserHtml:
    #inicializacion
    def __init__(self, articulos):
        self.articulos = articulos

    def generar_html(self, nombre_archivo="articulos.html"):
        #fecha actual
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        cuerpo = ""
        for titulo, autor, texto in self.articulos:
            if not titulo.strip() or not autor.strip() or not texto.strip():
                continue
            autor_normalizado = ' '.join(autor.strip().title().split())
            cuerpo += f"""
            <article>
                <h2>{titulo.strip()}</h2>
                <h4>Por {autor_normalizado}</h4>
                <p>{texto.strip()}</p>
            </article>
            <hr>
            """
        html_completo = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Nuestros Artículos Periodísticos</title>
        </head>
        <body>
            <h1>Artículos Disponibles</h1>
            {cuerpo if cuerpo else "<p>No hay artículos válidos para mostrar.</p>"}
            <footer>
                <p>Generado el {fecha}</p>
            </footer>
        </body>
        </html>
        """
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(html_completo)
        ruta_absoluta = os.path.abspath(nombre_archivo)
        webbrowser.open(f"file://{ruta_absoluta}")
        
        print(f"Archivo HTML generado correctamente: {nombre_archivo}")

