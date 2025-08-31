def count_words(text: str):
    return len(text.split())

def count_chars(text: str):
    count = dict()
    for c in text:
        lc = c.lower()
        if lc not in count:
            count[lc] = 0
        count[lc] += 1
    return count

def sort_by_count(entry: dict):
    return entry["num"]
    
def sort_char_count(dict: dict):
    counts_list = list()
    for c in dict:
        counts_list.append({ "char": c, "num": dict[c]})
    counts_list.sort(key=sort_by_count, reverse=True)
    return counts_list