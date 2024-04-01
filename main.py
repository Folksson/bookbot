
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_of_letters(text)
    print(f"{num_words} words found in the document")
    print(num_letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_of_letters(text):
    data = {}
    words = text.split()
    #print(words)

    for word in words:
        lowered_letters = word.lower()
        letters_list = lowered_letters.split()
        letters = str(letters_list)
        #print("Loop 1: " + str(letters))
        
        for letter in letters:
            #print("Letter: " + letter)
            if letter in data:
                data[letter] += 1
            else:
                data[letter] = 1

    return data


main()

