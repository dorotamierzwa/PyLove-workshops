from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    imie = request.args.get('imie')
    return render_template('imie.html', query=imie)

app.run(debug=True)