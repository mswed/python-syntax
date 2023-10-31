def print_upper_words(words, must_start_with):
    """
    Takes a list of words and returns them as upper case if they start with a specified letter

    @param words: list(str), list of words to convert
    @param must_start_with:  list(str), list of letters the word must start with
    @return: list(str), list of upper case words
    """

    results = []
    for word in words:
        upper_word = word.upper()

        for char in must_start_with:
            if upper_word.startswith(char.upper()):
                results.append(word.upper())

    print(results)


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=['h', 'y'])
