from flask import Flask

app = Flask(__name__)

@app.route('/world')
def world():
    return "World"

if __name__ == "__main__":
    app.run(port=5005)