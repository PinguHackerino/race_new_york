from threading import Thread # libreria per i thread
import time # libreria per far aspettare i thread
import random # libreria per generare numeri random
import sys # libreria per far terminare il programma

class Atleta(Thread): # classe atleta che eredita da Thread
    def __init__(self, nome, cognome, eta, peso, tempo_min):
        Thread.__init__(self) # importato il Thread
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.peso = peso
        self.tempo_min = tempo_min
        self.ha_stiramento = False # serve per vedere se ha uno stiramento
        self.ha_contrattura = False # serve per vedere se ha una contrattura
        self.tempo_totale = 0.0 # serve per la classifica finale
        self.report = [] # serve a salvare gli eventi accaduti agli atleti

    def __str__(self): # metodo per la stampa dell'atleta
        return f"{self.nome} {self.cognome}, {self.eta} anni, peso: {self.peso}"
    
    # def get_tempo_tot(self):
    #     return self.tempo_totale

    # def get_report(self):
    #     for i in self.report:
    #         print(i)
    
    def run(self): # metodo dove atleta corre
        for km in range(maratona.lunghezza): # for che fa tutti i km
            evento = random.randint(1, 10) # genera un intero random tra 1 e 10
            if(km % 2 == 0): # se km è pari (0,2,4,6,8,10...), questo perchè gli eventi vanno generati ogni 2 km
                print(f"---------- KM {km} ----------")
                if evento == 1:
                    self.scatto(km) # richiamo funzione scatto
                elif evento == 2:
                    self.contrattura(km) # richiamo funzione contrattura
                    if self.ha_contrattura: # controllo se contrattura si è sciolta o no
                        break # se non si scioglie, atleta finisce la gara
                elif evento >= 3 and evento <= 7: # tra 3 e 7, l'atleta fa la stessa funzione
                    self.andatura_normale(km) # richiamo funzione andatura normale
                elif evento == 8:
                    self.stiramento(km) # richiamo funzione stiramento
                    break # con lo stiramento l'atleta finisce immediatamente la gara
                elif evento == 9:
                    self.ritmo_aumento(km) # richiamo funzione ritmo in aumento
                elif evento == 10:
                    self.stanchezza(km) # richiamo funzione stanchezza
                self.tempo_totale += self.tempo_min 
                time.sleep(2) # ogni 2 secondi genera un evento

        if not self.ha_stiramento and not self.ha_contrattura: # se l'altleta non ha ne contratture ne stiramenti
            print(f"{self.nome} {self.cognome} ha terminato la gara con un tempo totale di {self.tempo_totale} minuti\n") 
        elif self.ha_contrattura: # se l'atleta ha una una contrattura non può finire la gara
            print(f"{self.nome} {self.cognome} ha una contrattura e non può vincere la gara\n")
            # maratona.iscritti.remove(atleta)
        else: # stessa cosa per lo stiramento
            print(f"{self.nome} {self.cognome} ha avuto uno stiramento e non può vincere la gara\n")
            # maratona.iscritti.remove(atleta)

        print(f"{self.nome} {self.cognome} tempo totale: {self.tempo_totale}\n")


    def classifica(self):
        print("Report di gara:")
        for atleta in maratona.iscritti: # scorro atleti
            print(atleta) # stampo atleta
            for evento in atleta.report: # scorro gli eventi salvati dentro report 
                print(evento) # stampo report atleta

        tempi_totali = [atleta.tempo_totale for atleta in maratona.iscritti] # creo una lista di tutti i tempi totali degli atleti
        # print(tempi_totali)
        minimo = min(tempi_totali) # trovo il tempo totale minimo
        for atleta in maratona.iscritti: # scorro atleti
            if (atleta.tempo_totale == minimo): # controllo se hanno il tempo totale minimo
                print(f"L'atleta vincitore è: {atleta.nome} {atleta.cognome}") # stapo il vincitore

        # atleti_ordinati = sorted(maratona.iscritti, key=lambda x: x[1])
        # for i, (atleta.nome, atleta.tempo_totale) in enumerate(atleti_ordinati, start=1):
        #     print(f"{i}. {atleta.nome}: {atleta.tempo_totale} minuti")

    
    def scatto(self, km): # funzione che gestisce scatto
        print(f"Scatto per {self.nome} {self.cognome} al km {km}\n")
        self.tempo_totale -= int(self.tempo_min * 0.3) # viene diminuito il tempo totale poichè l'atleta è scattato
        time.sleep(2)
        self.report.append(f"Scatto al km {km}") # aggiungo l'evento al report

    def contrattura(self, km): # funzione che gestisce contratture
        print(f"Contrattura per {self.nome} {self.cognome} al km {km}\n")
        self.report.append(f"Contrattura al km {km}") # aggiungo l'evento al report
        self.tempo_totale *= 2 # raddoppio il tempo poichè l'atleta ha subito una contrattura
        time.sleep(2)
        scioglimento = random.randint(1, 2) # scelta randomica di un numero tra 1 e 2 per decretare se la contrattura si scioglierà (e quindi l'atlata può continuare la gara) o se essa sarà persistente (atleta non può vincere la gara)
        if scioglimento == 2: # se è 2 la contrattura si scioglierà
            self.report.append(f"Contrattura si è sciolta al km {km}") # aggiungo l'evento al report
            print(f"La contrattura si è sciolta per {self.nome} {self.cognome}\n")
        else:
            self.report.append(f"Contrattura persistente al km {km}") # aggiungo l'evento al report
            print(f"La contrattura persiste per {self.nome} {self.cognome}\n")
            self.ha_contrattura = True # aggiorno il bool di contrattura poichè l'atleta con una contrattura persistente non può vincere la gara

    def andatura_normale(self, km): # funzione che gestisce l'andatura normale
        print(f"Andatura normale per {self.nome} {self.cognome} al km {km}\n")
        time.sleep(2)
        self.tempo_totale += int(self.tempo_min) # mantengo lo stesso tempo
        self.report.append(f"Andatura normale al km {km}") # aggiungo l'evento al report

    def stiramento(self, km):
        print(f"Stiramento per {self.nome} {self.cognome} al km {km}\n")
        self.tempo_totale *= 4 # quadruplico il tempo poichè l'atleta ha subito uno stiramento
        self.report.append(f"Stiramento al km {km}, gara terminata") # aggiungo l'evento al report
        self.ha_stiramento = True # aggiorno il bool di stiramento a true piochè l'atleta non può più vincere la gara

    def ritmo_aumento(self, km): # funzione che gestisce l'aumento di ritmo
        print(f"Ritmo in aumento per {self.nome} {self.cognome} al km {km}\n")
        self.tempo_totale -= int(self.tempo_min * 0.1) # diminuisco il tempo poichè l'atleta ha aumentato il ritmo
        time.sleep(2)
        self.report.append(f"Ritmo in aumento al km {km}") # aggiungo l'evento al report

    def stanchezza(self, km): # funzione che gestisce la stanchezza
        print(f"Stanchezza per {self.nome} {self.cognome} al km {km}\n")
        self.tempo_totale += int(self.tempo_min * 0.1) # incremento il tempo piochè l'atleta è stanco
        time.sleep(2)
        self.report.append(f"Stanchezza al km {km}") # aggiungo l'evento al report
        

class Maratona():
    def __init__(self, lunghezza, tempo_min_richiesto, numero_max_iscritti):
        self.lunghezza = lunghezza
        self.tempo_min_richiesto = tempo_min_richiesto
        self.numero_max_iscritti = numero_max_iscritti
        self.iscritti = [] # lista degli atleti iscritti alla maratona

    def __str__(self): # funzione per la stampa a schermo della maratona
        return f"MARATONA Lunghezza: {self.lunghezza} km, tempo minimo richiesto per la gara : {self.tempo_min_richiesto}"
    
    def iscrivi(self, atleta): # funzione per l'iscrizione di un atleta
        if atleta.tempo_min <= self.tempo_min_richiesto: # controllo che gli atleti abbiano un tempo minimo al km minore rispetto a quello richiesto dalla competizione
            self.iscritti.append(atleta) # se è tutto ok, aggiungo atleta a iscritti
            print(f"Atleta {atleta.nome} {atleta.cognome} iscritto con successo")
        else: # se atleta sfora il tempo minimo richiesto non può partecipare
            print(f"Atleta {atleta.nome} {atleta.cognome} non ha il tempo minimo richiesto, quindi non è stato possible iscriverlo alla maratona")
    
    def elimina(self, nome_elimina, cognome_elimina): # metodo per l'eliminazione di un'atleta
        if(atleta.nome == nome_elimina) and (atleta.cognome == cognome_elimina): # controllo se nome e cognome corrispondono con qualche nome e cognome degli atleti iscritti
            self.iscritti.remove(atleta) # rimuovo l'atleta desiderato
            print("Atleta rimosso con successo")
        else:
            print("Atleta non trovato") # nome e cognome non corrispondono a nessun atleta iscritto
    
    def visualizza(self, atleta): # metodo per la visualizzazione di un atleta
        if atleta in self.iscritti: # controllo se l'atleta che viene passato sia presente tra gli iscritti
            print(f"Nome: {atleta.nome}\nCognome: {atleta.cognome}\nEtà: {atleta.eta}\nPeso: {atleta.peso}\nTempo minimo per km: {atleta.tempo_min}")
        else:
            print(f"Atleta {atleta.nome} {atleta.cognome} non trovato")

    # # def inizia(self): # con questo metodo la gara inizia
    #     threads = []
    #     for atleta in self.iscritti: # scorro tra gli iscritti
    #         thread_atleta = Atleta(atleta.nome, atleta.cognome, atleta.eta, atleta.peso, atleta.tempo_min) # creo thread
    #         thread_atleta.start() # faccio partire il thread
    #         threads.append(thread_atleta) 

    #     for thread_atleta in threads:
    #         thread_atleta.join() # per il fine gara
    
    # def fine(self): # metodo per la stampa della classifica e del report
    #     print("Classifica: \n")
    #     for a in self.iscritti:
    #         #tempo_totale = atleta.get_tempo_tot()
    #         print(f"{a.nome} {a.cognome}: Tempo totale {a.tempo_totale}") ########## non va tempo tot
    #         print("Report di gara:")
    #         for evento in atleta.report: ########## report vuoto
    #            print(evento)

scelta = 0
n_atleti = 0
n = 1

print("BENVENUTI ALLA MARATONA!")
print("Crea le regole della tua maratona!")
lunghezza = int(input("Inserisci la lunghezza della maratona: "))
tempo_min_richiesto = float(input("Inserisci il tempo minimo per poter partecipare alla maratona: (in minuti) "))
numero_max_iscritti = int(input("Inserisci il massimo di atleti che possono partecipare alla gara "))
maratona = Maratona(lunghezza, tempo_min_richiesto, numero_max_iscritti) # creazione della maratona
print(maratona) # stampo la maratona grazie al metodo nella classe Maratona

n_atleti = int(input("Quanti atleti gareggiano? ")) # numero degli altri che vogliono gareggiare
if(n_atleti > maratona.numero_max_iscritti): # controllo il numero inserito dall'utente, se è maggiore stampo un messaggio di errore
    print("Numero massimo sforato")
    n_atleti = n_atleti - maratona.numero_max_iscritti # sottrazione di modo che gli iscritti rispettino il numero max
    print(f"Potrai inserire solo {n_atleti} atleti")
for x in range(n_atleti): # inserisco atleti fino al numero scritto prima
    nome_atleta = input("Inserisci nome dell'atleta: ") # inserimento di tutti i dati dell'atleta
    cognome_atleta = input("Inserisci cognome dell'atleta: ")
    eta_atleta = int(input("Inserisci eta dell'atleta: "))
    peso_atleta = float(input("Inserisci peso dell'atleta: "))
    tempo_atleta = float(input("Inserisci tempo dell'atleta: (in minuti) "))
    atleta = Atleta(nome_atleta, cognome_atleta, eta_atleta, peso_atleta, tempo_atleta) # creazione atleta con gli input datti dall'utente
    print(atleta) # stampo l'atleta grazie al metodo nella classe Maratona
    maratona.iscrivi(atleta) # iscrivo atleta alla maratona grazie al metodo iscrivi() nella classe Maratona

while (scelta < 4): # con un valore >= 4 il programma finisce
    print("Scegli cosa fare dal menu:") # menu delle scelte che l'utente può eseguire 
    print("1--Elimina un atleta")
    print("2--Visualizza atleti")
    print("3--Inizia la maratona")
    print("4--Esci")
    scelta = int(input("Immettere la scelta: "))

    if(scelta == 1):
        nome_elimina = input("Inserire il nome da eliminare: ") # inserisco nomi e cognomi degli atleti da eliminare
        cognome_elimina = input("Inserire il cognome da eliminare: ")
        maratona.elimina(nome_elimina, cognome_elimina) # eliminazione dell'atleta tramite il metodo elimina()

    if(scelta == 2):
        n = 1 # inizializzo l'indice
        for i in maratona.iscritti: # scorro gli iscritti
            print("ATLETA ", n)
            maratona.visualizza(i) # stampo tutti gli atleti iscritti alla maratona
            n += 1 # questo mi serve come indice degli atleti, così posso numerare gli atleti

    if(scelta == 3):
        # maratona.inizia() # la maratona inizia
        # la maratona inizia
        for atleta in maratona.iscritti: # scorro tutti gli atleti iscritti
            atleta.start() # starto ogni atleta
        # aspetta che tutti i thread abbiano finito la maratona
        for atleta in maratona.iscritti: # scorro tutti gli atleti iscritti
            atleta.join() # aspetto che ogni atleta finisce
        atleta.classifica() # stampa vincitore e report
        sys.exit() # fa finire il programma


