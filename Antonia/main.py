from ricevuta import GestoreRicevuta
from utente import Utente

def main():
    gestore = GestoreRicevuta()
    utente = None  # non c'è ancora un utente

    while True:
        print("\n------ MENU ------")
        print("1 - Inserisci/Modifica email utente")
        print("2 - Verifica o aggiorna email nel file")
        print("3 - Visualizza email salvata nel file")
        print("0 - Esci")
        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                email = input("Inserisci la tua email: ")
                utente = Utente(email)
                print("Utente aggiornato.")

            case "2":
                if utente is None:
                    print("❗ Devi prima inserire un utente (opzione 1).")
                else:
                    gestore.verifica_o_aggiorna(utente)
                    print("Email verificata/aggiornata nel file.")

            case "3":
                email_salvata = gestore.leggi_email()
                print(f"Email salvata nel file: {email_salvata}")

            case "0":
                print("Uscita dal programma...")
                break

            case _:
                print("Scelta non valida. Riprova.")


if __name__ == "__main__":
    main()