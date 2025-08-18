from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/guia')
def guia():
    return render_template('guia.html')

app.run(debug=True)

