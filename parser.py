import webbrowser
import os
from datetime import datetime
from collections import defaultdict

class ParserHtml:
    #inicializacion
    def __init__(self, articulos):
        self.articulos = articulos

    def generar_id(self,nombre):
        return nombre.lower().replace(" ", "-").replace("á", "a").replace("é", "e") \
                             .replace("í", "i").replace("ó", "o").replace("ú", "u") \
                             .replace("ñ", "n")

    def generar_html(self, nombre_archivo="articulos.html"):
        
        #fecha actual
        
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        #agrupa articulos por autor
        
        articulos_autor = defaultdict(list)
        for titulo, autor, texto in self.articulos:
            if not titulo.strip() or not autor.strip() or not texto.strip():
                continue
            autor_normalizado = ' '.join(autor.strip().title().split())
            articulos_autor[autor_normalizado].append((titulo.strip(), texto.strip()))

        
        #genera indice de autores con links
        
        indice = "<nav><h2>Índice de autores</h2><ul>"
        for autor in sorted(articulos_autor.keys()):
            autor_id = self.generar_id(autor)
            indice += f'<li><a href="#{autor_id}">{autor}</a></li>'
        indice += "</ul></nav><hr>"
        
        #genera secciones por autor
        
        cuerpo = ""
        for autor, articulos in articulos_autor.items():
            autor_id = self.generar_id(autor)
            cuerpo += f'<section id="{autor_id}">\n<h3>{autor}</h3>\n'
            for titulo, texto in articulos:
                cuerpo += f"""
                <article>
                    <h2>{titulo}</h2>
                    <p>{texto}</p>
                </article>
                <hr>
                """
            cuerpo += "</section>\n"
        
        #html completo con estilos
        
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
            <header>
                <h1>Articulos Disponibles</h1>
            </header>
            {indice}
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

