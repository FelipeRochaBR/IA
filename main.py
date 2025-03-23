from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run(debug=True)
