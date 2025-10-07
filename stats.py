"""

Lessons from boot.dev
How to build yout first bookbot

stats.py

"""

def word_count(book):
    words = 0

    for word in book.split():
        words = words + 1
    
    return words

def simbols_count(book):
    simbols = {}

    for simbol in book.lower():
        if simbol not in simbols:
            simbols[simbol] = 1
        else:
            simbols[simbol] += 1
    
    return simbols

def sort_on(items):
    return items["num"]

def sorted_list_dict(simbols):
    list_simbols = []

    for simbol in simbols:

        list_simbols.append({"name": simbol, "num": simbols[simbol]})

    list_simbols.sort(reverse=True, key=sort_on)

    return list_simbols
