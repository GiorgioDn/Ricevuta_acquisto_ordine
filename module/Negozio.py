class Prodotto:
    def __init__(self, nome:str, prezzo:float, quantita:int):
        self.__nome = nome
        self.__prezzo = prezzo
        self.__quantita = quantita
        
    #getter
    def get_nome(self):
        return self.__nome

    def get_prezzo(self):
        return self.__prezzo
    
    def get_quantita(self):
        return self.__quantita
    
    #setter
    def set_nome(self, value:str):
        self.__nome = value

    def set_prezzo(self, prezzo:float):
        self.__prezzo = prezzo
    
    def set_quantita(self, quantita:int):
        self.__quantita = quantita

class Negozio:
    #prende in input due stringhe ed un dizionario
    def __init__(self, nome:str, recapito:str, prodotti:list[Prodotto] = []):
        self.__nome = nome
        self.__recapito = recapito
        self.__prodotti = prodotti
        
    #getter
    def get_nome(self):
        return self.__nome
    
    def get_recapito(self):
        return self.__recapito
    
    def get_prodotti(self):
        return self.__prodotti
        
    #setter
    def set_nome(self, value:str):
        self.__nome = value
        
    def set_recapito(self, value:str):
        self.__recapito = value
    
    #aggiunge prodotti
    def add_prodotti(self, value:Prodotto):
        self.__prodotti.append(value)
    
    #restituisce i valori della chiave prodotto
    def cerca_prodotto(self, prodotto:str):
        for n in self.get_prodotti():
            if n.get_nome() == prodotto:
                print(f"Prodotto {n.get_nome()} - Costo: {n.get_prezzo()} - Quantita: {n.get_quantita()}")
                return True
    
    #stampa le chiavi e valori del dizionario
    def menu_prodotti(self):
        for n in self.get_prodotti():
            print(f"Prodotto {n.get_nome()} - Costo: {n.get_prezzo()} - Quantita: {n.get_quantita()}")
   
    #riduce la quantità del prodotto disponibile      
    def compra_quantita(self, prodotto:str, quantita:int):
        for n in self.get_prodotti():
            if n.get_nome() == prodotto:
                if quantita <= n.get_quantita():
                    quantita = n.get_quantita()
                    quantita -=1
                    n.set_quantita(quantita)
                    return True
                
        return False
        
    #aumenta la quantità del prodotto disponibile 
    def restituisci_quantita(self, prodotto:str, quantita:int):
        for n in self.get_prodotti():
            if n.get_nome() == prodotto:
                if quantita <= n.get_quantita():
                    quantita = n.get_quantita()
                    quantita +=1
                    n.set_quantita(quantita)
                    return True
        
        return False
        