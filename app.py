from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Teste ambiente de DEV - Image Updater - deploy dev"

app.run(host="0.0.0.0", port=5000)