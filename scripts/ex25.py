def break_words(stuff): #  defining the function break_words and giving the variable stuff as input 
    """ This function will break up words for us .""" # docstring
    words = stuff.split(' ') # this line splits the sentence into individual words 
    return words 

def sort_words(words): # definig the function sort_words and giving the varible words as input
    """Sorts the words.""" # sort
    return sorted(words) 

def print_first_word(words): # defining the function print_first_words and giving the variable words as input
    """Prints the first word after popping it off."""
    word = words.pop(0) # it removes and returns the first word feom the list called words and stores it in the variabe 
    print(word) # displaying message to the user 

def print_last_word(words): # defining the function print_last_words and giving the variable words as input 
    """Prints the last word after pooping it off."""
    word = words.pop(-1) # it removes last element from the list, pop(-1) the negative value do that
    print(word) # dispalys message to the user
def sort_sentence(sentence): # defining the function sort_sentence and giving the variable sentence as input
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) # splits the sentence into words using the break_words()
    return sort_words(words)

def print_first_and_last(sentence): # defining the function print_first_and_last and giving the variable sentence as input
    """Prints the first and last words of the sentence."""
    words = break_words(sentence) # splits the sentence into words using the break_words()
    print_first_word(words) # displaying message to the user
    print_last_word(words) # displaying message to the user

def print_first_and_last_sorted(sentence): # defining the function print_first_and_last_sorted and giving the variable sentence as input
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence) # Calls a function sort_sentence that sorts the word alphabetically
    print_first_word(words) # displaying message to the user
    print_last_word(words) # displaying message to the user 