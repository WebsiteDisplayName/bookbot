from collections import defaultdict

def generate_char_count_report(word_count: int, char_dict: defaultdict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for k, v in char_dict.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def character_count(input_string):
    char_dict = defaultdict(int)
    for char in input_string.lower():
        if char.isalpha():
            char_dict[char] += 1
    sorted_dict = dict(sorted(char_dict.items(), key=lambda pair: pair[1], reverse=True))
    print(sorted_dict)
    return sorted_dict

def get_words(input_string: str) -> int:
    word_count = len(input_string.split())
    print(word_count)
    return word_count

def read_book(path):
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)
    return file_contents

def main():
    path = "./books/frankenstein.txt"
    file_contents = read_book(path)
    word_count = get_words(file_contents)
    char_dict = character_count(file_contents)
    generate_char_count_report(word_count, char_dict)


if __name__ == '__main__':
    main()