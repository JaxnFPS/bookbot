from stats import count_words
from stats import count_letters
from stats import sort_dict
import sys
def main(): 
    if(len(sys.argv)>1):
        book_text= get_book_text(sys.argv[1])
        word_count = count_words(book_text)
        dictionary = count_letters(book_text)
        sorted_list = sort_dict(dictionary)
        print(f"Found {word_count} total words")
        for entry in sorted_list:
            print(f"{entry['letter']}: {entry['count']}")
    else: 
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)


    


def get_book_text(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()
    


main()