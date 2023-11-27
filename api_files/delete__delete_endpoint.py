
from flask import Flask

app = Flask(__name__)

@app.route('/delete_endpoint', methods=['DELETE'])
def delete__delete_endpoint():
    # Implementa la lógica de la solicitud aquí
    return 'Implementación de DELETE para /delete_endpoint'

if __name__ == '__main__':
    app.run(debug=True)
