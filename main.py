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


# Main Program
def main():
    
    dictionary = {}
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = split_string(file_contents)
    length = count_words(words)
    lower_case = to_lower(words)

    print (lower_case)

 


main()
