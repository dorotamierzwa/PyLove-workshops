from flask import Flask, request, jsonify

app = Flask(__name__)

osoby = []


@app.route('/users/add', methods=['POST'])
def add_user():
    osoby.append(request.get_json())
    return 'Zapisano osobe'


@app.route('/users/stats', methods=['GET'])
def stats():
    stats = {
        'ilosc_osob': 0,
        'plec': {
            'k': 0,
            'm': 0
        }
    }
    wiek_suma = 0
    imiona = {}
    imie = osoby[0]['imie']

    for osoba in osoby:
        stats['ilosc_osob'] += 1
        stats['plec'][osoba['plec']] += 1
        wiek_suma += osoba['wiek']
        imiona[osoba['imie']] = imiona.get(osoba['imie'], 0)
        if imiona[osoba['imie']] >= max(imiona.values()):
            imie = osoba['imie']

    stats['sredni_wiek'] = wiek_suma / len(osoby)
    stats['najpopularniejsze_imie'] = imie

    return jsonify(stats)

app.run(debug=True)