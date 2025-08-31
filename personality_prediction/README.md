# ATS Analyzer (Demo)

## How to run
1) Install dependencies (Python 3.9+ recommended)
```
pip install -r requirements.txt
```
2) Start the backend API
```
uvicorn backend.main:app --reload
```
3) Open the frontend
- Open `frontend/index.html` in your browser (double-click).
- Pick a PDF/DOC/DOCX file and click **Analyze**.

> If you run a firewall/antivirus, allow local connections on port 8000.
