
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_of_letters(text)
    #sorted_report = sort_report(num_letters)

    #sorted = num_letters.sort(reverse=True, key=sort_on)
    print(f"--- Report of book: {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    #print(num_letters)
    print(sorted_report(num_letters))
    print("--- End of report ---")


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
            if letter.isalpha():
                if letter in data:
                    data[letter] += 1
                else:
                    data[letter] = 1

    return data

def sorted_report(dict):
    for i in sorted(dict):
        num = dict[i]
        print(f"Letter: {i} - {num} times")


main()

