from module.utente import *
from module.Negozio import *

def main():
    
    salvadanaio = Salvadanaio(100)
    
    utente = Utente("me", "me", 18, "ciao", "34999", salvadanaio)
    
    prodotti = {
        "computer": [50, 10],
        "cuffie":[10, 30]
    }
    
    negozio = Negozio("negozio", "negozio", prodotti)
    
    while True:
           
        print("\n Che operazione si vuole effettuare nel negozio")
        print("1. Cercare un prodotto")
        print("2. Vedere i prodotti")
        print("3. Acquistare un prodotto")
        print("4. Ordinare un prodotto")
        print("5. Esci")
        chooice = int(input("Scegli una opzione: "))
        
        '''
        file = open("ricevuta.txt", "r")
        riga = file.readline()
        file.close()
        if riga == utente.cognome:    
            with open ("ricevuta.txt", "a") as file:
                file.write(string)
        '''
        
        match chooice:
            case 1:
                prodotto = input("Che prodotto stai cercando: ")
                print(negozio.cerca_prodotto(prodotto))
            case 2:
                negozio.menu_prodotti()
            case 3:
                prodotto = input("Che prodotto vuoi acquistare: ")
                quantita = int(input("Quanti ne vuoi acquistare: "))
                
                prodotto_1 = negozio.cerca_prodotto(prodotto)
                
                if utente.richiesta_acquisto(prodotto_1[0]) == True:
                    if negozio.compra_quantita(prodotto, quantita) == True:
                        string = f"Ricevuta acquisto prodotto: {prodotto}, per {utente.nome} {utente.cognome}\n"                    
                        with open ("ricevuta.txt", "a") as file:
                            file.write(string)
            case 4:
                prodotto = input("Che prodotto vuoi ordinare: ")
                quantita = int(input("Quanti ne vuoi ordinare: "))
                
                prodotto = negozio.cerca_prodotto(prodotto)
                
                if utente.richiesta_acquisto(prodotto_1[0]) == True:
                    if negozio.compra_quantita(prodotto, quantita) == True:
                        string = f"Ricevuta ordine prodotto: {prodotto}, per {utente.email}, in via: {utente.recapito}\n"
                        with open ("ricevuta.txt", "a") as file:
                            file.write(string)
            case 5:
                break
            case _:
                print("Scelta non valida")
                
if __name__ == "__main__":
    main()
else: 
    print("È stato importato")