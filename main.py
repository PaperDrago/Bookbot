def main():
    book_path = "books/frankenstein.txt"
    text = bookText(book_path)
    word_count = get_num_words(text)
    print(f"This is how many words are in the text: {word_count}\n")
    character_count = count_characters(text)
    print(f"There are this many character in the text: {character_count}\n")


def bookText(bookPath):
    with open(bookPath) as file:
        return file.read()
    
def get_num_words(doc):
    split = doc.split()
    i = 0
    for word in split:
        i += 1
    return i

def count_characters(text):
    text_lower = text.lower()
    characters = dict()
    for char in text_lower:
        if(char in characters):
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


if __name__ == "__main__":
    main()