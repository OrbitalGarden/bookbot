def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_character_occurence(text):
    char_lower = text.lower()
    character_occurence = {}
    for char in char_lower:
        if char not in character_occurence:
            character_occurence[char] = 1
        else:
            character_occurence[char] = character_occurence[char] + 1
    return character_occurence


#In order to sort by the value of a dictionnary key, we need it to break down
#into dictionnaries containing a key for the former key, and a key for the former value,
#make a list of these new dictionaries and then sort the list by the value of the former
#value key. Not confusing at all.

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