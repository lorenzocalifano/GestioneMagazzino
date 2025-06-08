#!/bin/bash

echo "🧹 Pulizia vecchio virtual environment (se esiste)..."
rm -rf .venv

echo "🐍 Creazione nuovo virtual environment con python3..."
python3 -m venv .venv || { echo "❌ Errore nella creazione del virtualenv"; exit 1; }

echo "✅ Virtualenv creato. Attivazione..."
source .venv/bin/activate

echo "🔁 Aggiornamento pip..."
pip install --upgrade pip

echo "📦 Installazione pacchetti da requirements.txt (senza pyqt5-tools)..."

# Crea un nuovo requirements filtrato
grep -v "pyqt5-tools" requirements.txt > requirements_no_tools.txt

# Installa i pacchetti
pip install --no-cache-dir -r requirements_no_tools.txt || { echo "❌ Errore nell'installazione dei pacchetti"; exit 1; }

echo "✅ Tutti i pacchetti installati."

echo "📂 Avvio dell'applicazione..."
python -m app.main || { echo "❌ Errore durante l'esecuzione dell'app"; exit 1; }
