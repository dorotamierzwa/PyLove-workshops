import requests

add_person = requests.post('http://localhost:5000/users/add',
                           json={'name': 'EEopooo',
                                  'age': 50,
                                  'sex': 'm'
                                  }
                           )

print(add_person.text)