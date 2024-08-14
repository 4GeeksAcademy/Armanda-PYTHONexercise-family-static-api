"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object, Inicializa la clase FamilyStructure con el nombre 'Jackson'
jackson_family = FamilyStructure('Jackson')

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


#declaro los Endpoints

# Aqui con este Endpoints 'GET' devuelvo, obtengo todos los miembros de la familia

# En este Endpoints 'GET' Obtengo un miembro específico por su ID
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200


# En este Endpoints 'GET' Obtengo un miembro específico por su ID
@app.route('/member/<int:menmber_id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404
    

    # En este Endpoints 'POST' Añado un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    member = request.json
    jackson_family.add_member(member)
    return jsonify({"msg": "Member added successfully"}), 200

# Aqui con este Endpoints  Eliminar un miembro por su ID
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = jackson_family.get_member(id)
    if member:
        jackson_family.delete_member(id)
        return jsonify({"msg": "Member deleted successfully"}), 200
    else:
        return jsonify({"error": "Member not found"}), 404




if __name__ == '__main__':
    app.run(debug=True)

