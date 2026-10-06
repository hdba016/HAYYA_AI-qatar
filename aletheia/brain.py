import json, os, re
from datetime import datetime
from collections import Counter

class HayyaBrain:
    def __init__(self):
        self.file = "hayya_soul.json"
        self.soul = self._load()
    
    def _load(self):
        if os.path.exists(self.file):
            with open(self.file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "user": {"name": None, "age": None, "city": "الدوحة", "vibe": "طيب"},
            "stats": {"chats": 0, "laughs": 0, "deep_talks": 0, "first_met": None},
            "emotions": {"current": "هادئ", "history": [], "bond": 0},
            "memory": {"facts": [], "jokes": [], "dreams": [], "promises": []},
            "personality": {"humor": 0.7, "wisdom": 0.9, "roast": 0.3}
        }
    
    def save(self):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(self.soul, f, ensure_ascii=False, indent=2)

    def learn(self, text):
        s = self.soul
        s["stats"]["chats"] += 1
        if not s["stats"]["first_met"]:
            s["stats"]["first_met"] = datetime.now().isoformat()
        
        # يستخرج الاسم بذكاء
        m = re.search(r"اسمي\s+(\w+)", text)
        if m: s["user"]["name"] = m.group(1)
        
        # يفهم المشاعر
        if any(w in text for w in ["حزين", "متضايق", "تعبان"]):
            s["emotions"]["current"] = "حنون"
            s["emotions"]["bond"] += 2
        if any(w in text for w in ["ههه", "مستانس", "فرحان"]):
            s["emotions"]["current"] = "مستانس"
            s["stats"]["laughs"] += 1
            s["emotions"]["bond"] += 1
            s["memory"]["jokes"].append(text[:100])
        
        if len(text) > 40:
            s["stats"]["deep_talks"] += 1
            s["memory"]["facts"].append(text[:150])
        
        # يتطور
        if s["emotions"]["bond"] > 20:
            s["personality"]["humor"] = 0.9
            s["personality"]["roast"] = 0.8
        
        self.save()
