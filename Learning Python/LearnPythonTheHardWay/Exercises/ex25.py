#More function practice

def break_words(stuff):
    """"This function will break up words for us."""
    words = stuff.split(' ')
    return words

#Used str.lower so all words would be lowercase before sorting
def sort_words(words):
    """Sorts the words."""
    return sorted(words, key=str.lower)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """"Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

sentence = "This is my test sentence!"

#Function calls
words = break_words(sentence)
print(words)

sorted_words = sort_words(words)
print(sorted_words)

print_first_word(words)
print_last_word(words)

sorted_sentence = sort_sentence(sentence)
print(sorted_sentence)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)