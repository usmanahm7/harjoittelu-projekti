import json
import os
from flask import Flask, Response, request

app = Flask(__name__)
DICT_FILE = "dictionary.json"

@app.route('/add')
def add_word():
    args = request.args
    en = args.get("en")
    fi = args.get("fi")

    if not en or not fi:
        response = {
            "message": "Missing en or fi parameter",
            "status": 400
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=400, mimetype="application/json")

    if os.path.exists(DICT_FILE):
        with open(DICT_FILE, "r", encoding="utf-8") as f:
            dictionary = json.load(f)
    else:
        dictionary = {}

    dictionary[en.lower()] = fi

    with open(DICT_FILE, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)

    response = {
        "English": en.lower(),
        "Finnish": fi,
        "status": 200
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)