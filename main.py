from stats import get_num_words,get_chars_dict,sort_words
import sys

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    #book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_char_list = sort_words(chars_dict)
    print(f"{num_words} words found in the document")
    print(chars_dict)
    
    print_report(book_path,num_words,sorted_char_list)
    

    

def get_book_text(file_path):
    with open(file_path) as f:
         return f.read()
        
  
def print_report(book_path, num_words, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")





main()
