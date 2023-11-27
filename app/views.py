# app.py
from http import HTTPStatus
from flask import request, jsonify, Blueprint, send_file
import copy
from zipfile import ZipFile

RESPONSE_BODY_DEFAULT = {"message": "", "data": [], "errors": []}
api = Blueprint("api", __name__, url_prefix="/api")

def validate_request(req, method):
    required_properties = []

    if method == 'delete':
        required_properties = ['descripcion', 'id', 'response', 'url']
        # Validar que el parámetro 'id' para DELETE esté presente
        if 'id' not in req:
            return False, "The 'id' parameter for DELETE is required."
    elif method == 'get':
        required_properties = ['body', 'descripcion', 'desc400', 'desc404', 'response', 'response2', 'response3', 'url']
        # Validar que el parámetro 'body' para POST sea una lista o un objeto JSON
        if 'body' in req:
            if not isinstance(req['body'], (list, dict)):
                return False, "The 'body' parameter for POST must be a list of JSON objects or a JSON object."
    elif method == 'post':
        required_properties = ['body', 'descripcion', 'response', 'url']
        # Validar que el parámetro 'body' para POST sea una lista o un objeto JSON
        if 'body' in req:
            if not isinstance(req['body'], (list, dict)):
                return False, "The 'body' parameter for POST must be a list of JSON objects or a JSON object."
    elif method == 'put':
        required_properties = ['body', 'descripcion', 'response', 'url']
        # Validar que el parámetro 'body' para POST sea una lista o un objeto JSON
        if 'body' in req:
            if not isinstance(req['body'], (list, dict)):
                return False, "The 'body' parameter for PUT must be a list of JSON objects or a JSON object."

    missing_properties = [prop for prop in required_properties if prop not in req]
    if missing_properties:
        error_message = f"Missing properties for {method.upper()} request: {', '.join(missing_properties)}"
        return False, error_message
    
    return True, None

@api.route('/generate_api', methods=['POST'])
def api_func():
    response_body = copy.deepcopy(RESPONSE_BODY_DEFAULT)
    request_json = request.json

    try:
        with ZipFile('api_files.zip', 'w') as zipf:
            # Escribir el código Flask en el archivo
            code = "from flask import Flask, jsonify, request\nfrom http import HTTPStatus\n\napp = Flask(__name__)\n\n"

            for method, requests in request_json.items():
                for req in requests:
                    is_valid, error_message = validate_request(req, method)
                    if not is_valid:
                        response_body["errors"].append(error_message)
                        return jsonify(response_body), HTTPStatus.BAD_REQUEST

                    # Concatenar la definición del endpoint con la descripción como comentario
                    code += f"""
@app.route('{req["url"]}', methods=['{method.upper()}'])
def {method}_{req["url"].replace('/', '_')}():
    # {req["descripcion"]}
    # Implementa la lógica de la solicitud aquí
"""

                    if method == 'get':
                        # Si es un GET, agregar un comentario explicativo sobre la estructura del cuerpo recibido
                        code += f"""
    # En el caso de un método GET, se espera que el cuerpo (body) tenga la siguiente estructura:
    # {req["body"]}
    # Ajusta esta lógica según tus necesidades específicas.
"""
                    elif method == 'post' or method == 'put':
                        # Si es un POST o PUT, agregar validación para asegurar que los elementos del cuerpo estén presentes en la solicitud
                        required_elements = req.get('body', [])
                        for element in required_elements:
                            code += f"""    if '{element}' not in request.json:
        return jsonify({{"message": "", "data": [], "errors": ["'{element}' is required in the request body"]}}), HTTPStatus.BAD_REQUEST
            """
                    elif method == 'delete':
                        # Si es un DELETE, agregar validación para asegurar que el parámetro 'id' esté presente en la solicitud
                        code += f"""    if 'id' not in request.json:
        return jsonify({{"message": "", "data": [], "errors": ["'id' is required in the request parameters"]}}), HTTPStatus.BAD_REQUEST
            """

                    code += f"""
    return 'Implementación de {method.upper()} para {req["url"]}'
"""

            # Agregar la condición de ejecución al final
            code += """
if __name__ == '__main__':
    app.run(debug=True)
"""

            # Escribir el código en un archivo
            with open('generated_api.py', 'w') as file:
                file.write(code)

            # Agregar el archivo al ZIP
            zipf.write('generated_api.py')

    except Exception as e:
        response_body["errors"].append(f"Error while creating ZIP file: {e}")
        return jsonify(response_body), HTTPStatus.INTERNAL_SERVER_ERROR

    return send_file('api_files.zip', as_attachment=True), HTTPStatus.OK
