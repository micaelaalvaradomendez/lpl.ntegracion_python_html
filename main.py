from parser import ParserHtml
from parser import Articulo


#articulos de ejemplo generados con ChatGPT
articulos_def = [
    ("La ciencia del sueño", "Ana Torres", 
     "Dormir bien mejora la memoria y el estado de ánimo. También reduce el estrés. Estudios muestran que el sueño profundo ayuda a consolidar recuerdos y mejora el rendimiento diario en actividades laborales y académicas."),
    
    ("Tecnología verde", "Carlos Méndez", 
     "Paneles solares, turbinas eólicas y baterías avanzadas están revolucionando cómo producimos y usamos la energía. Estas tecnologías no solo son sostenibles, sino que también impulsan el desarrollo económico en zonas rurales y urbanas."),
    
    ("Viajar en pandemia", "Marta López", 
     "Viajar con precauciones como mascarilla, vacunas y distanciamiento social es clave para explorar el mundo sin riesgos innecesarios."),
    
    ("El auge de la inteligencia artificial", "Carlos Méndez", 
     "La IA transforma industrias: desde medicina hasta transporte. Los algoritmos ya son clave en tareas cotidianas y estratégicas. Su impacto exige un debate ético sobre privacidad, sesgos, automatización del empleo y supervisión legal adecuada."),
    
    ("La revolución del teletrabajo", "Marta López", 
     "El trabajo remoto trajo libertad, pero también nuevos retos: fatiga digital, soledad y dificultad para desconectar."),
    
    ("Comida saludable sin complicaciones", "Juliana Romero", 
     "Cambios simples en la dieta, como sumar verduras o reducir azúcar, pueden hacer la diferencia. Planificar comidas caseras ayuda a evitar ultraprocesados y mantener un buen estado físico y mental en el largo plazo."),
    
    ("Educación digital en América Latina", "Carlos Méndez", 
     "La tecnología amplía el acceso educativo. Pero aún hay desafíos: falta de conexión, escasez de dispositivos, y necesidad de formación docente para lograr un aprendizaje significativo en entornos virtuales."),
    
    ("El arte callejero como forma de protesta", "Marta López", 
     "Murales y grafitis se convierten en voz de comunidades que buscan justicia. El arte urbano refleja el espíritu de lucha de las ciudades en crisis."),
    
    ("La siesta como herramienta de productividad", "Ana Torres", 
     "Descansar entre 10 y 30 minutos mejora el estado de alerta, reduce el estrés y potencia la creatividad. La siesta, bien planificada, es un recurso subestimado para el rendimiento laboral y el bienestar general."),
    
    ("Impacto de la IA en la educación", "Carlos Méndez", 
     "Tutores virtuales, plataformas adaptativas y evaluación automática están cambiando cómo aprendemos. La IA permite personalizar contenidos, pero también requiere una reflexión crítica sobre privacidad y equidad."),
    
    ("Nuevas formas de viajar en un mundo post-pandemia", "Marta López", 
     "El turismo se transforma: viajes más sostenibles, menos masivos y con más conciencia ambiental."),
    
    ("De la calle al museo: el viaje del arte urbano", "Marta López", 
     "El arte callejero llega a galerías y museos, lo que genera debates sobre su autenticidad. Aunque sigue siendo disruptivo, su inclusión en espacios institucionales plantea interrogantes sobre su esencia original y su comercialización."),
    
    ("El rol de la mujer en la ciencia", "Ana Torres", 
     "Mujeres científicas han roto barreras históricas. Desde la medicina hasta la astrofísica, hoy su participación es vital para el desarrollo global, aunque aún enfrentan desafíos de representación, equidad salarial y reconocimiento."),
    
    ("Minimalismo digital: menos es más", "Juliana Romero", 
     "Reducir el tiempo frente a pantallas mejora el bienestar. Este enfoque propone limitar el uso de redes sociales, priorizar relaciones reales y reencontrarse con el tiempo libre sin estímulos constantes."),
    
    ("Agroecología: una alternativa sostenible", "Carlos Méndez", 
     "La agroecología combina saberes ancestrales y ciencia moderna para producir alimentos sin dañar el entorno. Se basa en la biodiversidad, el uso eficiente de recursos locales y la autonomía de las comunidades agrícolas."),
    
    ("Ciberseguridad en el hogar", "Juliana Romero", 
     "Contraseñas fuertes, software actualizado y precaución con redes públicas: claves para cuidar tus datos."),
    
    ("Movimientos juveniles y cambio social", "Ana Torres", 
     "La juventud impulsa cambios sociales a través de redes, activismo y proyectos locales. Son protagonistas en temas como justicia ambiental, inclusión, derechos humanos y participación democrática."),

    ("Cultura maker y el poder de crear", "Valeria Ruiz", 
     "El movimiento maker impulsa la creatividad tecnológica. Desde la impresión 3D hasta el reciclaje electrónico, miles de personas desarrollan soluciones innovadoras en sus casas, escuelas o espacios compartidos, fomentando una cultura de autosuficiencia."),

    ("Narrativas interactivas en el periodismo", "Javier Ibáñez", 
     "El uso de infografías animadas, videos inmersivos y visualizaciones de datos en tiempo real permite una conexión más profunda con el lector. Las narrativas interactivas están redefiniendo la forma de informar y de consumir noticias digitales."),

    ("El lenguaje inclusivo en los medios", "Laura Martínez", 
     "El uso de lenguaje no sexista genera debate. Para algunos, es una herramienta de visibilización. Para otros, una imposición innecesaria. Sin embargo, cada vez más medios lo adoptan para fomentar una comunicación más equitativa."),

    ("Sostenibilidad en la moda urbana", "Gonzalo Herrera", 
     "Marcas independientes apuestan por ropa hecha con materiales reciclados y procesos éticos. Esta tendencia busca reducir el impacto ambiental y cuestiona el modelo de consumo rápido en la industria textil."),

    ("El fenómeno del true crime", "Javier Ibáñez", 
     "Series, podcasts y documentales que exploran crímenes reales han captado una gran audiencia. Este género plantea cuestionamientos sobre la ética del entretenimiento basado en tragedias reales.")
]


articulos = [Articulo(t, a, tx) for (t, a, tx) in articulos_def]

parser = ParserHtml(articulos)
parser.generar_html()