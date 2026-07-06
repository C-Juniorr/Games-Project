from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ultimate")
def ultimate():
    return render_template("tictactoe.html")

@app.route("/reinos")
def quiz():
    return render_template("reino_mobile.html")

@app.route("/football")
def memory():
    return render_template("football-master.html")

@app.route("/reigns-H.O.T.D")
def reignshotd():
    return render_template("trono_de_fogo.html")
    
@app.route("/Gkamasutra")
def gkamasutra():
    return render_template("roleta-kamasutra (1).html")
app = app
"""if __name__ == "__main__":
    app.run(debug=True)"""
