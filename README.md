# Flask Interactive Charts

Aplicación web desarrollada con Flask que muestra gráficos interactivos utilizando Chart.js. Permite visualizar datos dinámicos que se actualizan en tiempo real, con una interfaz moderna y responsiva. Incluye una API REST para la obtención de datos y un diseño intuitivo para la visualización de información.

## Características

- Gráfico de barras interactivo con Chart.js
- Actualización dinámica de datos en tiempo real
- Diseño responsivo y moderno con CSS3
- Interfaz de usuario intuitiva
- API REST para obtener datos aleatorios
- Fácil de personalizar y extender

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/ksalapeg/flask-interactive-charts.git
cd flask-interactive-charts
```

2. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```
flask-interactive-charts/
├── app.py              # Archivo principal de la aplicación Flask
├── requirements.txt    # Dependencias del proyecto
├── .gitignore         # Archivos y directorios ignorados por Git
├── LICENSE            # Licencia MIT
└── templates/         # Directorio de plantillas
    └── index.html     # Plantilla principal con el gráfico
```

## Uso

1. Iniciar la aplicación:
```bash
python app.py
```

2. Abrir el navegador y acceder a:
```
http://localhost:5000
```

## Componentes Principales

### app.py
- Configuración de la aplicación Flask
- Ruta principal ('/') para renderizar la página
- Ruta de API ('/datos') para obtener datos aleatorios
- Generación de datos dinámicos

### templates/index.html
- Interfaz de usuario con diseño responsivo
- Implementación del gráfico usando Chart.js
- Estilos CSS integrados
- Funcionalidad JavaScript para actualización dinámica
- Diseño moderno y atractivo

## API Endpoints

### GET /datos
Retorna datos aleatorios en formato JSON:
```json
{
    "labels": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
    "valores": [23, 45, 67, 89, 12]
}
```

## Tecnologías Utilizadas

- **Backend**:
  - Flask 3.0.2
  - Werkzeug 3.0.1

- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript
  - Chart.js

## Personalización

### Modificar el Gráfico
Para cambiar el tipo de gráfico, modifica el parámetro `type` en la configuración de Chart.js en `index.html`:
```javascript
type: 'bar' // Cambiar a 'line', 'pie', etc.
```

### Cambiar los Datos
Para modificar los datos generados, edita la función `obtener_datos()` en `app.py`.

## Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Kevin Alape - [Ksalapeg.270700@gmail.com](mailto:Ksalapeg.270700@gmail.com)

Link del Proyecto: [https://github.com/ksalapeg/flask-interactive-charts](https://github.com/ksalapeg/flask-interactive-charts)

