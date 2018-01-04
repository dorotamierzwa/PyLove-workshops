# Napisz program, który pod adresem /users/add będzie przyjmował zapytania POST z JSON-em o następującej strukturze:
# {"imie": "Grzegorz", "wiek": "26", "plec": "m"}
# W wyniku takiego zapytania dane osoby należy zapisać na serwerze.

# Po wejściu na adres: /users/stats zapytaniem GET program zwróci następującego JSON-a:
# {"ilosc_osob": X, "sredni_wiek": X, "najpopularniejsze_imie": X, "plec": {"k": X, "m": X}}
# (Rzecz jasna w miejscu X-ów powinny pojawić się dane oparte o dotychczas dodanych użytkowników.
# W kluczu ["plec"]["k"] powinna znaleźć się liczba zapisanych kobiet.)

from flask import Flask, request, jsonify

app = Flask(__name__)

people = []


@app.route('/users/add', methods=['POST'])
def add_users():
    people.append(request.get_json())
    return "Person has been saved."


@app.route('/users/stats', methods=['GET'])
def stats():
    stats = {'people_no': 0,
             'sex': {
                 'k': 0,
                 'm': 0
             }
             }

    sum_age = 0
    names = {}
    name = people[0]['name']

    for person in people:
        stats['people_no'] += 1
        stats['sex'][person['sex']] += 1
        sum_age += person['age']
        names[person['name']] = names.get(person['name'], 0)

    stats['avg_age'] = sum_age/len(people)
    stats['popular_name'] = name

    return jsonify(stats)

app.run(debug=True)
