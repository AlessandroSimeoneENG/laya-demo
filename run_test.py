import json
import laya

with open("prompts.json", "r", encoding="utf-8") as f:
    scenarios = json.load(f)

print("Caricamento modello multilingue (al primo avvio scarica i pesi)...")
agent = laya.Agent("convaiinnovations/laya-multilingual")

for i, item in enumerate(scenarios, 1):
    print(f"\n--- Caso {i} ---")
    print(f"Input: {item['state']}")
    
    out = agent.predict(item["state"], item["questions"])
    
    for q_name, ans in out["answers"].items():
        if ans.get("choice") is not None:
            valore = ans["choice"]
        elif ans.get("score") is not None:
            valore = ans["score"]
        else:
            valore = f"{ans.get('noul'):.2f}"
            
        route = ans.get("route", "n/a")
        print(f"  • {q_name}: {valore}  [azione consigliata: {route}]")
