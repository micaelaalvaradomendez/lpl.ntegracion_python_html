import webbrowser
import os
from datetime import datetime
from collections import defaultdict


#funcion global para def generar_id(self,nombre):
def generar_id(texto):
    return texto.lower().replace(" ", "-").replace("á", "a").replace("é", "e") \
                     .replace("í", "i").replace("ó", "o").replace("ú", "u") \
                     .replace("ñ", "n")

class Articulo:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo.strip()
        self.autor = ' '.join(autor.strip().title().split())
        self.texto = texto.strip()

class ParserHtml:
    def __init__(self, articulos):
        self.articulos = articulos

    def generar_html(self, nombre_archivo="index.html"):
        
        #fecha actual
        
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        # Crear carpeta para los artículos
        carpeta_articulos = "articulos"
        os.makedirs(carpeta_articulos, exist_ok=True)

        # Generacion de páginas individuales para cada artículo
        for articulo in self.articulos:
            if not articulo.titulo or not articulo.autor or not articulo.texto:
                continue
                
            id_articulo = generar_id(articulo.titulo)
            ruta_articulo = os.path.join(carpeta_articulos, f"{id_articulo}.html")
            
            with open(ruta_articulo, "w", encoding="utf-8") as f:
                f.write(f"""
                <!DOCTYPE html>
                <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <title>{articulo.titulo}</title>
                    <link href="https://fonts.googleapis.com/css2?family=PT+Sans&display=swap" rel="stylesheet">
                    <style>
                        body {{
                            font-family: "PT Sans", sans-serif;
                            margin: 40px;
                            background-color: #DEDBD2;
                            color: #4313839;
                        }}
                        article {{
                            background-color: #F7E1D7;
                            padding: 20px;
                            border-radius: 20px;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                            margin-bottom: 20px;
                            max-width: 800px;
                            margin: 0 auto;
                        }}
                        h1, h2 {{
                            color: #6F2732;
                        }}
                        a {{
                            color: #6F2732;
                            text-decoration: none;
                            font-weight: bold;
                        }}
                        a:hover {{
                            text-decoration: underline;
                        }}
                        .volver {{
                            display: inline-block;
                            margin-top: 20px;
                            padding: 8px 16px;
                            background-color: #EDAFB8;
                            border-radius: 4px;
                        }}
                    </style>
                </head>
                <body>
                    <article>
                        <h1>{articulo.titulo}</h1>
                        <p><strong>Autor:</strong> {articulo.autor}</p>
                        <div>{articulo.texto.replace('\n', '<br>')}</div>
                        <a class="volver" href="../{nombre_archivo}">← Volver al inicio</a>
                    </article>
                    <footer>
                        <p>Pagina generada el {fecha}</p>
                    </footer>
                </body>
                </html>
                """)

        # Agrupacion de artículos por autor para el índice
        articulos_por_autor = defaultdict(list)
        for articulo in self.articulos:
            if not articulo.titulo or not articulo.autor or not articulo.texto:
                continue
            articulos_por_autor[articulo.autor].append(articulo)

        # Generacion del índice para autores
        indice_autores = "<nav><h2>Índice de autores</h2><ul>"
        for autor in sorted(articulos_por_autor.keys()):
            autor_id = generar_id(autor)
            indice_autores += f'<li><a href="#{autor_id}">{autor}</a></li>'
        indice_autores += "</ul></nav><hr>"

        # Generacion de la lista de artículos para la página principal
        lista_articulos = ""
        for autor, articulos in articulos_por_autor.items():
            autor_id = generar_id(autor)
            lista_articulos += f'<section id="{autor_id}">\n<h3>{autor}</h3>\n'
            
            for articulo in articulos:
                id_articulo = generar_id(articulo.titulo)
                lista_articulos += f"""
                <div class="articulo-resumen">
                    <h4><a href="{carpeta_articulos}/{id_articulo}.html">{articulo.titulo}</a></h4>
                    <p>Por: {articulo.autor}</p>
                </div>
                """
            lista_articulos += "</section>\n"

                # HTML completo de la página principal
        html_principal = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Nuestros Artículos Periodísticos</title>
            <link href="https://fonts.googleapis.com/css2?family=PT+Sans&display=swap" rel="stylesheet">
            <style>
                body {{
                    font-family: "PT Sans", sans-serif;
                    margin: 40px;
                    background-color: #DEDBD2;
                    color: #4313839;
                    line-height: 1.6;
                }}
                header {{
                    background-color: #EDAFB8;
                    color: #7C6A0A;
                    padding: 20px;
                    text-align: center;
                    margin-bottom: 30px;
                    border-radius: 8px;
                }}
                nav {{
                    background-color: #F7E1D7;
                    padding: 15px;
                    border-radius: 8px;
                    margin-bottom: 20px;
                }}
                nav ul {{
                    list-style: none;
                    padding: 0;
                    columns: 3;
                }}
                nav li {{
                    margin-bottom: 8px;
                }}
                section {{
                    margin-bottom: 30px;
                }}
                h1, h2 {{
                    color: #6F2732;
                }}
                h3 {{
                    color: #F58D9D;
                    border-bottom: 2px solid #EDAFB8;
                    padding-bottom: 5px;
                }}
                .articulo-resumen {{
                    background-color: #F7E1D7;
                    padding: 15px;
                    border-radius: 8px;
                    margin-bottom: 15px;
                }}
                .articulo-resumen h4 {{
                    margin-top: 0;
                    margin-bottom: 5px;
                }}
                .articulo-resumen p {{
                    margin: 0;
                    font-size: 0.9em;
                    color: #6F2732;
                }}
                a {{
                    color: #6F2732;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                footer {{
                    background-color: #4A5759;
                    color: #F7E1D7;
                    text-align: center;
                    padding: 10px;
                    margin-top: 40px;
                    border-radius: 8px;
                }}
                #busqueda {{
                    width: 50%;
                    padding: 10px;
                    font-size: 16px;
                    border-radius: 6px;
                    border: 1px solid #ccc;
                    margin-bottom: 20px;
                }}
            </style>
        </head>
        <body>
            <header>
                <h1>Artículos Disponibles</h1>
                <div id="buscador">
                    <input type="text" id="busqueda" placeholder="Buscar artículos...">
                </div>
            </header>
            {indice_autores}
            {lista_articulos if lista_articulos else "<p>No hay artículos disponibles.</p>"}
            <footer>
                <p>Pagina generada el {fecha}</p>
            </footer>
            <script>
                document.getElementById('busqueda').addEventListener('input', function() {{
                    const termino = this.value.toLowerCase();
                    const articulos = document.querySelectorAll('.articulo-resumen');

                    articulos.forEach(articulo => {{
                        const texto = articulo.textContent.toLowerCase();
                        if (texto.includes(termino)) {{
                            articulo.style.display = 'block';
                        }} else {{
                            articulo.style.display = 'none';
                        }}
                    }});
                }});
            </script>
        </body>
        </html>
        """

        # Guardar la página principal
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(html_principal)
        
        ruta_absoluta = os.path.abspath(nombre_archivo)
        webbrowser.open(f"file://{ruta_absoluta}")

        print(f"Portal generado correctamente. Archivo principal: {nombre_archivo}")
        print(f"Artículos guardados en la carpeta: {carpeta_articulos}/")