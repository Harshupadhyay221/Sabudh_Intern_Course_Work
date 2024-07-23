def counts(word):
    vowel_chars = 'aeiouAEIOU'
    num_vowels = 0
    num_consonants = 0
    
    for char in word:
        if char.isalpha():  # Check if the character is a letter
            if char in vowel_chars:
                num_vowels += 1
            else:
                num_consonants += 1
    
    return num_vowels, num_consonants

# Example usage
word = input("Enter a word: ")
vowels, consonants = counts(word)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
