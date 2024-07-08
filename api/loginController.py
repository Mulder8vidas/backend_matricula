from flask import request, jsonify
from flask_jwt_extended import create_access_token

from api import api_bp
from dataBase.querys import register, login


@api_bp.route('/register', methods=['POST'])
def registro():
    data = request.get_json()
    print(data)
    retorno=register(data['username'],data['password'])

    if retorno:
        return jsonify({"message": "Registrado com sucesso!"}), 201
    else:
        return jsonify({"message": "Error al registrar"}), 400


@api_bp.route('/login', methods=['POST'])
def logincon():
    data = request.get_json()
    access_token = create_access_token(identity=data['username'])
    respuestabd=login(data['username'],data['password'])
    return jsonify({ "token": access_token, "username": data['username'] }), 200

