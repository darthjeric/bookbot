from stats import get_num_words
from stats import character_counter
from stats import list_chars
import sys



#Convert book text to string
def get_book_text(filepath):
    bookstring = ""
    with open(filepath) as f:
        bookstring = f.read()
    return bookstring

#main program
def main():
    #filepath = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    words = get_num_words(get_book_text(filepath))
    print("=============Bookbot=============")
    print(f"Analyzing book found at {filepath}...")
    print("-----------Word count -----------")
    print(f"Found {words} total words")
    character_count = character_counter(get_book_text(filepath))
    print("---------Character count --------")
    character_list = list_chars(character_count)
    for char_dict in character_list:
        letter = char_dict["letter"]
        value = char_dict["value"]
        print(f"{letter}: {value}")

#entry point
main()