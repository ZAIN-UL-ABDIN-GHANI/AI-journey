# ===================== IMPORTS =====================
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from groq import Groq   # 👈 NEW (Groq instead of OpenAI)

# ===================== LOAD ENV =====================

load_dotenv()

# ===================== APP INIT =====================

app = FastAPI()

# ===================== GROQ CLIENT =====================
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ===================== REQUEST MODEL =====================
class Message(BaseModel):
    text: str

# ===================== STATIC + TEMPLATE =====================
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ===================== FRONTEND ROUTE =====================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ===================== CHAT API =====================
@app.post("/chat")
def chat(msg: Message):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": msg.text}
        ]
    )

    return {
        "response": response.choices[0].message.content
    }