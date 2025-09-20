import os
import json
from groq import Groq

def analyze_transcript(transcript: str):
    transcript = (transcript or "").strip()
    if not transcript:
        return "", "Neutral"

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set. Please set your API key to use the Groq API.")

    client = Groq(api_key=api_key)

    system_prompt = (
        "You are a helpful assistant. Given a customer call transcript, "
        "output only a single valid JSON object with exactly two keys: "
        "'summary' (a concise 2-3 sentence summary) and 'sentiment' "
        "(one of 'Positive', 'Neutral', 'Negative'). Do not output any extra text."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": transcript}
    ]

    try:
        resp = client.chat.completions.create(
            messages=messages,
            model="openai/gpt-oss-20b",  # change if you want a different Groq model
        )
        content = resp.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Groq API call failed: {e}")

    # Expect valid JSON from the model
    try:
        parsed = json.loads(content)
        summary = parsed.get("summary", "").strip()
        sentiment = parsed.get("sentiment", "").strip().capitalize()
        return summary, sentiment or "Neutral"
    except Exception:
        raise RuntimeError(f"Groq API did not return valid JSON: {content}")
