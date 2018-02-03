# W aplikacji 5a. jeśli użytkownik odpowiednio zmodyfikuje argument "file"
# (zamiast "hehe.txt" poda np. "../../../../hehe.txt" [Linux] lub "..\..\..\..\hehe.txt" [Windows]),
# możliwe jest załadowanie dowolnego pliku (każde ../ lub ..\ powoduje wejście do katalogu/folderu nadrzędnego).
# Napraw aplikację tak, aby pod uwagę brana była tylko nazwa pliku.
# Przydatny moduł: os.path


from flask import Flask, request
import os.path

app = Flask(__name__)

@app.route('/', methods=['GET'])
def loading():
    data = request.args()
    filename = data.get('file')

    content = ''

    try:
        with open(os.path.basename(filename), 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return 'Can\'t load the file :<'

app.run(debug=True)