# GestioneMagazzino
Progetto di Ingegneria del Software, corso di laurea in Ingegneria Informatica e dell'Automazione.

per avere il codice aggiornato:
git pull --rebase origin main

git clone (direttamente da PyCharm cosi non dovete fa casino con i venv)
pip install -r requirements (ovviamente SOLO SU WINDOWS insllate python se non lo avete gia fatto)
per modificare la UI scrivere "designer" nel teminale, modificare, e rigenerare il file .py associato così
pyuic5 app/ui/main_window.ui -o app/ui/main_window.py
per "pushare" i cambiamenti su github:

git add .
git commit -m "messaggio"
git push

per eseguire il progetto:
python3 app/main.py