class Library:
	def __init__(self,list_of_books,library_name):
		self.list_of_books=list_of_books
		self.library_name=library_name
		self.lend_data={}

		for book in self.list_of_books:
			self.lend_data[book]=None

	def display_books(self):
		for book in self.list_of_books:
			print("     ",book)

	def add_book(self,name_of_book,name_of_person):
		self.list_of_books.append(name_of_book)
		self.lend_data[name_of_book]=None
		self.book_added_by=name_of_book
		print("   Succesfully Added book......\n") 

	def lend_book(self,name_of_book,name_of_person):
		if name_of_book in self.list_of_books:
			if self.lend_data[name_of_book] == None:
				self.lend_data[name_of_book]=name_of_person
				# self.list_of_books.remove(name_of_book)
			else :
				print(f"Book is not available\n taken by {self.lend_data[name_of_book]}")
		else:
			print("Enter valid book name")

		print("   Succesfully Lended book......\n")			

	def return_book(self,name_of_book):
		if name_of_book in self.list_of_books:
			if self.lend_data[name_of_book] != None:
				self.lend_data[name_of_book]=None
			else:
				print("Sorry, the book is not taken/lend")
		else:
			print("Please enter the valid book name")

		print("   Succesfully Return book......\n")

	def delete_book(self,name_of_book):
		if self.lend_data[name_of_book] == None:
			self.list_of_books.remove(name_of_book)
			self.lend_data.pop(name_of_book)
		else:
			print("Book is lend by an user")	

		print("   Succesfully Deleted book......\n")

	
	def print_dict(self):
		print(self.lend_data)	


def main():
	books = ['In Search of Lost Time','The Great Gatsby','War and Peace','Pride and Prejudice','To Kill a Mockingbird','In Cold Blood','chacha chaudhary','taarak metha','ram and shyam','introduction to algorithm']
	mohit=Library(books,'mohit_library')

	security_key= 'please_delete'
	print("_______       Welcome to Bharti Library      _______\n")
	i=1
	print("Books in Library :")
	for book in books:
		print(f"{i}. {book}")
		i+=1
	# print("Books in Library :\n    chacha chaudhary , taarak metha\n    introduction to algorithm , ram and shyam\n")
	print("       press 'dis' to Dilplay Books\n       press 'delete' to Deleta a BOOK\n       press 'lend' to Lend BOOK\n       Press 'return' to Return Book\n       Press 'add' to Add Book\n       Press 'end' to Exit\n       Press 'show' to see dictionary ")

	while (True):
		x=input("Type now...")
		if x=='end':
			break
		elif x=='dis':
			mohit.display_books()
		elif x=='lend' :
			a=input("Please Enter name of book\n")
			b=input("Please Enter Your name\n")
			mohit.lend_book(a,b)
		elif x=='add':
			a=input("Please Enter name of book\n")
			b=input("Please Enter Your name\n")
			mohit.add_book(a,b)
			
		elif x=='return':
			a=input("Please Enter name of book\n")
			mohit.return_book(a)
			
		elif x=='show':
			mohit.print_dict()
		
		elif x=='delete':
			j=input("Enter the Security Key\n")
			if j==security_key:
				book=input("Enter name of Book\n")
				if book in books:
					mohit.delete_book(book)
					
				else:
					print("Enter valid book name")
			else:
				print("Wrong security key entered..")

				

		else:
			print(" Enter valid Input or Exit......")	
			
		pass


if __name__ == '__main__':
		main()	
