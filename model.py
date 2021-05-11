class Igrica:

    def __init__(self, igralec='X'):
        self.igralec = igralec
        self.plosca = ["-", "-", "-", "-",
                       "-", "-", "-", "-",
                       "-", "-", "-", "-",
                       "-", "-", "-", "-"]

    # plosca
    # 0  1  2  3
    # 4  5  6  7
    # 8  9  10 11
    # 12 13 14 15

    def izpis_igre(self, stevilo=1):
        print(f"{self.plosca[0]} | {self.plosca[1]} | {self.plosca[2]} | {self.plosca[3]}")
        print("--------------")
        print(f"{self.plosca[4]} | {self.plosca[5]} | {self.plosca[6]} | {self.plosca[7]}")
        print("--------------")
        print(f"{self.plosca[8]} | {self.plosca[9]} | {self.plosca[10]} | {self.plosca[11]}")
        print("--------------")
        print(f"{self.plosca[12]} | {self.plosca[13]} | {self.plosca[14]} | {self.plosca[15]}")
        print("########################")

    def shrani_potezo(self, polje):
        if self.napacna_poteza(polje):
            return False
        # vemo da so polja cifre, mormo odštet nko da dobimo od 0-15 in ne 0-14
        polje = int(polje) - 1
        if self.ponovljena_poteza(polje):
            return False

        self.plosca[polje] = self.igralec
        return True

    def napacna_poteza(self, polje):
        if polje not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13","14", "15" ]:
            print("Nepravilen vnos")
            return True
        return False

    def ponovljena_poteza(self, polje):
        if self.plosca[polje] != '-':  # - je že spremenjen zato različen od -
            print("Polje je že zasedeno")
            return True
        return False

    # zmaga,poraz
    def preveri_situacijo(self):
        self.zmaga()
        self.neodloceno()

    #    matrika = self.matrika

    def zmaga(self):
        # 2 različni na vrstico
        if self.plosca[0] == self.plosca[1] == self.plosca[2] != '-':
            return self.igralec
        elif self.plosca[1] == self.plosca[2] == self.plosca[3] != '-':
            return self.igralec
        elif self.plosca[4] == self.plosca[5] == self.plosca[6] != '-':
            return self.igralec
        elif self.plosca[5] == self.plosca[6] == self.plosca[7] != '-':
            return self.igralec
        elif self.plosca[8] == self.plosca[9] == self.plosca[10] != '-':
            return self.igralec
        elif self.plosca[9] == self.plosca[10] == self.plosca[11] != '-':
            return self.igralec
        elif self.plosca[12] == self.plosca[13] == self.plosca[14] != '-':
            return self.igralec
        elif self.plosca[13] == self.plosca[14] == self.plosca[15] != '-':
            return self.igralec
        # stolpci
        elif self.plosca[0] == self.plosca[4] == self.plosca[8] != '-':
            return self.igralec
        elif self.plosca[4] == self.plosca[8] == self.plosca[12] != '-':
            return self.igralec
        elif self.plosca[1] == self.plosca[5] == self.plosca[9] != '-':
            return self.igralec
        elif self.plosca[1] == self.plosca[9] == self.plosca[13] != '-':
            return self.igralec
        elif self.plosca[2] == self.plosca[6] == self.plosca[10] != '-':
            return self.igralec
        elif self.plosca[6] == self.plosca[10] == self.plosca[14] != '-':
            return self.igralec
        elif self.plosca[3] == self.plosca[7] == self.plosca[11] != '-':
            return self.igralec
        elif self.plosca[7] == self.plosca[11] == self.plosca[15] != '-':
            return self.igralec
        # diagonale
        elif self.plosca[8] == self.plosca[5] == self.plosca[2] != '-':
            return self.igralec
        elif self.plosca[1] == self.plosca[6] == self.plosca[11] != '-':
            return self.igralec
        elif self.plosca[4] == self.plosca[9] == self.plosca[14] != '-':
            return self.igralec
        elif self.plosca[13] == self.plosca[10] == self.plosca[7] != '-':
            return self.igralec
        elif self.plosca[12] == self.plosca[9] == self.plosca[6] != '-':
            return self.igralec
        elif self.plosca[9] == self.plosca[6] == self.plosca[3] != '-':
            return self.igralec
        return False

    def neodloceno(self):
        if '-' not in self.plosca:
            return True
        return False

    def menjava_igralcev(self):
        if self.igralec == "X":
            self.igralec = "O"
        elif self.igralec == "O":
            self.igralec = "X"