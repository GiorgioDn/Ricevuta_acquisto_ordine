class Negozio:
    def __init__(self, nome:str, recapito:str, prodotti:dict = {}):
        self.nome = nome
        self.recapito = recapito
        self.prodotti = prodotti
        
    def prendi_prodotto(self, prodotto:str):
        return self.prodotti[prodotto]
    
    def menu_prodotti(self):
        for key, value in self.prodotti.items():
            print(f"Prodotto {key} - Costo: {value[0]} - Quantita: {value[1]}")
            
    def compra_quantita(self, prodotto:str, quantita:int):
        if prodotto in self.prodotti.keys():   
            self.prodotti[prodotto] -= quantita
    
    def restituisci_quantita(self, prodotto:str, quantita:int):
        if prodotto in self.prodotti.keys():   
            self.prodotti[prodotto] += quantita