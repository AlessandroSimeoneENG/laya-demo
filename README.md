# laya-demo

Guida rapida e set di prompt preconfigurati per installare e testare in locale il decision engine **[laya](https://github.com/NandhaKishorM/laya)** sui nostri casi d'uso.

Tutto viene eseguito **100% in locale** sulla tua macchina: nessun dato viene inviato a servizi esterni.

---

## Prerequisiti

* **Python 3.10** o superiore
* Circa **3–4 GB di RAM** liberi (il motore di default usa un reader compatto da `0.8B` che gira anche solo su CPU, senza bisogno di GPU dedicata)
* Connessione internet **solo al primo avvio** per scaricare automaticamente i pesi del modello da Hugging Face (~1.7 GB)

---

## Installazione e avvio rapido

1. **Clona questa repository e entra nella cartella:**
   ```bash
   git clone [https://github.com/](https://github.com/)<TUO-UTENTE>/laya-demo.git
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
   *(Nota: la prima esecuzione richiederà qualche decina di secondi per scaricare i pesi del modello; le esecuzioni successive saranno immediate).*

---

## Come leggere l'output

Per ogni scenario di test, lo script stampa l'esito delle tre tipologie di decisione supportate da `laya`:

* **`[CHOICE]`**: sceglie l'etichetta più adatta tra le opzioni disponibili.
* **`[SCORE]`**: assegna un livello intero lungo la scala ordinale definita nei criteri (da `0` al livello massimo).
* **`[NOUL]`**: restituisce un esito binario (`SÌ` / `NO`) insieme alla probabilità stimata (da `0.00` a `1.00`).

Ogni risposta è accompagnata dall'**azione consigliata** (`auto` o `review`), calcolata dal motore in base al grado di incertezza interna senza dover impostare soglie manuali:

* **`auto` (Gestione automatica):** Il modello è sicuro della risposta; il caso può essere gestito direttamente in autonomia dal sistema.
* **`review` (Revisione manuale):** Il caso è ambiguo o il modello ritiene plausibili più opzioni contemporaneamente; è consigliato l'intervento di un operatore umano (o di un modello più grande).

---

## Struttura della repository

* `README.md` — Questa guida.
* `requirements.txt` — Dipendenze Python necessarie (`laya>=0.5.0`).
* `prompts.json` — Lista di scenari di test in italiano; ogni oggetto contiene il contesto da analizzare (`"state"`) e le relative domande/criteri di valutazione (`"questions"` di tipo `choice`, `score` e `noul`).
* `run_test.py` — Script che inizializza `laya.Agent()`, legge `prompts.json` e stampa a schermo le decisioni e l'azione consigliata.

---

## Come fare nuovi test

Non serve modificare il codice Python per provare nuovi scenari:

1. Apri **`prompts.json`**.
2. Aggiungi un nuovo blocco `{ "titolo": "...", "spiegazione": "...", "state": "...", "questions": { ... } }` alla lista oppure modifica un caso esistente.
3. Rilancia:
   ```bash
   python run_test.py
   ```