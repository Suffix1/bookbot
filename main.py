def main():
    text = read_book_text('./books/frankenstein.txt')
    counted_words = count_words(text)
    counted_letters = count_letters(text)
    sorted_letters = sorted(counted_letters.items(), key=lambda item: item[1], reverse=True)

    print('\n--- Begin report of books/frankenstein.txt ---\n')
    print(f"{counted_words} words found in the document \n")
    for key, value in sorted_letters:
        print(f"the '{key}' character was found {value} times")
    print('\n--- End report ---')


def count_words(text):
    return len(text.split())

def count_letters(text):
    letters = {}
    for c in text:
        if c.isalpha() == False:
            continue
        lowered = c.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def read_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()

#need to sort the letters by occurance
#need to remove the symbols, can use isalpha() for this
#need to print it prettily

