import os
os.environ["HF_HUB_DISABLE_XET"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

import json
import laya

with open("prompts.json", "r", encoding="utf-8") as f:
    scenarios = json.load(f)

print("Caricamento motore laya 0.5 (al primo avvio scarica i pesi del reader 0.8B)...")
agent = laya.Agent()

for item in scenarios:
    print(f"\n==================================================")
    print(f"{item['titolo']}")
    print(f"({item['spiegazione']})")
    print(f"--------------------------------------------------")
    print(f"Input: {item['state']}\n")
    
    out = agent.predict(item["state"], item["questions"])
    
    for q_name, ans in out["answers"].items():
        q_info = item["questions"][q_name]
        q_type = q_info["type"]
        route = ans.get("route", "n/a")
        
        if q_type == "choice":
            valore = ans["choice"]
        elif q_type == "score":
            max_score = len(q_info["criteria"]) - 1
            valore = f"{int(ans['score'])} / {max_score}"
        else:  # noul
            prob = ans.get("noul", 0)
            esito = "SÌ" if prob >= 0.5 else "NO"
            valore = f"{esito} ({prob:.2f})"
            
        print(f"  • [{q_type.upper()}] {q_name}: {valore}  [azione consigliata: {route}]")