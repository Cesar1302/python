#se usa class para definir una clase
class Usuario:
    def __init__(self, nombre, apellido):  #la funcion __init__ es un metodo especial de clase de python que reemplaza al metodo que habiamos hecho en un concepto anterior.
        self.nombre = nombre #self será la referencia al momento de hacer las instancias separadas para que cada instancia pueda tener valores diferentes
        self.apellido = apellido

    def saludo(self): #debemos colocar self dentro del parentesis para que funcionen las referencias
        print('Hola!, mi nombre es', self.nombre, self.apellido)

    def sadulo2(self):
        print("hola, mi nombre es:", self.nombre, "y mi apellido es:", self.apellido)
        
usuario = Usuario("Julio Cesar", "LM")

usuario.saludo()
usuario.sadulo2()




class Admin(Usuario):
    def superSaludo(self):
        print('Hola!, me llamo,', self.nombre, ' y soy administrador')

usuario = Usuario('Felipe', 'Feliz')

usuario.saludo()
usuario.nombre = 'Chanchito' #podemos renormbrar las propiedades de las instancias de esta manera
usuario.saludo()
#del usuario.nombre # de esta forma quitamos propiedades a una instancia
#del usuario # esto elimina un objeto por completo
#print(usuario)

#Ya vamos a pasar a las herencias, es un concepto en Programacion orientada a objetos para reutilizar lo maximo posible un codigo donde la estructura sea muy similar
class Admin(Usuario):
    def supersaludo(self):
        print("hola mi nombre es:", self.nombre, "y soy desarrollador, me apellido", self.apellido)

admin = Admin("Cesar", "Libreros")
admin.supersaludo()


# usuario.superSaludo() # esta accion no se puede ejecutar porque las acciones de la clase padre no se pueden ejecutar con una clase hijo

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)
    def saludote(self):
        print("hola, soy un", self.tipo, "me llamo",self.nombre, "y hago", self.onomatopeya)


class Nina(Animal):
    tipo="minina"

class Byron(Animal):
    tipo="perro poderoso"

class Luna(Animal):
    tipo="favorita de mamá"


nina=Nina("Nina", "miau")
nina.saludo()
nina.saludote()

byron=Byron("Byron", "guau")
byron.saludo()
byron.saludote()

luna=Luna("Lunita","buff")
luna.saludo()
luna.saludote()

# Extendiendo el init de la clase padre

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):  # al volver a llamar el init, el init anterior (de la clase padre) no se ejecutara
        Animal.__init__(self, nombre, onomatopeya) # cuando se define el init de la clase animal, para que se ejecute de todas maneras debemos mencionar a la clase padre () y volver a llamar init y los mismos argumentos que nececita el metodo de su clase padre incluyento los argumentos
        print('Hola, soy un gato extendido!')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya) # super hace referencia siempre a la clase padre, en este caso la clase animal y ya no hace falta pasar la referencia de la instancia self
        print('instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()
