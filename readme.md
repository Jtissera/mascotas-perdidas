# MASCOTAS PERDIDAS

## ¿Qué es *Mascotas Perdidas*?

*Mascotas Perdidas* es una aplicación web desarrollada para la materia **Introducción al Desarrollo de Software** de la cátedra **Lanzillotta** en la Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA). Su propósito es facilitar la búsqueda y el encuentro de mascotas perdidas, conectando personas que han encontrado animales extraviados con quienes están buscándolos. Esta plataforma fomenta la colaboración de la comunidad en la reubicación de mascotas con sus familias.

## Objetivo

El objetivo principal de la aplicación es ofrecer un sistema intuitivo y accesible para que los usuarios puedan publicar tanto avisos de mascotas perdidas como de mascotas encontradas, permitiendo que cada mascota extraviada tenga mayores posibilidades de regresar a su hogar. La aplicación permite a los usuarios cargar detalles específicos (ubicación, características físicas, contacto, entre otros) y visualizarlos en un mapa para una búsqueda geográfica más precisa.

## Tecnologías utilizadas

El desarrollo de la aplicación utiliza diversas tecnologías para crear una experiencia eficiente y visualmente amigable. A continuación, el stack tecnológico:

- **HTML** y **CSS**: para la estructura y estilos de la interfaz.
- **Flask**: framework de Python utilizado para manejar el backend y el enrutamiento.
- **SQL**: para gestionar la base de datos de mascotas y usuarios.
- **JavaScript**: en algunas secciones de la interfaz para mejorar la interactividad.
- **Google Maps**: para visualizar la ubicación de las mascotas extraviadas o encontradas, utilizando un iframe en la página correspondiente.

## Estructura del Proyecto

La estructura de carpetas está organizada de la siguiente forma:

- **Frontend/**
  - **static/**
    - `style.css`: contiene los estilos de la aplicación.
    - `images/`: carpeta con imágenes utilizadas en la interfaz.
  - **templates/**: carpeta con las plantillas HTML para las diferentes vistas de la aplicación.
    - `base.html`: plantilla base que sirve como marco general.
    - `homev1.html`: página principal de la aplicación.
    - `index.html` y `index-2.html`: otras versiones de la página de inicio.
    - `perdi_mi_mascota.html`: vista para la carga de datos de mascotas perdidas.

- **app.py**: archivo principal que configura y ejecuta el servidor Flask, definiendo las rutas para las diferentes páginas.

## Servicios y Herramientas Utilizadas

Para el desarrollo y prueba de la aplicación *Mascotas Perdidas*, se utilizan diversas herramientas y servicios que facilitan tanto el desarrollo como la integración de funcionalidades. A continuación, se presenta un listado de los más relevantes:

### Herramientas de Desarrollo

- **Postman**: 
  - Una herramienta útil para probar APIs. Permite enviar solicitudes HTTP a tu servidor Flask y verificar las respuestas, facilitando la depuración y el desarrollo de la API.

### APIs Externas

- **Google Maps API**:
  - Utilizada para integrar mapas en la aplicación. Permite visualizar la ubicación de las mascotas perdidas y encontradas. Para usarla, es necesario registrarse en Google Cloud Platform y obtener una clave API.

- **Twilio API** (opcional):
  - Si decides implementar notificaciones por SMS para usuarios que reportan mascotas perdidas o encontradas, Twilio ofrece una API sencilla para enviar y recibir mensajes de texto.

- **Cloudinary** (opcional):
  - Un servicio para gestionar y almacenar imágenes. Puede ser útil si planeas permitir a los usuarios subir fotos de mascotas perdidas o encontradas.

### Otras Herramientas

- **GitHub**:
  - Plataforma de control de versiones que permite gestionar el código fuente del proyecto, colaborar con otros desarrolladores y mantener un historial de cambios.

- **Virtualenv**:
  - Herramienta para crear entornos virtuales en Python, lo que ayuda a evitar conflictos de dependencias y mantener un entorno limpio para el desarrollo.

### Recomendaciones

Es importante que los miembros del equipo se familiaricen con estas herramientas y servicios para mejorar el flujo de trabajo y la calidad del desarrollo. Cada uno de estos servicios requiere configuración adicional, así que asegúrate de revisar la documentación oficial para su correcta implementación.

## Instalación y Configuración

### Prerrequisitos

Para correr esta aplicación en tu entorno local, necesitas tener instalado:

- **Python 3.x**: la versión mínima recomendada es 3.6.
- **Flask**: framework web para Python.
- **pip**: administrador de paquetes de Python (suele venir instalado con Python).

### Paso a paso para la instalación

1. Clona el repositorio de GitHub en tu máquina local:
    ```bash
    git clone https://github.com/usuario/repo-mascotas-perdidas.git
    ```
   
2. Cambia al directorio del proyecto:
    ```bash
    cd repo-mascotas-perdidas
    ```

3. Crea y activa un entorno virtual (opcional pero recomendado para evitar conflictos de dependencias):
    ```bash
    python3 -m venv env
    source env/bin/activate  # En Linux/Mac
    .\env\Scripts\activate   # En Windows
    ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

### Dependencias y Versiones

El archivo `requirements.txt` contiene todas las dependencias necesarias para el correcto funcionamiento de la aplicación. Algunas de las principales son:

- **Flask**: permite levantar el servidor y manejar las rutas de la aplicación.
- **Jinja2**: motor de plantillas utilizado por Flask para renderizar las vistas HTML.
- **Werkzeug**: proporciona herramientas para gestionar peticiones HTTP.