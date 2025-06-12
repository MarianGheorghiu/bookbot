import sys

from stats import get_num_words, count_characters, sorted_chars_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
book_path = sys.argv[1]

def main():
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    num_chars = count_characters(text)
    print(num_chars)
    
    chars_sorted_list = sorted_chars_dict(num_chars)
    print_report(book_path, num_words, chars_sorted_list)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()