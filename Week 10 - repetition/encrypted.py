from flask import Flask, render_template, request

app = Flask(__name__)

def cezar_encryption(content, offset):
    encrypted_text = ''
    for character in content:
        if ord(character) >= 97 and ord(character) <= 122:
            encrypted_text += chr(ord(character) + offset % 26)

@app.route('/', methods=['GET', 'POST'])
def cezar_handler():

    encrypted_text = ''

    if request.method == 'POST':
        content = request.form.get('text', '')
        offset = int(request.form.get('offset', '0'))
        encrypted_text = cezar_encryption(content, offset)

    return render_template('cezar.html', encrypted_text=encrypted_text)

app.run(debug=True)