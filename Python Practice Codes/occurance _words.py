def occ_word(text):

    words = text.strip().lower().split()

    word_count = {}
    for word in words:
        word = ''.join(char for char in word if char.isalpha())

        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count

text = input("Enter a sentence: ")
print(occ_word(text))