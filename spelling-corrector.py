from spell import correction

while True:
    word = input("Please enter a word\n").strip()
    corrected_word = correction(word)
    if(word != corrected_word):
        print("You have a typo")
        print("Corrected word:", corrected_word, "\n")
    else:
        print("No typo\n")
