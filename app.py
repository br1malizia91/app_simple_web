from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <h1>Ciao Bruno! 🎉</h1>
    <p>Questa è la tua API con un'immagine.</p>
    <img src="/immagine" width="300">
    """

@app.route("/immagine")
def immagine():
    return send_from_directory("static", "bruno.jpg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
