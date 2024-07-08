from flask import jsonify
from flask_jwt_extended import jwt_required

import api
from dataBase.querys import obtenerAulas, eliminarAula, obtenerAlumnosxAula


@api.api_bp.route('/aulas', methods=['GET'])
@jwt_required()
def get_all_aulas():
    aulas=obtenerAulas()
    return jsonify(aulas),200

#@app.route('/user/<username>')

@api.api_bp.route('/aulas/<id>', methods=['DELETE'])
@jwt_required()
def delete_aulas(id):
    deletear= eliminarAula(id)
    if deletear==True:
        return jsonify({"message":"Aula eliminada exitosamente"}),200
    else:
        return jsonify({"message":"Error al eliminar tabla"}),400


@api.api_bp.route('/aulas/<id>', methods=['GET'])
@jwt_required()
def mostrar_alumnos_aula(id):
    datos_alumnos= obtenerAlumnosxAula(id)
    return jsonify(datos_alumnos),200