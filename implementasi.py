class PerpusItem :
    def __init__(self, judul, subjek) :
        self.judul = judul
        self.subjek = subjek

    def lokasi_penyimpan(self) :
        pass
    
    def info(self) :
        pass

class Katalog :
    def cari(self) :
        pass

class Buku (PerpusItem) :
    def __init__(self, judul, subjek, ISBN, pengarang, jmlHal, ukuran) :
        super().__init__(judul, subjek)
        self.ISBN = ISBN
        self.pengarang = pengarang
        self.jmlHal = jmlHal
        self.ukuran = ukuran

class Majalah (PerpusItem) :
    def __init__(self, judul, subjek, volume, issu) :
        super().__init__(judul, subjek)
        self.volume = volume
        self.issu = issu

class DVD (PerpusItem) :
    def __init__(self, judul, subjek, aktor, genre) :
        super().__init__(judul,subjek)
        self.aktor = aktor
        self.genre = genre

class Pengarang () :
    def __init__(self, nama) :
        self.nama = nama

    def info(self) :
        pass

    def cari(self) :
        pass

    katalog_1 = Katalog()
    katalog_2 = Katalog()
    katalog_3 = Katalog()

    perpus_item_1 = PerpusItem("Bahasa", katalog_1)
    perpus_item_2 = PerpusItem("Matematika", katalog_2)
    perpus_item_3 = PerpusItem("Statiska", katalog_3)

    buku_1 = Buku("Bahasa", katalog_1, "123-456-100")
    buku_2 = Buku("Matematika", katalog_2,"123-456-101")
    buku_3 = Buku("Statiska", katalog_3,"123-456-103")

    majalah_1 = Majalah("Bumi Manusia", katalog_1, 1, 1)
    majalah_2 = Majalah("Tere Liye", katalog_2, 1, 2)
    majalah_3 = Majalah("Dilan 1990", katalog_3, 1, 3)

    DVD_1 = DVD("horor", ["rara", "riri", "rere"], "horor") 
    DVD_2 = DVD("romance",["widi", "wida", "wilda"], "romance")
    DVD_3 = DVD("komedi", ["pee mak", "tia", "tio", "tiur"], "komedi")

    print()
    katalog_1.info()
    print()
    katalog_1.cari("Bahasa")
    katalog_2.cari("Matematika")
    print()
    buku_1.info()
    print()
    majalah_1.info()
    print()
    DVD_1.info()












