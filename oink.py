def is_vowel(letter):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        if letter == vowel:
            return True
    return False

source = "source"

translation  = source.split(' ')

for word in translation:
    if is_vowel(word[0]):
        word = word + "way"
        print(word)
    else:
        word = word[1:len(word)] + word[0] + "ay"
        print(word)
