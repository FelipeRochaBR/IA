from flask import Flask ,request
from backEnd import mainGrid 
app = Flask(__name__)

from views import *

def test():
    print ('',mainGrid())


if __name__ == "__main__":
    app.run(debug=True,port=7000)

 