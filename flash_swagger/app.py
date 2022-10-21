from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

server = Flask(__name__)
Swagger(server)
server.config['JSON_AS_ASCII'] = False


@server.route('/flask/flasgger/demo', methods=['POST'])
@swag_from('demo.yml')
def demo_request():
    json_data = request.json
    result = {"code": "200", "msg": "SUCCES", "data": {"name": "xxxxxx", "age": 25, "job": "python"}}
    return jsonify(result)


if __name__ == "__main__":
    server.run(port=8085, debug=True)
