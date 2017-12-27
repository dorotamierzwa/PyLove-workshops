# # Napisz funkcję, która sprawdzi czy podane dane w formie stringa są dopuszczalne i zwróci True lub False.

email = input("Podaj swój email: ")



def email_validate(email):

    char = email.split()
    if '@' in email[1:-4]:
        if '.' in email[email.rfind("@"):len(email)-1]:
            print(True)
    else:
        print(False)

email_validate(email)

zip = input("Podaj kod pocztowy: ")

def validate_zip(zip):

    char = zip.split()
    if len(zip) == 6:
        if zip[2] == "-":
            if "-" not in zip[0:1]:
                if "-" not in zip[3:]:
                    print(True)
    else:
        print(False)

validate_zip(zip)
