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
#Validacion de articulos
class LongitudInvalidaError(Exception):
    def __init__(self, campo, longitud_minima):
        super().__init__(f"El campo '{campo}' debe tener al menos {longitud_minima} caracteres.")

#filtro de letras por apellido
def filtro_alfabeto(articulos_por_autor):
    iniciales = sorted({autor.split()[-1][0].upper() for autor in articulos_por_autor.keys()})
    
    #filtro en HTML
    html = """
    <div class="card mb-4">
        <div class="card-header">
            <h4 class="mb-0">Filtrar por apellido</h4>
        </div>
        <div class="card-body p-2">
            <div class="d-flex flex-wrap justify-content-center">
                <a href="#" class="btn btn-sm btn-outline-primary m-1" onclick="resetFiltro()">Todos</a>
    """

    #todas las letras
    letras = [chr(i) for i in range(65, 91)]  # A-Z
    for letra in letras:
        if letra in iniciales:
            html += f"""
                <a href="#" class="btn btn-sm btn-primary m-1" onclick="filtrarPorInicial('{letra}')">{letra}</a>
            """
        else:
            html += f"""
                <span class="btn btn-sm btn-outline-secondary m-1 disabled">{letra}</span>
            """
    
    html += """
            </div>
        </div>
    </div>
    """
    return html

def seccion_autores(articulos_por_autor):
    html = ""
    for autor, articulos in sorted(articulos_por_autor.items(), key=lambda x: x[0].split()[-1]):
        inicial_apellido = autor.split()[-1][0].upper()
        html += f"""
        <div class="autor-section" data-inicial="{inicial_apellido}">
            <h2 class="autor-title border-bottom pb-2" id="{generar_id(autor)}">{autor}</h2>
            <div class="row">
        """
        
        for articulo in articulos:
            html += f"""
                <div class="col-md-4 mb-4">
                    <div class="card articulo-card h-100">
                        <div class="card-body">
                            <h5 class="card-title">{articulo.titulo}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">Por: {articulo.autor}</h6>
                            <a href="articulos/{generar_id(articulo.titulo)}.html" class="btn btn-primary mt-3">Leer más</a>
                        </div>
                    </div>
                </div>
            """
        
        html += """
            </div>
        </div>
        """
    return html

class Articulo:
    def __init__(self, titulo, autor, texto):
        if len(titulo) < 10:
            raise LongitudInvalidaError("Título", 10)
        if len(texto) < 10:
            raise LongitudInvalidaError("Texto", 10)
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

        # Generar tabla de autores
        filas_tabla = ""
        for autor, articulos in sorted(articulos_por_autor.items(), key=lambda x: -len(x[1])):
            filas_tabla += f"""
            <tr>
                <td><a href='#{generar_id(autor)}' class='text-decoration-none'>{autor}</a></td>
                <td class='text-end'>{len(articulos)}</td>
            </tr>
            """

        tabla_autores = f"""
        <div class="card mb-4">
            <div class="card-header bg-primary text-white">
                <h3 class="mb-0">Autores</h3>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-striped table-hover">
                        <thead class="table-light">
                            <tr>
                                <th>Autor</th>
                                <th class="text-end">Artículos</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filas_tabla}
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

        # Generar secciones de artículos por autor
        secciones_articulos = ""
        for autor, articulos in sorted(articulos_por_autor.items(), key=lambda x: x[0].split()[-1]):
            inicial_apellido = autor.split()[-1][0].upper()
            secciones_articulos += f"""
            <div class="autor-section mb-5" data-inicial="{inicial_apellido}" id="{generar_id(autor)}">
                <h2 class="autor-title border-bottom pb-2">{autor}</h2>
                <div class="row">
            """

            for articulo in articulos:
                secciones_articulos += f"""
                    <div class="col-md-4 mb-4">
                        <div class="card articulo-card h-100">
                            <div class="card-body">
                                <h5 class="card-title">{articulo.titulo}</h5>
                                <h6 class="card-subtitle mb-2 text-muted">Por: {articulo.autor}</h6>
                                <a href="{carpeta_articulos}/{generar_id(articulo.titulo)}.html" class="btn btn-primary mt-3">Leer más</a>
                            </div>
                        </div>
                    </div>
                """

            secciones_articulos += """
                </div>
            </div>
            """

        # HTML completo
        html_principal = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Portal de Artículos</title>
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
                .btn.active {{
                    font-weight: bold;
                    transform: scale(1.05);
                }}
            </style>
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
                <div class="container">
                    <a class="navbar-brand" href="index.html">Artículos Periodísticos</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <form class="d-flex ms-auto" role="search">
                            <input class="form-control me-2" type="search" placeholder="Buscar..." id="busqueda">
                        </form>
                    </div>
                </div>
            </nav>

            <div class="container mt-5">
                <h1 class="text-center mb-5">Artículos Disponibles</h1>

                {tabla_autores}

                {filtro_alfabeto(articulos_por_autor)}

                {secciones_articulos}
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
                        card.style.display = texto.includes(termino) ? 'block' : 'none';
                    }});
                }});

                // Filtro por inicial
                function filtrarPorInicial(inicial) {{
                    // Resaltar letra activa
                    document.querySelectorAll('.card-body .btn').forEach(btn => {{
                        btn.classList.remove('active');
                        if (btn.textContent === inicial) {{
                            btn.classList.add('active');
                        }}
                    }});

                    // Filtrar secciones
                    document.querySelectorAll('.autor-section').forEach(section => {{
                        section.style.display = section.dataset.inicial === inicial ? 'block' : 'none';
                    }});

                    // Scroll a la primera sección visible
                    const primeraSeccion = document.querySelector('.autor-section[style="display: block;"]');
                    if (primeraSeccion) {{
                        window.scrollTo({{
                            top: primeraSeccion.offsetTop - 100,
                            behavior: 'smooth'
                        }});
                    }}
                }}

                function resetFiltro() {{
                    // Quitar resaltado de letras
                    document.querySelectorAll('.card-body .btn').forEach(btn => {{
                        btn.classList.remove('active');
                    }});

                    // Mostrar todas las secciones
                    document.querySelectorAll('.autor-section').forEach(section => {{
                        section.style.display = 'block';
                    }});
                }}
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