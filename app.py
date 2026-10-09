from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Docker web app</h1><p>Running inside a container</p>"

@app.route("/health")
def health():
    return {"status":"healthyyy"}

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)