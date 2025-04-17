import webbrowser
import os
from datetime import datetime
from collections import defaultdict


#funcion global para def generar_id(self,nombre):
def generar_id(texto):
    return texto.lower().replace(" ", "-").replace("á", "a").replace("é", "e") \
                     .replace("í", "i").replace("ó", "o").replace("ú", "u") \
                     .replace("ñ", "n")

#funcion globarl para generar el pie de pagina
def generar_footer():
    año_actual = datetime.now().year
    return f"""
    <footer class="bg-dark text-white text-center py-4 mt-5">
        <div class="container">
            <p> {año_actual} - Todos los derechos reservados</p>
            <p class="mb-0">Generado el {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
        </div>
    </footer>
    """


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
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <link href="https://fonts.googleapis.com/css2?family=PT+Sans&display=swap" rel="stylesheet">
                    <style>
                        body {{
                            font-family: "PT Sans", sans-serif;
                            background-color: #f8f9fa;
                            padding-top: 56px;
                        }}
                        .articulo-completo {{
                            background-color: white;
                            border-radius: 8px;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                            padding: 30px;
                            margin-top: 30px;
                        }}
                        .volver-inicio {{
                            margin-top: 20px;
                        }}
                    </style>
                </head>
                <body>
                    <!-- Navbar Bootstrap -->
                    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
                        <div class="container">
                            <a class="navbar-brand" href="../index.html">Articulo periodistico</a>
                        </div>
                    </nav>

                    <div class="container">
                        <div class="articulo-completo">
                            <h1 class="mb-3">{articulo.titulo}</h1>
                            <h5 class="text-muted mb-4">Por: {articulo.autor}</h5>
                            <div class="articulo-contenido">{articulo.texto.replace('\n', '<br>')}</div>
                            <a href="../index.html" class="btn btn-primary volver-inicio">← Volver al inicio</a>
                        </div>
                    </div>
                    {generar_footer()}
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
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
            indice_autores = """
                <div class="card mb-5">
                    <div class="card-header">
                        <h2 id="autores">Autores</h2>
                    </div>
                    <div class="card-body">
                        <div class="row">                            
                            <div class="col-md-4 mb-3">
                            <div class="d-flex justify-content-between align-items-center border p-3 rounded">
                            <a href="#{generar_id(autor)}" class="btn btn-outline-primary w-100 position-relative">
                            {autor}
                            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                            {len(articulos)}</span></a></div>
                            for autor, articulos in sorted(articulos_por_autor.items())
                            )}
                        </div>
                    </div>
                </div>
                """
            
        def generar_tabla(articulos_por_autor):
            filas = ""
            total = len(self.articulos)
            for autor, articulos in sorted(articulos_por_autor.items(), key=lambda x: -len(x[1])):
                filas += (
                    f"<tr>"
                    f"<td><a href='#{generar_id(autor)}' class='text-decoration-none'>{autor}</a></td>"
                    f"<td class='text-end'>{len(articulos)}</td>"
                    f"</tr>"
                )
            return f"""
            <div class="card mb-4">
                <div class="card-header bg-primary text-white">
                    <h3 class="mb-0"><i class="bi bi-bar-chart me-2"></i>Autores</h3>
                </div>
                <div class="card-body">
                    <div class="table-responsive">
                        <table class="table table-striped table-hover">
                            <thead class="table-light">
                                <tr>
                                    <th>Autor</th>
                                    <th class="text-end">Artículos Publicados</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filas}
                            </tbody>
                            <tfoot class="table-secondary fw-bold">
                                <tr>
                                    <td>Total</td>
                                    <td class="text-end">{sum(len(a) for a in articulos_por_autor.values())}</td>
                                </tr>
                            </tfoot>
                        </table>
                    </div>
                </div>
            </div>
            """

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
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=PT+Sans&display=swap" rel="stylesheet">
            <style>
                body {{
                    font-family: "PT Sans", sans-serif;
                    background-color: #f8f9fa;
                    padding-top: 56px;
                }}
                .articulo-card {{
                    height: 100%;
                    transition: transform 0.3s;
                }}
                .articulo-card:hover {{
                    transform: translateY(-5px);
                    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
                }}
                .autor-section {{
                    margin-bottom: 40px;
                }}
                .autor-title {{
                    border-bottom: 2px solid #dee2e6;
                    padding-bottom: 10px;
                    margin-bottom: 20px;
                }}
            </style>
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
                <div class="container">
                    <a class="navbar-brand" href="index.html">Articulos Periodisticos</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <form class="d-flex" role="search">
                            <input class="form-control me-2" type="search" placeholder="Buscar..." id="busqueda">
                        </form>
                    </div>
                </div>
            </nav>

            <div class="container mt-5">
                <h1 class="text-center mb-5">Artículos Disponibles</h1>
                {generar_tabla(articulos_por_autor)}
                <div class="card mb-5">
                    <div class="card-header">
                        <h2 id="autores">Autores</h2>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            {"".join(
                                f'<div class="col-md-4 mb-3"><a href="#{generar_id(autor)}" class="btn btn-outline-primary w-100">{autor}</a></div>'
                                for autor in sorted(articulos_por_autor.keys())
                            )}
                        </div>
                    </div>
                </div>
                {"".join(
                    f'''
                    <div class="autor-section" id="{generar_id(autor)}">
                        <h2 class="autor-title">{autor}</h2>
                        <div class="row">
                            {"".join(
                                f'''
                                <div class="col-md-4 mb-4">
                                    <div class="card articulo-card">
                                        <div class="card-body">
                                            <h5 class="card-title">{articulo.titulo}</h5>
                                            <h6 class="card-subtitle mb-2 text-muted">Por: {articulo.autor}</h6>
                                            <a href="{carpeta_articulos}/{generar_id(articulo.titulo)}.html" class="btn btn-primary mt-3">Leer más</a>
                                        </div>
                                    </div>
                                </div>
                                '''
                                for articulo in articulos
                            )}
                        </div>
                    </div>
                    '''
                    for autor, articulos in articulos_por_autor.items()
                )}
            </div>
            {generar_footer()}
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            <script>
                // Función de búsqueda
                document.getElementById('busqueda').addEventListener('input', function() {{
                    const termino = this.value.toLowerCase();
                    const cards = document.querySelectorAll('.articulo-card');

                    cards.forEach(card => {{
                        const texto = card.textContent.toLowerCase();
                        if (texto.includes(termino)) {{
                            card.parentElement.style.display = 'block';
                        }} else {{
                            card.parentElement.style.display = 'none';
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

        #para que se abra el html al ejecutar el codigo
        ruta_absoluta = os.path.abspath(nombre_archivo)
        webbrowser.open(f"file://{ruta_absoluta}")

        print(f"HTML generado correctamente. Archivo principal: {nombre_archivo}")
        print(f"Artículos guardados en la carpeta: {carpeta_articulos}/")