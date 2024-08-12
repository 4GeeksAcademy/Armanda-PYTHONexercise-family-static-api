"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.next_id = 1
        self.members = []


from flask import Flask, jsonify; request
#from models import Person

app = Flask(__name__)
# app.url_map.strict_slashes = False
# CORS(app)

# create the jackson family object, Inicializa la clase FamilyStructure con el nombre 'Jackson'
jackson_family = FamilyStructure('Jackson')


# Agregar los miembros iniciales de la familia Jackson
jackson_family.add_member({
    "first_name": "John",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
})

jackson_family.add_member({
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
})

jackson_family.add_member({
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
})


#declaro los Endpoints

# Aqui con este Endpoints 'GET' devuelvo, obtengo todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200


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

