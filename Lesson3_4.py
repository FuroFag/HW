def single_root_words(root_word, *other_words):
    same_words = []
    root_word_check = root_word.lower()
    for i in other_words:
        other_words_lower = i.lower()
        if root_word in other_words_lower or other_words_lower in root_word_check:
            same_words.append(i)
    return same_words

result1 = single_root_words('self', 'selfharm', 'yourself', 'thySeLf', 'Ampersand')
print (result1)