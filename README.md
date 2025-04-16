<h2 align="center">Laboratorio de Programación y Lenguajes</h2>
<h1 align="center">Integracion de Python con HTML y CSS</h1>
<h2 align="center">Trabajo Práctico N°2</h2>
<div align="center"> 
  <p>En este repositorio se encuentra el desarrollo que corresponde a un trabajo practico de la carrera "Licenciatura en Sistemas" de la UNTDF correspondiente a la materia "Laboratorio de programacion y lenguajes</p>
  <p>El trabajo consiste en generar una web dinamica de articulos periodisticos a traves de scripts en Python que generen automáticamente un sitio web a partir de una lista de artículos periodísticos, implementando progresivamente funcionalidades tanto visuales como estructurales. La web final cuenta con una presentación clara de los artículos, organización por autor, navegación entre páginas, estilo personalizado y uso de Bootstrap.</p>
<p>En el repositorio se adjunta el trabajo practico proporcionado por la materia.</p>
<p>Para ver el proyecto solo hay que ejecutar el scrip de generador.py</p>
</div>
<h2 aling="center">Funcionalidades Implementadas</h2>
 
1. **Generación básica de HTML** con f-strings desde una lista de tuplas.
2. **Filtrado de artículos vacíos** y normalización del autor (capitalización y eliminación de espacios).
3. Inclusión de **header y footer** con la fecha actual.
4. Estilos aplicados mediante **bloque `<style>`** dentro del `<head>`.
5. Agrupación de artículos por **autor** con encabezados `<h3>`.
6. **Índice de autores** con enlaces internos (`<a href="#autor">`).
7. Reemplazo de tuplas por objetos de la clase `Articulo` con método `to_html()`.
8. **Filtro por palabra clave** dentro del contenido del artículo.
9. Visualización recortada a los **primeros 300 caracteres** del texto.
10. Generación de una **página individual por artículo**, con enlace desde el índice.
11. Inclusión de un enlace para **volver al índice** desde cada artículo.
12. Uso de **Bootstrap**: grillas de 3 artículos por fila y navbar estilizada.
13. Organización del código en **múltiples archivos**: lógica y ejecución.
14. Centralización del **footer reutilizable**, incluyendo el año actual.
15. Tabla con **cantidad de artículos por autor** al inicio del índice.
16. Validación de campos (`título`, `texto`) con excepciones personalizadas.
17. Navegación por autores según la **letra inicial de su apellido**.
18. Archivo de **tests con `assert`** para probar métodos clave.
19. Navegación entre artículos: **enlaces a anterior/siguiente**.
