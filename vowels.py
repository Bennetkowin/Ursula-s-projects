def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return sum(1 for char in string if char in vowels)
#Hii nayo inacount the number of vowels in a given a string
#for each character in a string kama ni vowel it adds one to the total sum