from author import Author
from book import BOOK
from libary import Libary

au1 = Author("Ahmad", "68884548", "ahmadhg@gmail.com", "25")
au2 = Author("Ruba", "78564545", "rubakg@gmail.com", "28")
au3 = Author("Alaa", "745845244", "alaaog@gmail.com", "26")
au4 = Author("Hashem", "465845465", "hashemlg@gmail.com", "29")
au5 = Author("Banan", "85446486", "bananghourab@gmail.com", "30")
au6 = Author("Mohammed", "854545455", "mohammedjk@gmail.com", "40")

book1 = BOOK("JAVA", "09-09-2009", 1, au1.id)
book2 = BOOK("PYTHON", "10-10-2010", 2, au2.id)
book3 = BOOK("PHP", "11-11-2011", 3, au3.id)
book4 = BOOK("C#", "12-12-2012", 4, au4.id)
book5 = BOOK("JAVASCRIPT", "08-08-2009", 5, au1.id)
book6 = BOOK("LOGIC", "13-10-2010", 6, au3.id)
book7 = BOOK("HTML", "06-06-2011", 7, au6.id)
book8 = BOOK("CSS", "01-01-2012", 8, au5.id)

Lib = Libary()

Lib.add_author(au1)
Lib.add_author(au2)
Lib.add_author(au3)
Lib.add_author(au4)
Lib.add_author(au5)
Lib.add_author(au6)

Lib.add_book(book1)
Lib.add_book(book2)
Lib.add_book(book3)
Lib.add_book(book4)
Lib.add_book(book5)
Lib.add_book(book6)
Lib.add_book(book7)
Lib.add_book(book8)

for author in Lib.Author:
    print("name : ", author.name, "phone : ", author.phone, "Email :", author.Email, "age", author.age)

Lib.remove_author(au6.id)

for author in Lib.Author:
    print("name : ", author.name, "phone : ", author.phone, "Email :", author.Email, "age", author.age)
Lib.print_authors()

Lib.print_books()
Lib.remove_book(book1.id)
Lib.print_books()

Lib.print_author_books(au1.id)
