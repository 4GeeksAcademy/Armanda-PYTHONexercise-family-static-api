
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint



    
     # Este método genera un 'id' único al agregar miembros a la lista 
    def _age_id(self, age):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member['id'] = self._generate_id('jackson')  # Asigna un ID único al miembro
        member['last_name'] = self.last_name  # Asegura que el apellido sea 'Jackson'
        self._members.append(member)

    def delete_member(self, name):
        self._members = [member for member in self._members if member['id'] != id']

    def get_member(self, id_numbers):
        for member in self._members:
            if member[id] == id:
                return member
        return None

    def get_all_members(self):
        return self._members