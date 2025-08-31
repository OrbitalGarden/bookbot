import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_number_of_words, get_character_occurence, make_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()        
    return book_text

def main():
    book_text = get_book_text(f"{sys.argv[1]}")
    words = get_number_of_words(book_text)
    number_char = get_character_occurence(book_text)
    sorted_list = make_sorted_list(number_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")

main()