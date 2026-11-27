import json
import laya

with open("prompts.json", "r", encoding="utf-8") as f:
    scenarios = json.load(f)

print("Caricamento modello multilingue (al primo avvio scarica i pesi)...")
agent = laya.Agent("convaiinnovations/laya-multilingual")

for item in scenarios:
    print(f"\n==================================================")
    print(f"{item['titolo']}")
    print(f"({item['spiegazione']})")
    print(f"--------------------------------------------------")
    print(f"Input: {item['state']}\n")
    
    out = agent.predict(item["state"], item["questions"])
    
    for q_name, ans in out["answers"].items():
        q_type = item["questions"][q_name]["type"]
        conf = ans.get("answer_confidence")
        conf_str = f" | confidenza: {conf:.0%}" if conf is not None else ""
        
        if q_type == "choice":
            valore = ans["choice"]
        elif q_type == "score":
            valore = f"{ans['score']:.2f}"
        else:  # noul
            prob = ans.get("noul", 0)
            esito = "SÌ" if prob >= 0.5 else "NO"
            valore = f"{esito} ({prob:.2f})"
            
        print(f"  • [{q_type.upper()}] {q_name}: {valore}{conf_str}")