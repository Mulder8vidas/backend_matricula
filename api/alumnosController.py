

from flask import jsonify, request
from flask_jwt_extended import jwt_required

from api import api_bp
from dataBase.querys import obtenerAlumnos, registrarAlumno, editarAlumno, eliminarAlumno


@api_bp.route('/alumnos', methods=['GET'])
@jwt_required()
def getAlumnos():
    alumnos=obtenerAlumnos()
    return jsonify(alumnos), 200
@api_bp.route('/alumnos', methods=['POST'])
@jwt_required()
def createAlumno():
    alumno=request.get_json()
    guardarbd=registrarAlumno(alumno['nombres'],alumno['apellidos'],alumno['fechaNacimiento'],alumno['dni'],alumno['sexo'],alumno['apoderado'],alumno['nroTelefono'],alumno['direccion'],alumno['nivel'],alumno['grado'])
    if guardarbd ==True:
        return jsonify({"message":"Alumno guardado exitosamente"}), 200
    else:
        return jsonify({"message":"error"}), 400

@api_bp.route('/alumnos/<id>', methods=['PUT'])
@jwt_required()
def updateAlumno(id):
    alumno=request.get_json()
    guardarbd=editarAlumno(id,alumno['Nombres'],alumno['Apellidos'],alumno['DNI'],alumno['Sexo'],alumno['Apoderado'],alumno['NroTelefono'],alumno['Direccion'],alumno['Nivel'],alumno['Grado'])
    if guardarbd ==True:
        return jsonify({"message":"Alumno editado exitosamente"}), 200
    else:
        return jsonify({"message":"error"}), 400

@api_bp.route('/alumnos/<id>', methods=['DELETE'])
@jwt_required()
def deleteAlumno(id):
    deletear= eliminarAlumno(id)
    if deletear==True:
        return jsonify({"message":"Alumno eliminado exitosamente"}),200
    else:
        return jsonify({"message":"Error al eliminar alumno"}),400