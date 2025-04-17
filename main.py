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
    ("El arte callejero como forma de protesta", "Andrés Navarro", "Murales y grafitis expresan la voz del pueblo en tiempos de crisis."),
    ("La siesta como herramienta de productividad", "Ana Torres", "Un descanso breve durante el día puede mejorar el rendimiento cognitivo."),
    ("Impacto de la IA en la educación", "Carlos Méndez", "Desde tutores inteligentes hasta clases personalizadas, la IA transforma el aula."),
    ("Nuevas formas de viajar en un mundo post-pandemia", "Marta López", "La industria del turismo se reinventa con protocolos más sostenibles."),
    ("De la calle al museo: el viaje del arte urbano", "Andrés Navarro", "La legitimación del arte callejero en espacios institucionales."),
    ("El rol de la mujer en la ciencia", "Claudia Moreno", "Rompiendo barreras históricas en laboratorios y universidades."),
    ("Minimalismo digital: menos es más", "Ricardo Díaz", "Reducir el uso de pantallas para mejorar la salud mental."),
    ("Agroecología: una alternativa sostenible", "Lucía Fernández", "Cultivar respetando la naturaleza y fortaleciendo comunidades."),
    ("Ciberseguridad en el hogar", "Javier Castillo", "Proteger tus dispositivos personales también es crucial."),
    ("Neurociencia y aprendizaje", "Silvia Rivas", "Cómo funciona el cerebro al adquirir nuevos conocimientos."),
    ("Movimientos juveniles y cambio social", "Marina Torres", "Los jóvenes lideran transformaciones políticas y culturales.")
]


parser = ParserHtml(articulos)
parser.generar_html()