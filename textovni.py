from model import Igrica

nova_igra = 'n'

while nova_igra == "n":
    trenutna_igra = Igrica()

    # print(trenutna_igra)

    while True:
        trenutna_igra.izpis_igre()
        print(f"na vrsti je igralec {trenutna_igra.igralec}")

        while True:
            print("Napiši št:  ")
            polje = input()
            poteza = trenutna_igra.shrani_potezo(polje)
            if poteza:
                break

        if trenutna_igra.zmaga() != False:
            print(f"Zmagovalec je {trenutna_igra.zmaga()}")
            print("!!!!!!!!!!!!!!")
            trenutna_igra.izpis_igre()
            print("!!!!!!!!!!!!!!")
            break

        if trenutna_igra.neodloceno():
            print("Neodloceno")
            break

        trenutna_igra.menjava_igralcev()

    print("Igre je konec")
    nova_igra = input("Pritisnite N za novo igro: ")

print("KONEC PROGRAMA")