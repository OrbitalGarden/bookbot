def number_of_words(text):
    words = text.split()
    return len(words)

def character_occurence(text):
    char_lower = text.lower()
    character_occurence = {}
    for char in char_lower:
        if char not in character_occurence:
            character_occurence[char] = 1
        else:
            character_occurence[char] = character_occurence[char] + 1
    return character_occurence

def make_sorted_list(dict):
    sorted_list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on_num)
    return sorted_list

def sort_on_num(items):   
    return items["num"]