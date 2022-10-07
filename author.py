class Author:
    __id_author = 0

    def __init__(self, name, phone, Email, age):
        Author.__id_author += 1
        self.id = Author.__id_author
        self.name = name
        self.phone = phone
        self.Email = Email
        self.age = age


au1 = Author("Ahmad", "68884548", "ahmadhg@gmail.com", "25")
au2 = Author("Ruba", "78564545", "rubakg@gmail.com", "28")
au3 = Author("Alaa", "745845244", "alaaog@gmail.com", "26")
au4 = Author("Hashem", "465845465", "hashemlg@gmail.com", "29")
au5 = Author("Banan", "85446486", "bananghourab@gmail.com", "30")
au6 = Author("Mohammed", "854545455", "mohammedjk@gmail.com", "40")

print(au1.id)
print(au2.id)
print(au3.id)
print(au4.id)
print(au5.id)
print(au6.id)
