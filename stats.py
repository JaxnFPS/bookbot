#returns the number of times a word appears in a string
def count_words(book_text: str) -> int:
    word_list = book_text.split()
    return len(word_list)


#returns the number of times a letter appears in a string
def count_letters(book_text: str) -> dict:
    letter_count = {}
    for char in book_text:
        lower_char = char.lower()
        if(char.isalpha()):
            if letter_count.__contains__(lower_char):
                letter_count[lower_char]+=1
            else:
                letter_count[lower_char]= 1
    return letter_count


#returns a sorted list
def sort_dict(dict:dict)->list:
    list = []
    for entry in dict:
        key = entry
        value = dict[key]
        list.append({"letter":key,"count":value})
        list.sort(reverse=True,key=sort_on)
    return list
        
#defines the sorting method used
def sort_on(items):
    return items["count"]

    

