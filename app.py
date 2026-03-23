from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Testando o promote via PR para ambiente de HML"

app.run(host="0.0.0.0", port=5000)