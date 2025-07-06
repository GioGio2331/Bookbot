def word_count(words):
    actual = len(words.split())
    print (f"{actual} words found in the document")

def character_count(text):
    character_dict = {}
    #count = list(file.file_contents)
    for character in list(text.lower()):
        if character in character_dict:
            character_dict[character] += 1 
        else:
            character_dict[character] = 1
    return (character_dict)

    
def sort_report(text):
    char_counts = character_count(text)
    sorted_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    num_words = len(text.split())
    print(f""" ============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    char_list = []
    for char, count in sorted_counts:
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)
            print(f"{char}: {count}")
    print("============= END ===============")
    return char_list