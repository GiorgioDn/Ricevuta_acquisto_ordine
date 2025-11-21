class Negozio:
    #prende in input due stringhe ed un dizionario
    def __init__(self, nome:str, recapito:str, prodotti:dict = {}):
        self.nome = nome
        self.recapito = recapito
        self.prodotti = prodotti
        
    #restituisce i valori della chiave prodotto
    def cerca_prodotto(self, prodotto:str):
        return self.prodotti[prodotto]
    
    #stampa le chiavi e valori del dizionario
    def menu_prodotti(self):
        for key, value in self.prodotti.items():
            print(f"Prodotto {key} - Costo: {value[0]} - Quantita: {value[1]}")
   
    #riduce la quantità del prodotto disponibile      
    def compra_quantita(self, prodotto:str, quantita:int):
        if prodotto in self.prodotti.keys():
            prodotto = self.prodotti[prodotto]
            if quantita <= prodotto[1]:
                prodotto[1]-= quantita
                return True
        else:
            return False
    
    #aumenta la quantità del prodotto disponibile 
    def restituisci_quantita(self, prodotto:str, quantita:int):
        if prodotto in self.prodotti.keys():
            prodotto = self.prodotti[prodotto]
            if quantita <= prodotto[1]:
                prodotto[1]+= quantita
                return True
        else:
            return False