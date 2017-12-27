
@app.route("")
def hello (liczba1, liczba2):
    return str(int(liczba1 + liczba2))

app.run(debug=True)