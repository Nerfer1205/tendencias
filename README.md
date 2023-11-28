Requisitos
Python 3.x
virtualenv (opcional pero recomendado)
Configuración del entorno
Clona el repositorio:


git clone https://github.com/Nerfer1205/tendencias.git
cd tendencias
Crea y activa un entorno virtual usando virtualenv:


# Instala virtualenv si aún no lo tienes instalado
pip install virtualenv

# Crea un entorno virtual
virtualenv venv

# Activa el entorno virtual
# En Windows
.\venv\Scripts\activate
# En Linux
source venv/bin/activate
Instala las dependencias del proyecto:

pip install -r requirements.txt

# Ejecutar la aplicación
python3 run.py
