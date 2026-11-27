# laya-demo

Guida rapida e set di prompt preconfigurati per installare e testare in locale il decision model **[laya](https://github.com/NandhaKishorM/laya)** sui nostri casi d'uso.

Tutto viene eseguito **100% in locale** sulla tua macchina: nessun dato viene inviato a servizi esterni.

---

## Prerequisiti

* **Python 3.10** o superiore
* Circa **2–4 GB di RAM** liberi (il modello di default è leggero e gira anche solo su CPU, senza bisogno di GPU dedicata)
* Connessione internet **solo al primo avvio** per scaricare automaticamente i pesi del modello da Hugging Face

---

## Installazione e avvio rapido

1. **Clona questa repository e entra nella cartella:**
   ```bash
   git clone [https://github.com/](https://github.com/)<TUO-UTENTE>/laya-demo.git
   cd laya-demo
   
2. **Crea e attiva un ambiente virtuale Python:**
   * **Linux / macOS / WSL:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   * **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```

3. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Esegui lo script di test con i prompt preconfigurati:**
   ```bash
   python run_test.py
   ```
   *(Nota: la prima esecuzione richiederà qualche decina di secondi per scaricare i pesi del modello; le esecuzioni successive saranno immediate).*
   
