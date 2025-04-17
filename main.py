from parser import ParserHtml

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