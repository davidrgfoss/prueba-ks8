from flask import Flask
import os
app = Flask(__name__)	


@app.route('/',methods=["GET"])
def inicio():
    return "<h1>App de: "+os.environ["NOMBRE"]+"</h1>"

if __name__ == '__main__':
    app.run('0.0.0.0',5001,debug=True)
