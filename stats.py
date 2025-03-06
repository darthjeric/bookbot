def get_num_words(text):
    words = text.split()
    num_of_words = len(words)
    return num_of_words

def character_counter(text):
    text = text.lower()
    character_dictionary = {}
    for letter in text:
        if letter not in character_dictionary:
            character_dictionary[letter] = 1
        else:
            character_dictionary[letter] += 1
    return character_dictionary

def sort_on(dict):
    return dict["value"]

def list_chars(chars):
    chars_dict = []
    for key in chars.keys():
        #print(f"key is {key}")
        #print(f"value is {chars[key]}")
        if key.isalpha():
            chars_dict.append({"letter": key, "value": chars[key]})
    chars_dict.sort(reverse=True, key=sort_on)
    return chars_dict