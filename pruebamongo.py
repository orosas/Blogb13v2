from pymongo import MongoClient
import pprint

cliente = MongoClient('localhost', 27017)
db = cliente.booksdb
books = db.books

class Book(object):

	def __init__(self, name, author, published, cover, tags):

		self.name = name
		self.author = author
		self.published = published
		self.cover = cover
		self.tags = tags

class Author(object):

	def __init__(self, name, lastname, age, nationality):

		self.name = name
		self.lastname = lastname
		self.age = age
		self.nationality = nationality

def save_book():

	name_autor = input("Nombre del Autor?: ")
	lastname_autor = input("Apellidos delautor?: ")
	age_autor = input("Edad del autor?: ")
	nationality_autor = input("Nacionalidad del Autor?: ")
	name_book = input("Nombre del libro?: ")
	published_book = input("Fecha de publicación?: ")
	cover_book = input("Caratula del libro?: ")
	tags = input("Tags para el libro?: ")

	autor = Author(name_autor, lastname_autor, age_autor, nationality_autor)

	tags_list = tags.split(',')

	book = Book(name_book, autor.__dict__, published_book, cover_book, tags_list)

	books_id = books.insert_one(book.__dict__).inserted_id
	print("Tu libro se guardó con el id %s" % books_id)


def list_books():
	for book in books.find():
		pprint.pprint(book)

def search_book(book):
	book = books.find_one({'name':book})
	if book :
		print("Tu libro es:")
		pprint.pprint(book)
	else:
		print("No se encontró el libro")

def edit_book(campo,nuevo_valor):
	pass
	print(" ")
	print("***********************")
	print("Selecciona una opción para editar: ")

	#books_list = books.find()

	count = 0
	books_list = []

	for book in books.find():
		count+= 1
		books_list.append(book)
		print("%s .- %s" % (str(count), book['name']))
		#print(book['name'])
	print(" ")
	print("***********************")

	# seleccionar id para borrar
	element_id = input("Libro a Borrar ---> ")
	element_id = int(element_id)




def delete_book():
	#print("***********************")
	#print("Los Libros guardados son: ")
	print(" ")
	print("***********************")
	print("Selecciona una opción para borrar: ")

	#books_list = books.find()

	count = 0
	books_list = []

	for book in books.find():
		count+= 1
		books_list.append(book)
		print("%s .- %s" % (str(count), book['name']))
		#print(book['name'])
	print(" ")
	print("***********************")

	# seleccionar id para borrar
	element_id = input("Libro a Borrar ---> ")
	element_id = int(element_id)
	book = books_list[element_id-1]
	books.delete_one({'_id': book['_id']})
	print(" ")
	print("Elemento borrado ")
	print("\n")





if __name__ == '__main__':
	print("----------- Ejemplo Mongo & Python--------------")
	loop = True
	while loop:
		print("Selecciona una opción")
		print("1:Guardar Libro")
		print("2: Ver todos los libros")
		print("3: Buscar libro")
		print("4: Borrar libro: ")
		print("Cualquier Letra Para Salir")
		choice = input("----> ")
		choice = int(choice)
		if choice is 1:
			save_book()
		elif choice is 2:
			list_books()
		elif choice is 3:
			book = input("¿Cuál libro?: ")
			search_book(book)
		elif choice is 4:
			delete_book()
		else:
			loop = False