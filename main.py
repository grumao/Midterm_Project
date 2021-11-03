
from flask import Flask
app = Flask(__name__) # "__main__"

@app.route('/hello',methods = ['GET'])

def hello_world():

    print("Hello world!")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)