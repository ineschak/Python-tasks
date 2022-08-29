def remove_letters(letters, word):

    for i in word:
        if i in letters:
            letters.remove(i)
    print (letters)
    

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon")