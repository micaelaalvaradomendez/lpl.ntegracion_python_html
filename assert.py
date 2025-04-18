import os
from datetime import datetime
from collections import defaultdict
from parser import Articulo, ParserHtml, generar_id, LongitudInvalidaError

# Configuración de prueba
TEST_ARTICULOS = [
    ("Python en 2023", "Ana Torres", "Un análisis completo del lenguaje Python y sus nuevas características."),
    ("Inteligencia Artificial", "Carlos Pérez", "Cómo la IA está transformando diferentes industrias."),
    ("Desarrollo Web Moderno", "Marta López", "Las últimas tendencias en desarrollo web frontend y backend.")
]

def test_articulo():
    print("\n=== Probando clase Articulo ===")
    
    # Test creación válida
    articulo = Articulo("Título válido", "Autor Válido", "Texto con más de 10 caracteres")
    assert articulo.titulo == "Título válido", "Título no coincide"
    assert articulo.autor == "Autor Válido", "Autor no coincide"
    assert articulo.texto == "Texto con más de 10 caracteres", "Texto no coincide"
    print("Creación de artículo válido")
    
    # Test validaciones
    try:
        Articulo("Corto", "Autor", "Texto suficientemente largo")
        assert False, "Debería haber fallado por título corto"
    except LongitudInvalidaError as e:
        assert "título" in str(e).lower(), "Mensaje de error incorrecto"
        print("Validación de título corto")
    
    try:
        Articulo("Título válido", "Autor", "Corto")
        assert False, "Debería haber fallado por texto corto"
    except LongitudInvalidaError as e:
        assert "texto" in str(e).lower(), "Mensaje de error incorrecto"
        print("Validación de texto corto")
    
    # Test formateo autor
    articulo = Articulo("Título", "  juan  pérez  ", "Texto válido")
    assert articulo.autor == "Juan Pérez", "Autor no se formateó correctamente"
    print("Formateo de autor")

def test_parser_html():
    print("\n=== Probando clase ParserHtml ===")
    
    # Preparación
    articulos = [Articulo(*datos) for datos in TEST_ARTICULOS]
    parser = ParserHtml(articulos)
    output_file = "test_index.html"
    
    # Ejecución
    parser.generar_html(output_file)
    
    # Verificaciones
    assert os.path.exists(output_file), "No se creó el archivo HTML principal"
    print("Creación de archivo HTML principal")
    
    assert os.path.exists("articulos"), "No se creó la carpeta de artículos"
    for articulo in articulos:
        expected_file = f"articulos/{generar_id(articulo.titulo)}.html"
        assert os.path.exists(expected_file), f"No se creó {expected_file}"
    print("Creación de artículos individuales")
    
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    assert "<!DOCTYPE html>" in content, "Falta doctype en HTML"
    assert "Artículos Disponibles" in content, "Falta título en HTML"
    for articulo in articulos:
        assert articulo.titulo in content, f"Falta título '{articulo.titulo}' en HTML"
        assert articulo.autor in content, f"Falta autor '{articulo.autor}' en HTML"
    print("Contenido HTML principal")
    
    # Limpieza
    if os.path.exists(output_file):
        os.remove(output_file)
    if os.path.exists("articulos"):
        for file in os.listdir("articulos"):
            os.remove(os.path.join("articulos", file))
        os.rmdir("articulos")

def test_generar_id():
    print("\n=== Probando función generar_id ===")
    
    assert generar_id("Título del Artículo") == "título-del-artículo", "ID básico incorrecto"
    print("Generación de ID básico")
    
    assert generar_id("Canción de María") == "cancion-de-maria", "ID con acentos incorrecto"
    print("Generación de ID con acentos")
    
    assert generar_id("Año Nuevo") == "ano-nuevo", "ID con ñ incorrecto"
    print("Generación de ID con ñ")

if __name__ == "__main__":
    print("=== Iniciando pruebas ===")
    test_articulo()
    test_parser_html()
    test_generar_id()
    print("\n=== Todas las pruebas pasaron exitosamente ===")