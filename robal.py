import random
import sys

def find_index(word, let) -> int:
    indexes = []
    for index, let_in_word in enumerate(word):
        if let == let_in_word:
            indexes.append(index)
    return indexes

def imp_haslo() -> str:
    try: 
        plik = open("hasla.txt")
    except FileNotFoundError:
        #TODO
        plik = open("hasla.txt", "w")
        print("Wystąpił błąd - brak dostępnych haseł. Uruchom program ponownie i przejdź do ustawień, aby dodać nowe hasła.")
        plik.close()
        sys.exit(0)

    try:
        lista_slow = plik.readlines()
        # można też: lista_slow = file("hasla.txt").readlines() ???
        plik.close()
        i_haslo = random.choice(lista_slow).strip().upper()
        return i_haslo
    except:
         print("Wystąpił błąd - brak dostępnych haseł. Uruchom program ponownie i przejdź do ustawień, aby dodać nowe hasła.")
         sys.exit(0)

def spr(s_haslo) -> int:
	#ec - kod błędu
	ec = 0
	if len(s_haslo) > 50:
		ec = 1
	elif len(s_haslo) < 10:
		ec = 2
	else:
		for _ in s_haslo:
			if _.isdigit():
				ec = 3
				break
			
	return ec
			
				
def dodaj(d_haslo):				
	file = open("hasla.txt", "a")
	file.write("\n" + d_haslo)

def wyswietl():
	file = open("hasla.txt")
	for line in file:
		print(line.strip())


if __name__ == "__main__":
    w1 = 0
    print("ZAGRAJ W ROBALA!")
    input()

    while w1 != "3": #żeby zawsze wracał do menu głównego

        print("Wybierz:\n1 aby zagrać\n2 aby przejść do ustawień\n3 aby wyjść")
        w1 = input()

        if w1 == "1":
            haslo = imp_haslo()
            pp = 3

            #odgadnięte litery
            o_litery = []
            #użyte litery
            u_litery = []



            for znak in haslo:
                if znak == " ":
                    o_litery.append(" ")
                else:
                    o_litery.append("_")

            while True:

                #drukowane na początku każdej pętli
                print("Zgadnij hasło")
                for _ in o_litery:
                    print(_, end = " ")
                print()
                print("Pozostałe próby: " + str(pp))
                print("Użyte litery:")
                for _ in u_litery:
                    print(_ + ",", end=" ")
                spr_lit = input("Wprowadź literę: ").upper()

                #jeśli gracz jest gamoniem i nie wie, co to litera
                while len(spr_lit) != 1 or spr_lit == " " or spr_lit.isdigit():
                    spr_lit = input("Nieprawidłowa wartość. Wprowadź jedną literę: ").upper()
                while spr_lit in u_litery:
                    spr_lit = input("Litera już użyta, wprowadź inną: ").upper()
                u_litery.append(spr_lit)

                #sprawdzanie litery
                index = find_index(haslo, spr_lit)
                if len(index) == 0:
                    print("Zła odpowiedź!")
                    pp -= 1

                    if pp < 0:
                        print("PRZEGRAŁEŚ x.x Hasło to: " + haslo)
                        break

                else:
                    for _ in index:
                        o_litery[_] = spr_lit
                        

                    if "_" not in o_litery:
                        print("GRATULACJE, WYGRAŁEŚ! <3")
                        print(haslo)
                        break

                
                
        if w1 == "2":
             
            w2 = 0

            while w2 != "2":
                
                print("Wprowadź nowe hasło lub wpisz:")
                print("1 aby wyświetlić listę haseł")
                print("2 aby powrócić do Menu")
                
                w2 = input()
                
                if w2 == "1":
                    wyswietl()
                    
                elif w2 != "0" and w2 != "1":
                    ec = spr(w2)
                    if ec == 1:
                        print("Hasło zbyt długie! Maksymalna długość hasła to 50 znaków.")
                    elif ec == 2:
                        print("Hasło zbyt krótkie! Minimalna długość hasła to 10 znaków.")
                    elif ec == 3:
                        print("Hasło nie może zawierać cyfr!")
                    if ec == 0:
                        dodaj(w2)
         

    if w1 == "3":
	    sys.exit(0)
