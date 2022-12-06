#se usa class para definir una clase
class Usuario:
    def __init__(self, nombre, apellido):  #la funcion __init__ es un metodo especial de clase de python que reemplaza al metodo que habiamos hecho en un concepto anterior.
        self.nombre = nombre #self será la referencia al momento de hacer las instancias separadas para que cada instancia pueda tener valores diferentes
        self.apellido = apellido

    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)

usuario = Usuario("Julio Cesar", "LM")

usuario.saludo()

# class Admin(Usuario):
#     def superSaludo(self):
#         print('Hola!, me llamo,', self.nombre, ' y soy administrador')

# # usuario = Usuario('Felipe', 'Feliz')

# # usuario.saludo()
# # usuario.nombre = 'Chanchito'
# # usuario.saludo()
# # # del usuario.nombre
# # # del usuario
# # # print(usuario)

# # admin = Admin('Super', 'Feliz')
# # admin.saludo()
# # admin.superSaludo()

# # usuario.superSaludo()

# class Animal:
#     def __init__(self, nombre, onomatopeya):
#         self.nombre = nombre
#         self.onomatopeya = onomatopeya
#     def saludo(self):
#         print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

# class Gato(Animal):
#     tipo = 'gato'
#     def __init__(self, nombre, onomatopeya):
#         Animal.__init__(self, nombre, onomatopeya)
#         print('Hola, soy un gato extendido!')

# class Perro(Animal):
#     tipo = 'perro'
#     def __init__(self, nombre, onomatopeya):
#         super().__init__(nombre, onomatopeya)
#         print('instanciando un perro')

# class Canario(Animal):
#     tipo = 'canario'

# gato = Gato('Fluffy', 'maullido')
# gato.saludo()

# perro = Perro('Firulais', 'ladrido')
# perro.saludo()

# canario = Canario('Piolin', 'silvido')
# canario.saludo()
