import os
import csv
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from groq_client import analyze_transcript

app = FastAPI(title="Mini Tech Challenge - Call Analyzer")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, transcript: str = Form(...)):
    # Analyze using groq (or fallback)
    summary, sentiment = analyze_transcript(transcript)

    # Save to CSV
    csv_path = "call_analysis.csv"
    file_exists = os.path.exists(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Transcript", "Summary", "Sentiment"])
        writer.writerow([transcript, summary, sentiment])

    return templates.TemplateResponse("result.html", {
        "request": request,
        "transcript": transcript,
        "summary": summary,
        "sentiment": sentiment,
        "csv_path": csv_path
    })

@app.get("/download_csv")
def download_csv():
    csv_path = "call_analysis.csv"
    if os.path.exists(csv_path):
        return FileResponse(csv_path, media_type='text/csv', filename='call_analysis.csv')
    return {"error": "CSV not found. Run an analysis first."}

# @app.get("/download_code_zip")
# def download_code_zip():
#     zip_path = "mini_tech_challenge.zip"
#     if os.path.exists(zip_path):
#         return FileResponse(zip_path, media_type='application/zip', filename='mini_tech_challenge.zip')
#     return {"error": "ZIP not found."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
