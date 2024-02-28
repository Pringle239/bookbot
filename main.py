#determine file to be read
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    number_of_letters = count_letters(text)
    sorted_listed = Convert_Dict(number_of_letters) 
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    for item in sorted_listed:
        print(f"The {item['char']} character was found {item['num']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    letters = {}
    for text in book_text:
        lowered = text.lower()
        if lowered.isalpha() == True:
            if lowered in letters:
                letters[lowered] += 1
            else:
                letters[lowered] = 1
        else:
            continue
    return letters

def Convert_Dict(Dict):
    sorted_list = []
    for character in Dict:
        sorted_list.append({"char": character, "num": Dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


    
def sort_on(dict):
    return dict["num"]




main()