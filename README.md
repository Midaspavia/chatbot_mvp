# 🧠 Interner Firmen-Chatbot (MVP)

Ein einfacher Chatbot, der auf interne PDF, Word und Excel-Dokumente antwortet – mit Quellenverweis.  
Ideal für Deployment auf [Render.com](https://render.com).

## 🚀 Setup lokal

```bash
pip install -r requirements.txt
python ingest.py       # Dokumente einlesen
streamlit run app.py   # Chat starten
```

## 📂 Dokumente

Lege deine Dateien in den `docs/` Ordner. Unterstützt werden:
- PDF (`.pdf`)
- Word (`.docx`)
- Excel (`.xlsx`)

## ☁️ Deployment auf Render

1. Neues GitHub-Repo anlegen & Projekt hochladen
2. Bei Render → „New Web Service“
3. Einstellungen:
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run app.py --server.port=8000`
   - Python environment: `3.10+`
4. Environment Variable:
   - `OPENAI_API_KEY = dein_api_key`

Fertig! ✅

---

© PROGREDA AG – intern & vertraulich
