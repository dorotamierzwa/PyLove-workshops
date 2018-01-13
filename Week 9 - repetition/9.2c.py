# Do strony z listą pracowników dodaj formularz, umożliwiający dodanie nowego pracownika. Powinien zawierać osobne pole
# tekstowe dla każdej informacji o pracowniku. Przesłanie formularza powinno spowodować dodanie pracownika i wyświetlenie
# zaktualizowanej listy.


from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Employee:
    def __init__(self, ide, fname, lname, pay, position):
        self.ide = ide
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.position = position


table_emp = [
    Employee(1, 'Barack', 'Obama', 2000, 'President'),
    Employee(2, 'Krzysztof', 'Kuc', 6777, 'CEO'),
    Employee(3, 'Julia', 'Roberts', 15000, 'Actress'),
    Employee(4, 'Johnny', 'Depp', 1309, 'Pirate')
]


@app.route('/people', methods=['GET', 'POST'])
def people_list():
    if request.method == 'POST':
        ide = int(request.form.get('ide'))
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        pay = int(request.form.get('pay'))
        position = request.form.get('position')
        new_emp = Employee(ide, fname, lname, pay, position)

        if new_emp is not None:
            table_emp.append(new_emp)
        return redirect('/people')

    return render_template('9.2a-people.html', table_emp=table_emp)


@app.route('/people/<ide>')
def person_details(ide):
    ide = int(ide)
    for employee in table_emp:
        if employee.ide == ide:
            return render_template('9.2b.html', ide=ide, table_emp=table_emp, employee=employee)


app.run(debug=True)