import sys
from stats import word_count, char_count, sort_num, list_of_characters

def check():
    args = sys.argv
    while True:
        try:
            print(args[1])
            break
        except IndexError:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

def main():
    check()
    args = sys.argv
    # cesta pro načtení
    #book_path = "/home/anton/KasintonGit/github/Kasinton/bookbot/books/frankenstein.txt" 
    # načtení do proměnné
    content = get_book_text(args[1])
    # spošítá slova
    the_count = word_count(content)
    # spočítá znaky
    the_char_count = char_count(content)
    
    for_sorting_list = list_of_characters(the_char_count)
    
    for_sorting_list.sort(reverse=True, key=sort_num)  
    print(f"""============ BOOKBOT ============
Analyzing book found at {args[1]}...
----------- Word Count ----------
Found {the_count} total words
--------- Character Count -------""")
    for char_dict in for_sorting_list:
        character = char_dict["character"]
        count = char_dict["count"] 
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")


def get_book_text(filepath):
    # načte z full filename obsah
    with open(filepath) as f:
        return f.read()

main()