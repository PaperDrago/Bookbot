def main():
    book_path = "books/frankenstein.txt"
    text = bookText(book_path)
    word_count = get_num_words(text)
    character_count = count_characters(text)
    list_dict = convert_dict_to_list(character_count)
    #print(f"There are this many character in the text: {character_count}\n")
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for dictionary in list_dict:
        print(f"The '{dictionary['char']}' character was found {dictionary['num']} times")


def convert_dict_to_list(dictionary):
    list_dicts = []
    for dict in dictionary:
        temp = {}
        temp["char"] = dict
        temp["num"] = dictionary[dict]
        list_dicts.append(temp)
    list_dicts.sort(reverse=True, key=sort_on)
    return list_dicts

def sort_on(dict):
    return dict["num"]


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