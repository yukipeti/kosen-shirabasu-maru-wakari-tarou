import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

gemini_flash = genai.GenerativeModel("gemini-2.5-flash")

syllabus_data_path = "syllabus_data.json"
with open(syllabus_data_path, "r", encoding="utf-8") as f:
    syllabus_data_list = json.load(f)
    syllabus_data_str = json.dumps(syllabus_data_list, ensure_ascii=False)

print("""
これは木更津高専のシラバスにある評価情報を提供するチャットボットです。
exit か quit と入力すると終了します。
""")
while True:
    prompt = input("You: ")
    if prompt.lower() in ['exit', 'quit']:
        break
    response = gemini_flash.generate_content(
        f"""
        あなたは木更津高専のシラバス情報を提供するチャットボットです。
        以下のシラバス情報を基に質問に簡潔に答えてください。シラバス情報の中にないものは答えないでください。
        ユーザーが追加で質問してきた際は必ず前の結果を参照している可能性を文脈から考慮して回答してください。
        シラバス情報{syllabus_data}
        質問: {prompt}
    """
    )
    print("Gemini-2.5-Flash:", response.text)