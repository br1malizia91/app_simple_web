from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Ciao Bruno! 🎉 Questa è la tua prima API in Flask dentro Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)