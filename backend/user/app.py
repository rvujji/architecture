rom flask import Flask

app = Flask(__name__)

@app.route('/')
def user():
    return "User Service"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
