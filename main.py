from flask import Flask ,request

app = Flask(__name__)

from rotas import *



if __name__ == "__main__":
    app.run(debug=True,port=7000)

 