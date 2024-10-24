###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Tittle in capital letters: ', movie.upper())

# print title in small letters
print('Tittle in small letters: ', movie.lower())
...

# print how many times the vowel "e" appears in the title
print('Vowel "e" appears',movie.find('e'), 'times')

# print where in the text is the word "Lord"
print('Vowel "e" appears',movie.find('Lord'),)
...

# print where in the text is the word "dragon"
print('Vowel "e" appears',movie.rindex('Lord'),)
...