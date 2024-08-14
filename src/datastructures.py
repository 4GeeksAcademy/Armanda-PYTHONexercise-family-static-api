
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

#iniciazlizando la extrutura de datos. inicializamos la extructura de la clase desde el componente que tiene los objetos
class FamilyStructure: 
    def __init__(self, last_name):
        self.last_name = last_name
#Aqui le damos valor cero al self._next_ id, para que empieze la apsinacion de id desde cero 
        self._next_id = 0

 #aqui escribimos todos los objetos que se vera en pantalla
        self._members =[
        {
            "first_name":"john",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers": [7,13,22],
            "id": self._generate_id()
        }, 
        {
            "first_name":"Jane ",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3],
            "id": self._generate_id()

        },
        {
            "first_name":"Jimmy ",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1],
            "id": self._generate_id()

        }

        ]
        
    #creamos la variable def_generate_id y le introducimos el parametro self
     # Este método genera un 'id' único al agregar miembros a la lista 
    def _generate_id(self): 
 #a continuacion la ponemos la variable creada a igual self.nombre_id              
        generated_id = self._next_id
 #Aqui le asignamos la operacion matematica += 1 Esto es para que vaya sumando los id de los objetos segun lo vas introducien en uno mas     
        self._next_id += 1
        return generated_id
    
 # Asigna un ID único al miembro  
    def add_member(self, member):
        member['id'] = self._generate_id() 
# Asegura que el apellido sea 'Jackson'         
        member['last_name'] = self.last_name  
        self._members.append(member)
        return member

    def delete_member(self, id):
        for member in self._members:
            if member['id'] == id: 
                self._members.remove(member)
                return {"done":True}

    def get_member(self, id_numbers):
        for member in self._members:
            if member[id] == id:
                return member
        return None

    def get_all_members(self):
        return self._members