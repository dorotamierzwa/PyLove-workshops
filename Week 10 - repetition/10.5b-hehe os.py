# W aplikacji 5a. jeśli użytkownik odpowiednio zmodyfikuje argument "file"
# (zamiast "hehe.txt" poda np. "../../../../hehe.txt" [Linux] lub "..\..\..\..\hehe.txt" [Windows]),
# możliwe jest załadowanie dowolnego pliku (każde ../ lub ..\ powoduje wejście do katalogu/folderu nadrzędnego).
# Napraw aplikację tak, aby pod uwagę brana była tylko nazwa pliku.
# Przydatny moduł: os.path