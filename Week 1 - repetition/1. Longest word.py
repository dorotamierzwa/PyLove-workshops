# Napisz funkcję, która w tekście podanym na wejście znajdzie najdłuższe słowo i je wyprintuje

text = input("Wpisz tekst: ")


def longest_word(text):
    words = text.split(' ')
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))

    longest = max(word_lengths)
    print("Najdłuższe słowo to: ", words[word_lengths.index(longest)], '. Ma:', longest, "liter.")




longest_word(text)
