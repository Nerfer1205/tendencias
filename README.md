# Aplicación Flask

Este repositorio contiene una aplicación Flask simple que puedes ejecutar localmente. Asegúrate de seguir estos pasos para configurar y ejecutar la aplicación en tu entorno.

## Requisitos

- Python 3.x
- `virtualenv` (opcional pero recomendado)

## Configuración del entorno

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/Nerfer1205/tendencias.git
    cd tendencias
    ```

2. **(Opcional) Crear y activar un entorno virtual usando `virtualenv`:**

    ```bash
    # Instalar virtualenv si aún no lo tienes instalado
    pip install virtualenv

    # Crear un entorno virtual
    virtualenv venv

    # Activar el entorno virtual
    # En Windows
    .\venv\Scripts\activate
    # En Linux
    source venv/bin/activate
    ```

3. **Instalar las dependencias del proyecto:**

    ```bash
    pip install -r requirements.txt
    ```

## Ejecutar la aplicación

1. Asegúrate de estar en el directorio del proyecto y con el entorno virtual activado.

2. **Ejecutar la aplicación Flask:**

    ```bash
    python3 run.py
    ```

3. Abre tu navegador y visita [http://127.0.0.1:5000/](http://127.0.0.1:5000/) para ver la aplicación en funcionamiento.

## Detener la aplicación

Para detener la aplicación, simplemente presiona `Ctrl+C` en la terminal.

## Contribuciones

Si deseas contribuir a este proyecto, por favor crea un *issue* o envía un *pull request*.

¡Gracias por usar esta aplicación!
