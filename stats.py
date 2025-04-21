def word_count(content):
    words = content.split()
    count = 0
    for word in words:
        count += 1
    return  count

def char_count(content):
    words = content.lower()
    '''cont_low = content.lower()
    words = cont_low.split()
    chars = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }'''
    chars = {}
    for word in words:
        char = list(word)
        for ii in char:
            if ii in chars:
                chars[ii] += 1 
            else:
                chars[ii] = 1 # delete else and uncomented lines before for block, for alphabet only enumeration'
    return chars

def list_of_characters(chars):
    chars_list = []
    for char, count in chars.items():
        char_info = {"character": char,"count": count}
        chars_list.append(char_info)
    return chars_list
    
def sort_num(dictionary):
    return dictionary["count"]
