# Napisz funkcję, która zamieni wszystkie cyfry na "#" w tekście (stringu) >>> cenzura_cyfr("password12345") "password#####"

def cenzura_cyfr(text):
    for i in text:
        if i in "1234567890":
            text = text.replace(i, "#")
    print(text)

cenzura_cyfr("pasword1234")
cenzura_cyfr("A1a ma k0ta")
