
import requests
import json

def main():
    url = 'http://127.0.0.1:8000/ask_syllabus'
    data = {
        "prompt": "後期の必修科目のうち、中間試験があるものを教えてください"
    }

    # ここでAPIを呼び出す,データはjson形式ではないとエラーが起きる
    res = requests.post(url, json.dumps(data))
    print(res.json().get('answer'))

if __name__ == '__main__':
    main()
