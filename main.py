import sys
if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():

    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count
from stats import character_count 
from stats import sort_report


file_contents = main()
word_count(file_contents)
character_count(file_contents)
sort_report(file_contents)