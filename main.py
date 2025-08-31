from stats import count_words, count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    content  = get_book_text('books/frankenstein.txt')
    print(f"{count_words(content)} words found in the document")
    print(count_chars(content))

main()