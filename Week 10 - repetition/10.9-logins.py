# Napisz aplikację, która będzie pozwalała założyć w niej konto posiadające login i hasło.
# Dane użytkowników trzymaj w słowniku. Pamiętaj żeby sprawdzić czy użytkownik o danym loginie już nie istnieje.
# Aplikacja też powinna pozwolić zalogować się wykorzystując login i hasło.

from flask import Flask, request, render_template, redirect

app = Flask(__name__)
user_data = {}


@app.route('/', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in user_data.keys():
            return redirect('/login')

        else:
            user_data[username] = password
            return render_template('logins.html', user_data=user_data, username=username)

    else:
        return render_template('logins.html', user_data=user_data)

@app.route('/login', methods=['POST', 'GET'])
def user_login():

    if request.method == 'POST':
        username1 = request.form['username1']
        password1 = request.form['password1']

        if username1 in user_data.keys():
            if user_data[username1] == password1:
                success = True
                return render_template('logins2.html', user_data=user_data, username1=username1, password1=password1,
                                       success=success)

            else:
                return render_template('logins3.html')

    else:
        return render_template('logins2.html')

app.run(debug=True)
