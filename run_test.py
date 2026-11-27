import json
import laya

# Carica prompt e casi di test dal file JSON
with open("prompts.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Caricamento modello multilingue (al primo avvio scarica i pesi)...")
agent = laya.Agent("convaiinnovations/laya-multilingual")

for i, text in enumerate(data["test_cases"], 1):
    print(f"\n--- Caso {i} ---")
    print(f"Input: {text}")
    
    out = agent.predict(text, data["questions"])
    
    for q_name, ans in out["answers"].items():
        # Estrae la risposta principale in base al tipo (choice, score o noul)
        valore = ans.get("choice") or ans.get("score") or f"{ans.get('noul'):.2f}"
        route = ans.get("route", "n/a")
        print(f"  • {q_name}: {valore}  [azione consigliata: {route}]")
