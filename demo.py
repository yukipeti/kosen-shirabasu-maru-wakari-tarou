
import requests
import json

def main():
    while True:
        #プロンプトの入力
        prompt :str = input("質問を入力してください ( q で終了): ")
        if prompt.lower() == 'q':
            break

        url = 'http://127.0.0.1:8000/ask_syllabus'
        data = {
            "prompt": prompt
        }

        # ここでAPIを呼び出す,データはjson形式ではないとエラーが起きる
        res = requests.post(url, json.dumps(data))
        
        print(res.json().get("answer"))

if __name__ == '__main__':
    main()
