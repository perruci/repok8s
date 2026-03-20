from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Teste Final Image Updater Argo =)"

app.run(host="0.0.0.0", port=5000)