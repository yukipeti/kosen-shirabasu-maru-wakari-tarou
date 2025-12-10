import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


gemini_flash = genai.GenerativeModel("gemini-2.5-flash")

syllabus_data_path = "syllabus_data.json"
with open(syllabus_data_path, "r", encoding="utf-8") as f:
    syllabus_data_list = json.load(f)
    syllabus_data_str = json.dumps(syllabus_data_list, ensure_ascii=False)

chat = gemini_flash.start_chat(history=[])

class gemini_prompt(BaseModel):
    prompt: str

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    global syllabus_data_list
    try:
        if not os.path.exists(syllabus_data_path):
            raise FileNotFoundError(f"{syllabus_data_path} not found")
        with open(syllabus_data_path, "r", encoding="utf-8") as f:
            syllabus_data_list = json.load(f)
        print("Syllabus data loaded successfully.")
    except Exception as e:
        print(f"Error loading syllabus data: {e}")
    yield


@app.get("/")
def index():
    return {"message": "高専シラバス丸わかり太郎 API is running"}

@app.post("/ask_syllabus")
def response(data: gemini_prompt):
    prompt = data.prompt
    answer: str = chat.send_message(
        f"""
        あなたは木更津高専のシラバス情報を提供するチャットボットです。
        以下のシラバス情報を基に質問に簡潔に答えてください。シラバス情報の中にないものは答えないでください。
        シラバス情報{syllabus_data_str}
        質問: {prompt}
    """)
    return {"answer": answer.text}