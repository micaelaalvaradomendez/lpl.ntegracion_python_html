class ParserHtml:
    #inicializacion
    def __init__(self, articulos):
        self.articulos = articulos

    def generar_html(self, nombre_archivo="articulos.html"):
        cuerpo = ""
        for titulo, autor, texto in self.articulos:
            cuerpo += f"""
            <article>
                <h2>{titulo}</h2>
                <h4>Por {autor}</h4>
                <p>{texto}</p>
            </article>
            <hr>
            """
        html_completo = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Artículos Periodísticos</title>
        </head>
        <body>
            <h1>Lista de Artículos</h1>
            {cuerpo}
        </body>
        </html>
        """
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(html_completo)
        
        print(f"Archivo HTML generado correctamente: {nombre_archivo}")

articulos = [
    ("La ciencia del sueño", "Ana Torres", "Dormir bien mejora la memoria y el estado de ánimo."),
    ("Tecnología verde", "Luis Pérez", "Las energías renovables son el futuro del planeta."),
    ("Viajar en pandemia", "Marta López", "Consejos útiles para explorar el mundo de forma segura."),
    ("El auge de la inteligencia artificial", "Carlos Méndez", "La IA está transformando industrias enteras, desde la medicina hasta el transporte."),
    ("Cambio climático: ¿estamos a tiempo?", "Laura Gutiérrez", "El planeta muestra señales claras de deterioro. La acción global es urgente."),
    ("La revolución del teletrabajo", "Federico Alonso", "El trabajo remoto llegó para quedarse, con impactos en la productividad y la vida personal."),
    ("Comida saludable sin complicaciones", "Juliana Romero", "Pequeños cambios en la dieta pueden mejorar significativamente la salud."),
    ("Educación digital en América Latina", "Sofía Ramírez", "Las plataformas virtuales abren nuevas oportunidades de aprendizaje."),
    ("El arte callejero como forma de protesta", "Andrés Navarro", "Murales y grafitis expresan la voz del pueblo en tiempos de crisis.")

]

parser = ParserHtml(articulos)
parser.generar_html()

