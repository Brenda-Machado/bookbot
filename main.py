"""

Lessons from boot.dev
How to build yout first bookbot

main.py

"""
import sys
from stats import word_count, simbols_count, sorted_list_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():

    print("============ BOOKBOT ============")

    filepath = sys.argv

    if len(filepath) == 2:
        
        content = get_book_text(filepath[1])

        print(f"Analyzing book found at {filepath[1]}")

        print("----------- Word Count ----------")

        num_words = word_count(content)

        print(f"Found {num_words} total words")

        sim_count = simbols_count(content)

        print("--------- Character Count -------")

        report = sorted_list_dict(sim_count)

        for item in report:
            if item['name'].isalpha():

                print(f"{item['name']}: {item['num']}")
    
    else:

        print("Usage: python3 main.py <path_to_book>")

        sys.exit(1)

main()