class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo={self.info[0]}, autor={self.info[1]}, categoria={self.categoria}, ISBN={self.isbn})"

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados al usuario

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, ID={self.user_id}, Libros Prestados={self.libros_prestados})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con ISBN como clave
        self.usuarios = {}  # Diccionario de usuarios con user_id como clave
        self.usuarios_ids = set()  # Conjunto para manejar IDs únicos

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios_ids:
            self.usuarios[usuario.user_id] = usuario
            self.usuarios_ids.add(usuario.user_id)

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.usuarios_ids.remove(user_id)

    def prestar_libro(self, user_id, isbn):
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros.pop(isbn)  # Quita el libro de la colección disponible
            self.usuarios[user_id].prestar_libro(libro)

    def devolver_libro(self, user_id, libro):
        if user_id in self.usuarios:
            self.usuarios[user_id].devolver_libro(libro)
            self.añadir_libro(libro)  # Añade el libro de nuevo a la colección disponible

    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, clave, None) == valor for clave, valor in kwargs.items()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            return self.usuarios[user_id].libros_prestados
        else:
            return "Usuario no encontrado."

# Pruebas del sistema
if __name__ == "__main__":
    # Creación de objetos de libros
    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Ficción", "1234567890")
    libro2 = Libro("1984", "George Orwell", "Ficción distópica", "0987654321")

    # Creación de objetos de usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("Ana López", "002")

    # Creación de la biblioteca y operaciones
    biblioteca = Biblioteca()
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar un libro
    biblioteca.prestar_libro("001", "1234567890")
    print(biblioteca.listar_libros_prestados("001"))

    # Devolver un libro
    biblioteca.devolver_libro("001", libro1)
    print(biblioteca.listar_libros_prestados("001"))

    # Buscar libros por categoría
    print(biblioteca.buscar_libro(categoria="Ficción distópica"))
