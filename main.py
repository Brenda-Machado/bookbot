"""

Lessons from boot.dev
How to build yout first bookbot

main.py

"""

from stats import word_count, simbols_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    content = get_book_text("books/frankenstein.txt")
    
    # print(content)

    num_words = word_count(content)

    print(f"Found {num_words} total words")

    sim_count = simbols_count(content)

    print(sim_count)

main()