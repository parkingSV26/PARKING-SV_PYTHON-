# Parking SV — Prototipo de escritorio en Python

[English](README.md) | [Español](README.es.md)

## Descripción general

Este repositorio contiene un prototipo independiente de escritorio en Python relacionado con Parking SV. Explora cómo presentar una experiencia de descubrimiento de parqueos dentro de una aplicación de escritorio utilizando **BeeWare Toga** y una vista web integrada.

Es una base de código distinta de la aplicación web Parking SV desarrollada con Next.js. Ambos repositorios tienen implementaciones e historiales separados.

## Qué incluye el prototipo

- Pantallas de bienvenida, navegación y página principal.
- Formularios visuales de inicio de sesión y registro.
- Catálogo de parqueos con búsqueda de texto sobre registros de ejemplo predefinidos.
- Fichas de parqueos con horarios, tarifas, descripciones, imágenes, servicios y restricciones de muestra.
- Pantallas de perfil, notificaciones, contacto y planes.
- Enlaces de navegación externa, incluidos enlaces de Waze asociados a parqueos de ejemplo.

La interfaz está principalmente en español y utiliza una maquetación adaptable al área de la vista web integrada.

## Cómo funciona

La capa Python actúa como una envoltura ligera de escritorio:

1. **Parking_SV/__main__.py** inicia la aplicación.
2. **Parking_SV/app.py** crea una ventana MainWindow de Toga.
3. La aplicación lee **resources/Index.html** desde los recursos empaquetados.
4. Un componente WebView de Toga muestra la interfaz HTML dentro de la ventana de la aplicación.
5. JavaScript incluido en el HTML cambia entre pantallas, filtra la lista local de parqueos de ejemplo y muestra sus detalles.

La interfaz visual está implementada en un único recurso HTML con CSS y JavaScript integrados. **pyproject.toml** contiene los metadatos de empaquetado de Briefcase y las dependencias de Toga para cada plataforma.

## Límites del prototipo

Este repositorio debe evaluarse como un prototipo de interfaz e integración de escritorio, no como un servicio de parqueos en funcionamiento.

- Los parqueos están predefinidos en el frontend; no se consultan desde una API de producción.
- La búsqueda filtra la lista local de ejemplos.
- Las pantallas de inicio de sesión y registro no autentican usuarios ni crean cuentas.
- Las reservas, la disponibilidad y las notificaciones son ejemplos sin conexión a un servicio real.
- El formulario de contacto no envía mensajes.
- Esta base de código no implementa pagos, inventario en tiempo real, servidor de aplicación ni integración con una base de datos.

Los nombres, precios, datos de contacto, imágenes y descripciones que aparecen en la interfaz son contenido de muestra y no deben considerarse información comercial verificada.

## Tecnologías

- Python 3
- BeeWare Toga
- Briefcase
- Toga WebView
- HTML5, CSS3 y JavaScript

## Ejecución en modo desarrollo

El proyecto Briefcase se encuentra dentro del directorio **Parking-SV/**.

~~~bash
cd Parking-SV
python -m venv .venv
~~~

Activa el entorno:

**Windows PowerShell**
~~~powershell
.venv\Scripts\Activate.ps1
~~~

**Linux / macOS**
~~~bash
source .venv/bin/activate
~~~

Instala Briefcase y ejecuta la aplicación en modo desarrollo:

~~~bash
python -m pip install briefcase
briefcase dev
~~~

Las dependencias nativas necesarias varían según el sistema operativo. La configuración específica de cada plataforma está declarada en **pyproject.toml**.

## Estructura del código

~~~text
Parking-SV/
├── pyproject.toml
├── src/Parking_SV/
│   ├── __main__.py
│   ├── app.py
│   └── resources/
│       └── Index.html
└── tests/
~~~

## Proyecto relacionado

- [Parking SV — Aplicación web Next.js](https://github.com/parkingSV26/parkingsv-web)
- [Experiencia web pública de Parking SV](https://parkingsv.vercel.app/)

El prototipo Python es una referencia de implementación separada. Su funcionalidad y sus colaboradores no deben confundirse con los de la aplicación Next.js.
