# 🌐 **Proyecto Dominios** 🚀

Este proyecto tiene como objetivo **buscar y analizar dominios**, enfocado en la **detección de phishing** y en la identificación de **posibles amenazas de seguridad web**. A través de diferentes métodos de búsqueda, el sistema permite monitorear registros de dominios, identificar patrones sospechosos y obtener información sobre dominios asociados con actividades maliciosas.


### 🔍 Funcionalidades

- **Búsqueda por fecha 📅**: Puedes buscar dominios registrados en una fecha específica. Por ejemplo, si deseas ver todos los dominios registrados el 5 de diciembre de 2024, simplemente ingresa la fecha `20241205`.

- **Búsqueda por rango de fechas ⏳**: Puedes buscar dominios registrados dentro de un rango de fechas. Por ejemplo, si quieres ver los dominios registrados entre el 5 de noviembre de 2024 y el 5 de diciembre de 2024, puedes ingresar el rango `20241105-20241205`.

- **Búsqueda por palabras clave 🗝️**: Si deseas encontrar dominios que contengan palabras clave específicas, puedes agregar esas palabras clave. Por ejemplo, si quieres ver dominios relacionados con el banco "BBVA", solo necesitas agregar la palabra `bbva`. **Si quieres traer todos los dominios sin ninguna restricción, escribe `todo`**.

  También puedes buscar múltiples palabras clave separadas por comas, como `bbva,santander,hsbc`, y el script traerá todos los dominios que contengan alguna de esas palabras clave. Si no deseas hacer una búsqueda filtrada, simplemente escribe `todo` para obtener todos los resultados disponibles.

- **Dominios con distintos TLDs 🌍**: El sistema soporta dominios con diferentes TLDs (por ejemplo, `.com`, `.net`, `.org`, etc.), lo que te permite obtener resultados más completos.

### 📋 Requisitos

Asegúrate de tener instalado `python` y `pip` antes de comenzar.

### 🚀 Instalación

Sigue estos pasos para clonar el repositorio y configurar el entorno:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Ivancastl/dominios.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd dominios
    ```

3. Instala las dependencias del proyecto usando el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### 🖥️ Uso

Una vez que las dependencias estén instaladas, puedes ejecutar el script con el siguiente comando:

```bash
python dominios.py
