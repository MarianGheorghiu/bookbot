def main():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words():
    words = main().split()
    return len(words)
    
def count_characters():
    count_chars = {}
    book = main().lower()
    for char in book:
        if char in count_chars:
            count_chars[char] += 1
        else:
            count_chars[char] = 1
    return count_chars

def sort_on(dict):
    return dict["value"]

def sort_book():
    total_chars = count_characters()
    result = []
    for char in total_chars:
        if char in total_chars and char.isalpha():
            result.append({"name": char, "value": total_chars[char]})
        result.sort(reverse=True, key=sort_on)
    return result

def report():
    print(" --Begin report of books/frankenstein.txt ---")
    print(f"{count_words()} words found in the document")
    print()
    sorted_chars = sort_book()
    for char in sorted_chars:
        print(f"The '{char["name"]}' character was found {char["value"]} times")
    print()
    print("--- End report ---")
    
report()
    
    