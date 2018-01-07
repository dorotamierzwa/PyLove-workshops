# Napisz aplikację, która wyświetla stronę HTML zawierającą listę zespołów (zdefiniowaną w aplikacji) oraz formularz do
# wyszukiwania z jednym inputem. Przesłanie formularza powinno spowodować wyświetlenie tylko tych zespołów,
# które w nazwie zawierają ciąg znaków podany przez użytkownika.


from flask import Flask, render_template, request

app = Flask(__name__)

bands = ['System of a Down', 'Metallica', 'Rammstein', 'Arctic Monkeys', 'Pall']


@app.route('/', methods=['GET'])
def band_search():
    name = request.args.get('query')
    return render_template('8.7-bands.html', bands=bands, name=name)


app.run(debug=True)
