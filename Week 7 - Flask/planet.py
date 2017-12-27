@app.route("/planet-details", methods=['GET'])
def planet_details():
    planet = request.args['planet']
    swapi_resp = requests.get(
        'https://swapi.co/api/planets/?search=' + planet
    )
    planets = swapi_resp.json()['results']
    if not planets:
        return 'Planet {} does not exist'.format(planet)

    planet_data = planets[0]
    response = {'terrain' : planet_data['terrain'],
                'climate' : planet_data['climate']}
    return json.dumps(response)

app.run(debug=True)