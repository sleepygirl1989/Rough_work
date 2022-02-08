def reverse_word(user_text = input("Please enter a sentence : ")):
    reverse_text = []
    user_text= user_text.split()
    print(user_text)
    for word in user_text:
        reverse_text.insert(0, word)
    return " ".join(reverse_text)




print(reverse_word())
