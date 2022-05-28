# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from tabnanny import check


def find_anagram(word, anagram):
    # [assignment] Add your code here
    #check if the length of the word is the same as the length of the anagram
    if len(word) != len(anagram):
        return False
    #create a dictionary to store the letters of the word
    word_dict = {}
    #create a dictionary to store the letters of the anagram
    anagram_dict = {}
    #loop through the word and add the letters to the word_dict
    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1   
    #loop through the anagram and add the letters to the anagram_dict
    for letter in anagram:
        if letter in anagram_dict:
            anagram_dict[letter] += 1
        else:
            anagram_dict[letter] = 1
    #check if the word_dict and the anagram_dict are the same
    if word_dict == anagram_dict:
        print("True", word, "&", anagram, "are anagrams")
        return True
    else:
        print("False:", word, "&", anagram, "are not anagrams")
        return False
word = input("Enter a word: ")
anagram = input("Enter an anagram: ")

find_anagram(word, anagram)
