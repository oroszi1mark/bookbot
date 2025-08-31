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
    