def letter_difference(word1, word2):
    if len(word1) > len(word2):
        while len(word1) != len(word2):
            word2 += "_"
    elif len(word1) < len(word2):
        while len(word1) != len(word2):
            word1 += "_"
    final_difference = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            final_difference += 1
    return final_difference

input_number = int(input())
sentence = input()
persian_letters = [' ', 'آ', 'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']
for letter in sentence:
    if letter not in persian_letters:
        sentence = sentence.replace(letter, '')
target_word = input()

words = sentence.split()

'''for word in words:
    letter_difference(target_word, word)'''

result_words = [word for word in words if letter_difference(target_word, word) <= input_number]

for result_word in result_words:
    print(result_word)