from flask import Flask
from config.configuration import DevelopmentConfig
from flask_cors import CORS
from app.views import api

SERVICIOS = [('/api', api),]

app = Flask(__name__)

# Configuración de la base de datos
app.config.from_object(DevelopmentConfig())

CORS(app, resources={r"/*": {"origins": "*"}})
for url, blueprint in SERVICIOS:
        app.register_blueprint(blueprint, url_prefix=url)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)