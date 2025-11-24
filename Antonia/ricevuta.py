from module.utente import *
from module.Negozio import *

#creazione della classe ricevuta acquisto
class GestoreRicevuta:
    def __init__(self, percorso_file="ricevuta.txt"):
        # Percorso del file in cui verrà salvata l'email dell'utente
        self.percorso_file = percorso_file

    def leggi_email(self):
        """
        Legge la prima riga del file e la restituisce come stringa.
        Il metodo strip() rimuove eventuali spazi e newline.
        """
        with open(self.percorso_file, "r") as file:
            return file.readline().strip()

    def salva_email(self, email):
        """
        Scrive l'email nel file, sovrascrivendone completamente il contenuto.
        Aggiunge un newline per mantenere il formato ordinato.
        """
        with open(self.percorso_file, "w") as file:
            file.write(f"{email}\n")

    def verifica_o_aggiorna(self, utente):
        """
        Verifica se l'email presente nel file è la stessa dell'utente corrente.
        
        - Se sono uguali → non fa nulla.
        - Se sono diverse → aggiorna il file salvando la nuova email.

        Parametri:
        - utente: oggetto che deve possedere un attributo 'email'
        """
        email_salvata = self.leggi_email()   # Legge l'email attualmente nel file

        # Se l'email non corrisponde a quella dell'utente corrente, la aggiorna
        if email_salvata != utente.email:
            self.salva_email(utente.email)
    