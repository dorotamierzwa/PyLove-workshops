from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello!'

@app.route('/witam')
def witam():
    return redirect('/hello')

app.run(debug=True)