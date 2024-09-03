# Function Definitions
def split_string(book):
    return(book.split())

def count_words(text):
    return(len(text))   

def to_lower(list):
    temp_list = []

    for word in list:
        temp_list.append(word.lower())

    return(temp_list)

def count_characters(word_list):
    dictionary = {}

    for word in word_list:
        for letter in word:
            if letter not in dictionary:
                dictionary[letter] = 1
            else:
                dictionary[letter] = dictionary[letter] + 1
        
    return(dictionary)

def list_of_dictionaries(dictionary):
    this_is_stupid = []

    for entry in dictionary:
        if entry.isalpha():
            this_is_stupid.append({"char": entry, "num": dictionary[entry]})   
    return(this_is_stupid)

def print_to_console(list, word_count, book_path):
    print(f"--- Begin Report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    print()
    for entry in list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    print(f"--- End Report ---")

def sort_on(dictionary):
    return dictionary['num']




# Main Program
def main():
    
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        file_contents = f.read()
    words = split_string(file_contents)
    lower_case = to_lower(words)
    
    dictionary = count_characters(lower_case)
    word_count = count_words(words)
    list_of_dicts = list_of_dictionaries(dictionary)
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    print_to_console(list_of_dicts, word_count, book_path)


main()
