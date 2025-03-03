class library:

    def _init_(self, list_of_books, name):
        self.bookList = list_of_books
        self.name = name
        self.lendDict = {}

        def displayBooks(self):
            print(f"We have the following books in our library: {self.name}")
            for book in self.booksList:
                print(book)

        def lendBook(self, user, book):
            if book not in self.booksList:
                print("Sorry, we do not have that book.")   
            elif book in self.lendDict:
                print(f"The book is already being used by {self.lendDict[book]}")
            else:
                self.lendDict[book] = user
                print(
                    "Lender-Book database has been updated. You can take the book now."
                )  

        def addBook(self, book):
            self.booksList.append(book)
            print(f"{book} has been added to the book list.")    

        def returnBook(self, book):
            if book in self.lendDict:
                print("Book has been returned")
            else:
                print("That book wasn't borrowed from us.")

    if _name_== '_main_':        
    books = library([
        'python','Rich Dad Poor Dad ', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'
        "lET'S Upskill"
    ], )
    user_name = input("Welcome to our library! Please enter your name:")

    while True:
        print(
            f"\nHello {user_name}, Welcome to the {books.name} library. Please choose an option"
        )

        print(
            "1. Display Books\n2. Lend a Boook\n3. Add a Book\n4. Return a Book\n5. Quit"
        )
        user_choice not in ["Enter your choice to comtinue: "]

        if user_choice not in ['1','2', '3 ', '4', '5']:
            print("Plkease enter a valid option.")
            continue

        if user_choice == '1':
            books.diplayBooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend:")   
            books.lendBook(user_name, book)

        elif user_choice == '2':
            book = input("Enter the name of the book you want to add:")   
            books.lendBook(user_name, book)   

        elif user_choice == '4':
            book = input("Enter the name of the book you want to ruturn :")   
            books.lendBook(user_name, book)    

        elif user_choice == '5':
           print(f"Thank oyu for using the library, (user_name). Goodbye!")
           break
          