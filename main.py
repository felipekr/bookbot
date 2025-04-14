from stats import get_num_words
import sys


args = sys.argv
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

else:
    try:
        get_num_words(sys.argv[1])
    except:
        print("Problem trying to open book! Please, check the path a try again.")


