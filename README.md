# Mini Tech Challenge - Call Analyzer

This project implements the requested mini challenge:
- Accept a customer call transcript via a simple web UI (FastAPI).
- Use the Groq API to generate a 2-3 sentence summary and a sentiment (Positive / Neutral / Negative).
- Print and save results into `call_analysis.csv` with columns: Transcript | Summary | Sentiment.

## 📱 Screenshots
<img width="1890" height="885" alt="Screenshot 2025-09-20 145057" src="https://github.com/user-attachments/assets/10b46256-ca75-41a7-9a1f-dd9216551f2a" />
<img width="1905" height="896" alt="Screenshot 2025-09-20 145037" src="https://github.com/user-attachments/assets/3c48575d-11f1-4470-96a9-85df6d62d81d" />

---

**Files included**:
- `app.py` - FastAPI app + simple front-end form.
- `groq_client.py` - wrapper that calls Groq and falls back to a simple rule-based method when Groq is unavailable.
- `templates/` - Jinja2 HTML templates for the UI.
- `requirements.txt` - Python dependencies.
- `sample_transcript.txt` - a short sample transcript you can paste.
- `.env.example` - example showing how to set `GROQ_API_KEY`.
- `call_analysis.csv` - will be created when you run an analysis.

## ⚡ Quick start

1. **Clone / projec**t
```bash
cd mini_tech_challenge

2. **(Optional)** Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   uvicorn app:app --reload
   ```
   Open `http://127.0.0.1:8000` in your browser, paste a transcript, and click **Analyze**.

5. **Where output is saved**
   - After analyzing, results are appended to `call_analysis.csv` in the same folder.
   - The CSV columns are: `Transcript, Summary, Sentiment`.

6. **Notes about Groq usage**
   - This project uses the official Groq Python client and their Chat Completions API to request a JSON response (summary + sentiment). See the Groq Python repo for usage examples and installation instructions. citeturn1view0turn0search4
   - If the Groq call fails (no API key, network error, or model output can't be parsed), the app falls back to a deterministic short-summary + token-based sentiment heuristic so you can still demo the functionality.

7. **Example curl test**
   ```bash
   curl -X POST -F 'transcript=Hi, I was trying to book a slot yesterday but the payment failed and I received no email confirmation.' http://127.0.0.1:8000/analyze
   ```

## References
- Groq Python client & examples. citeturn1view0
- Groq Chat / text API docs. citeturn0search17
