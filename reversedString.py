word = input ("Write a word ")
word2 = word[::-1]

if word2 == word:
    print ("Your word is a palindrome")
else:
    print ("Your word isn't a palindrome")