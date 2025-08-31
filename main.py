from stats import count_words, count_chars, sort_char_count
from sys import argv, exit

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    subject = argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {subject}...")
    print("----------- Word Count ----------")
    
    content  = get_book_text(subject)
    word_count = count_words(content)
    char_count = count_chars(content)
    sorted_counts = sort_char_count(char_count)


    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for entry in sorted_counts:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
        
    print("============= END ===============")

main()