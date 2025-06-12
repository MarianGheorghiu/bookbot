def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count_chars = {}
    book = text.lower()
    for char in book:
        if char in count_chars:
            count_chars[char] += 1
        else:
            count_chars[char] = 1
    return count_chars

def sort_on(d):
    return d["num"]

def sorted_chars_dict(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list