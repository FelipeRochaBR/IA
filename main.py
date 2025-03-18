from flask import Flask 
import backEnd.mainGrid as principal

app = Flask(__name__)

from views import *

#def teste() :
 #  print('',principal.caminho) 

if __name__ == "__main__":
    app.run()
