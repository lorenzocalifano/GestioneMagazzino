# GestioneMagazzino
#### Progetto di Ingegneria del Software, corso di laurea in Ingegneria Informatica e dell'Automazione.

Se hai voglia di guardare il codice sul tuo computer e non più su github o se hai addirittura voglia di metterci mano, ecco quello che devi fare:
1. Aprire PyCharm e cliccare "Clone Repository"
2. Inserire questo link https://github.com/lorenzocalifano/GestioneMagazzino.git 
3. Trust Project
4. Aprire un terminale da sotto (c'è l'inconcina a sisitra in basso) e scrivere "git init"

Appena ti viene per caso in mente di modificare qualcosa, esita e chiediti "ma ho fatto il pull della versione piu recente"?\
Se non ricordi la risposta tu comunque rifallo:
1. git pull
2. git pull origin main

Adesso sei ready per scrivere del codice...\
Per salvare il codice che hai scritto (i cambiamenti che hai apportato):
1. git add . (il punto è compreso nel comando)
2. git commit -m "Ragione dei cambiamenti"
3. git push
 
Consiglio di fare questi 3 passaggi ogni volta che modificate qualcosa, così in caso di errore è più semplice tornare ai "backup" precedenti.\
Prima di scrivere qualsiasi cosa consiglio un bel "git pull" che vi prende la versione piu aggiornata dei file su github.

La prima volta ti chiederà di fare il login a github, tu fai il login a github.\
Metti il tuo nome utente ma non la password, perchè da un recente aggiornamento per fare queste cose non vuole la password (anche se c'è scritto di mettere la password) ma vuole l'access token.\
L'access token si trova sul sito di github, fai il login > Icona del profilo > impostazioni > giu in basso developer settings > Sotto "Personal Access Token" > Tokens (classic) > Generate new token > Generate new token (classic).\
Dagli un nome e COPIALO SUBITO, quel token sul sito non potrai mai piu vederlo. se lo perdi devi generarne uno nuovo.

per modificare la UI scrivere "designer" nel teminale, modificare, e rigenerare il file .py associato così.\
pyuic5 app/ui/main_window.ui -o app/ui/main_window.py

Consiglio di fare questi 3 passaggi ogni volta che modificate qualcosa, così in caso di errore è più semplice tornare ai "backup" precedenti.\
Prima di scrivere qualsiasi cosa consiglio un bel "git pull" che vi prende la versione piu aggiornata dei file su github.

## AVVIO
1. git pull obbligatorio
2. pip install -r requirements.txt 
3. python -m app.main

### ALTERNATIVA
1. git pull obbligatorio
2. pip install -r requirements.txt 
3. (./.venv/bin/python -m app.main)