Proyecto LexyPruebaTecnica

Este es un proyecto de prueba técnica desarrollado con Flask, que incluye una serie de rutas, controladores, y tests para validar el funcionamiento de una API básica. El proyecto permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) y está acompañado de pruebas unitarias para asegurar la correcta operación de cada uno de sus componentes.

Contenido:

Instalación
Estructura del Proyecto
Componentes
Pruebas
Uso

Instalación
Para configurar y ejecutar este proyecto, sigue los pasos a continuación:

Clona este repositorio.

git clone <https://github.com/jesusbloise/Lexy.git>
cd LexyPruebaTecnica

Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

Instala las dependencias requeridas:

pip install -r requirements.txt
Configura las variables de entorno si es necesario, como FLASK_APP para indicar el nombre del archivo de la aplicación de Flask.

Ejecuta la aplicación:

flask run

La aplicación debería estar disponible en http://localhost:5000.

Estructura del Proyecto
La estructura del proyecto es la siguiente:

my_project/
├── app/
│   ├── __init__.py
│   ├── routes.py
├── tests/
│   └── test_routes.py
├── README.md
├── requirements.txt
└── run.py

Componentes

app/__init__.py
Este archivo inicializa la aplicación de Flask y configura los componentes necesarios para la ejecución. Aquí se registra la aplicación y se configuran las rutas.

app/routes.py
Este archivo define las rutas de la API. Cada ruta está asociada a una operación específica, como obtener datos, crear nuevos registros o eliminar registros existentes. Ejemplos de rutas incluyen:

GET /items: Obtener una lista de ítems.

tests/test_routes.py
Este archivo contiene las pruebas para verificar el correcto funcionamiento de las rutas y controladores. Se emplea el framework pytest para validar las funcionalidades de la API, asegurando que las rutas devuelvan las respuestas esperadas. Se realizaron pruebas básicas de creación, obtención y eliminación de datos.

Pruebas
Para ejecutar las pruebas, asegúrate de estar en el entorno virtual y usa el siguiente comando:

pytest

Este comando ejecutará las pruebas en tests/test_routes.py y te informará de los resultados. Puedes usar pytest --disable-warnings si deseas ejecutar las pruebas sin las advertencias relacionadas con la deprecación de ast.Str.

Uso
Para interactuar con la API, puedes utilizar herramientas como curl o Postman. Aquí tienes algunos ejemplos de solicitudes:

Obtener una lista de ítems:

get http://localhost:5000/items

