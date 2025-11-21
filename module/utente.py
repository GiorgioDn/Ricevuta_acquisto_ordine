#crea una classe utente con attributi nome, cognome, età e email

class Utente:
    def __init__(self, nome: str, cognome: str, eta: int, email: str, recapito: str, salvadanaio):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.email = email
        self.recapito = recapito
        self.salvadanaio = salvadanaio
        
    def richiesta_acquisto(self, costo:float):       
        #controlla se l'acquisto può essere effettuato e stampa il risultato
        if self.salvadanaio.spendi(costo):
            return True
        else:
            return False
        
        #return self.salvadanaio.ha_budget(costo) (forse non serve più)
    
#classe salvadanaio con attributo budget e metodo per controllare se il budget è sufficiente per un costo dato
class Salvadanaio:
    def __init__(self, budget: float):
        self.budget = budget
        
    def ha_budget(self, costo):
        #controlla se il costo è coperto dal budget disponibile
        return self.budget >= costo
    
    def spendi(self, costo):
        if self.ha_budget(costo):
            # deduce il costo dal budget per simulare una spesa
            self.budget -= costo
            return True
        return False