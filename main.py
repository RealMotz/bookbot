from typing import Dict


def main():
    path_to_book = "books/frankenstein.txt"
    read_book(path_to_book)

def read_book(path_to_book):
    with open(path_to_book) as f:
        book = f.read()
        total_words = len(book.split())
        letters = count_letters(book)
        report(path_to_book, total_words, letters)

def count_letters(text) -> Dict[str, int]:
    letters = {}
    for character in text.lower().replace(" ", ""):
        if not letters.get(character):
            letters[character] = 1
            continue
        letters[character]+= 1
    return letters

def report(book_name: str, total_words: int, letter_count: Dict[str, int]) -> None:
    print(f"--- Begin report of ${book_name} ---")
    print(f"{total_words} words found in the document\n")
    char_list = list(letter_count.items())

    fn = lambda d : d[1]
    char_list.sort(reverse=True, key=fn) 
    for item in char_list:
        if not item[0].isalpha():
            continue
        print(f"The '{item[0]}' was found {item[1]} times")
    print("--- End report ---")

main()
