from flask import Flask

app = Flask(__name__)

@app.route('/')
def notification():
    return "Notification Service"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

