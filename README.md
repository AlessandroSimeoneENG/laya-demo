# laya-demo

Guida rapida e set di prompt preconfigurati per installare e testare in locale il decision engine **[laya](https://github.com/NandhaKishorM/laya)** (modello multilingue) sui nostri casi d'uso.

Tutto viene eseguito **100% in locale** sulla tua macchina: nessun dato viene inviato a servizi esterni.

---

## Prerequisiti

* **Python 3.10** o superiore
* Circa **2 GB di RAM** liberi (l'encoder multilingue gira rapidamente anche solo su CPU, senza bisogno di GPU dedicata)
* Connessione internet **solo al primo avvio** per scaricare automaticamente i pesi di `convaiinnovations/laya-multilingual` da Hugging Face

---

## Installazione e avvio rapido

1. **Clona questa repository e entra nella cartella:**
   ```bash
   git clone https://github.com/AlessandroSimeoneENG/laya-demo.git
   cd laya-demo
   ```

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
   *(Nota: la prima esecuzione richiederà qualche secondo per scaricare i pesi del modello; le esecuzioni successive saranno immediate).*

---

## Come leggere l'output

Per ogni scenario di test, lo script stampa l'esito delle tre tipologie di decisione supportate da `laya`, affiancate dall'indice di **confidenza** del modello:

* **`[CHOICE]`**: restituisce l'etichetta scelta tra le opzioni disponibili.
* **`[SCORE]`**: restituisce un punteggio numerico continuo lungo la scala ordinale definita nei criteri.
* **`[NOUL]`**: restituisce un esito binario (`SÌ` / `NO`) insieme alla probabilità stimata (da `0.00` a `1.00`).

---

## Struttura della repository

* `README.md` — Questa guida.
* `requirements.txt` — Dipendenze Python necessarie (`laya>=0.5.0`).
* `prompts.json` — Contiene le domande/criteri di classificazione (`choice`, `score`, `noul`) e i testi di esempio in italiano su cui testarli.
* `run_test.py` — Script che inizializza `laya.Agent("convaiinnovations/laya-multilingual")`, legge `prompts.json` e stampa a schermo le decisioni e l'azione consigliata.

---

## Come fare nuovi test

Non serve modificare il codice Python per provare nuovi scenari:

1. Apri **`prompts.json`**.
2. Aggiungi un nuovo blocco `{ "state": "...", "questions": { ... } }` alla lista oppure modifica un caso esistente.
3. Rilancia:
   ```bash
   python run_test.py
   ```
