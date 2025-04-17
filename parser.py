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
            <link href="https://fonts.googleapis.com/css2?family=PT+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap">
            <style>
                body {{
                    font-family: "PT Sans", sans-serif;
                    margin: 40px;
                    background-color: #DEDBD2; 
                    color: #4313839; 
                }}

                header {{
                    background-color: #EDAFB8;
                    color: #7C6A0A;
                    padding: 20px;
                    text-align: center;
                    margin-bottom: 30px;
                }}

                article {{
                    background-color:  #F7E1D7;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                    margin-bottom: 20px;
                }}

                footer {{
                    background-color: #4A5759;
                    color: #F7E1D7;
                    text-align: center;
                    padding: 10px;
                    margin-top: 40px;
                }}

                h1, h4{{
                    margin-top: 0;
                    color:#6F2732
                }} 
                
                h2 {{
                    margin-top: 0;
                    color: #F58D9D;
                }}

                hr {{
                    border: none;
                    height: 1px;
                    background-color: #F1EDDF;
                    margin-top: 10px;
                }}
            </style>
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

