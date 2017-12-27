# Wykorzystując dwie nowe wbudowane char() ord() >>> ord("a") 97 >>> chr(98) "b" funkcje zaimplementuj szyfr cezara, który jako drugi parametr będzie brał przesunięcie.
# Przykłady szyfr cezaraz o parametrze 3 podmieni każd literka alfabetu na trzecią z kolei np A na D a Z na C.
# >>> cezar("abc", 2) "cde" >>> cezar("abc", -2) "yza"
# Pamiętaj żeby znaki inne niż litery nie zmieniać. uwzględnij dodatkowo wielkie litery



def Caesar(text, move):
    code = ""

    if move < 26 or move > -26:

        for x in text:

            if x.isalpha() and x.islower():
                if ord('a') <= ord(x) + move <= ord('z'):
                    x1 = ord(x) + move
                    code += str(chr(x1))

                elif ord(x) + move < ord('a'):
                    x1 = ord(x) + move + 26
                    code += str(chr(x1))

                elif ord(x) + move > ord('z'):
                    x1 = ord(x) + move - 26
                    code += str(chr(x1))

            elif x.isalpha() and x.isupper():
                if ord('A') <= ord(x) + move <= ord('Z'):
                    x1 = ord(x) + move
                    code += str(chr(x1))

                elif ord(x) + move < ord('A'):
                    x1 = ord(x) + move + 26
                    code += str(chr(x1))

                elif ord(x) + move > ord('Z'):
                    x1 = ord(x) + move - 26
                    code += str(chr(x1))

            else:
                code += x
        print(code)

    else:
        print("Choose a number between -26 and 26 for the code to work properly.")

Caesar("abc", 2)
Caesar("abc", -2)
Caesar("AA%A", 2)







