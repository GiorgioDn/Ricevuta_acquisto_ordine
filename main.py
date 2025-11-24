from module.utente import *
from module.Negozio import *

def main():
    
    salvadanaio = Salvadanaio(100)
    
    utente = Utente("me", "me", 18, "salve", "34999", salvadanaio)
    
    prodotto_1 = Prodotto("computer", 10.0, 10)
    prodotto_2 = Prodotto("cuffie", 10.0, 20)
    
    prodotti = [prodotto_1, prodotto_2]
    
    negozio = Negozio("negozio", "negozio", prodotti)
    
    #apre il file per verificare l'utente
    file = open("ricevuta.txt", "r")
    #il metodo strip rimuove gli spazi bianchi
    riga = file.readline().strip()
    file.close()
    #controlla se l'email è dell'utente corrente
    if riga != utente.email:    
        file = open ("ricevuta.txt", "w")
        string = f"{utente.email}\n"
        file.write(string)
        file.close()
    
    while True:
           
        print("\n Che operazione si vuole effettuare nel negozio")
        print("1. Cercare un prodotto")
        print("2. Vedere i prodotti")
        print("3. Acquistare un prodotto")
        print("4. Ordinare un prodotto")
        print("5. Esci")
        chooice = int(input("Scegli una opzione: "))
        
        match chooice:
            case 1:
                prodotto = input("Che prodotto stai cercando: ")
                prodotto = negozio.cerca_prodotto(prodotto)
                
                negozio.cerca_prodotto(prodotto)
                    
            case 2:
                negozio.menu_prodotti()
            case 3:
                prodotto = input("Che prodotto vuoi acquistare: ")
                quantita = int(input("Quanti ne vuoi acquistare: "))
                
                for n in negozio.get_prodotti():
                    if n.get_nome() == prodotto:
                        if utente.richiesta_acquisto(n.get_prezzo()) == True:
                            if negozio.compra_quantita(prodotto, quantita) == True:
                                string = f"Ricevuta acquisto prodotto: {prodotto}, per {utente.nome} {utente.cognome}\n"                    
                                with open ("ricevuta.txt", "a") as file:
                                    file.write(string)
            case 4:
                prodotto = input("Che prodotto vuoi ordinare: ")
                quantita = int(input("Quanti ne vuoi ordinare: "))
                
                for n in negozio.get_prodotti():
                    if n.get_nome() == prodotto:
                        if utente.richiesta_acquisto(n.get_prezzo()) == True:
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