# GestioneMagazzino
#### Progetto di Ingegneria del Software, corso di laurea in Ingegneria Informatica e dell'Automazione.

Se hai voglia di guardare il codice sul tuo computer e non più su github o se hai addirittura voglia di metterci una mano, ecco quello che devi fare:
1. PREREQUISITO --> Avere Python3.11 installato
2. Aprire un terminale
2. Creare una cartella ed entrarci dentro con il terminale
3. fare "git clone https://github.com/lorenzocalifano/GestioneMagazzino.git"
4. poi "cd GestioneMagazzino"
5. ed infine "git init"

Adesso sei ready per scrivere del codice...\
Per salvare il codice che hai scritto (i cambiamenti che hai apportato):
1. git add .
2. git commit -m "Ragione dei cambiamenti"
3. git push

per modificare la UI scrivere "designer" nel teminale, modificare, e rigenerare il file .py associato così.\
pyuic5 app/ui/main_window.ui -o app/ui/main_window.py

Consiglio di fare questi 3 passaggi ogni volta che modificate qualcosa, così in caso di errore è più semplice tornare ai "backup" precedenti.\
Prima di scrivere qualsiasi cosa consiglio un bel "git pull" che vi prende la versione piu aggiornata dei file su github.

## AVVIO
1. git pull obbligatorio
2. pip install -r requirements.txt 
3. python -m app.main (./.venv/bin/python -m app.main)