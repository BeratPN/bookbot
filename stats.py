def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def sort_words(char_dict):
    result = []
    for ch in char_dict:
        if ch.isalpha(): 
            result.append({"char": ch, "num": char_dict[ch]})
    result.sort(reverse=True, key=sort_on)
    return result