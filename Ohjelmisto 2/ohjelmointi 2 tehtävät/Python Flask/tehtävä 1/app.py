import json
from flask import Flask, Response

app = Flask(__name__)


@app.route('/prime_number/<number>')
def prime_number(number):
    try:
        num = int(number)

        if num < 2:
            is_prime = False
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

        response = {
            "Number": num,
            "isPrime": is_prime
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)