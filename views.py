from main import app
from flask import render_template

# rotas
@app.route("/")
def Gridpage():
    return render_template("homepage.html")
