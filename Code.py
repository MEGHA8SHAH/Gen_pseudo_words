# importing libraries
import pandas
import random
import string
from collections import Counter
from random_word import RandomWords

# Uploading the selected data
lexique = pandas.read_csv('lexique383.tsv.gz', sep='\t')
words= list(lexique.ortho)
print(words)

# Generating random-stringe of segments
def random_string(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))
chars = words
size = 3
print(chars)
random_string = (random_string(size, chars))
print(random_string)

# Creating bi-grams and tri-grams
bigrams = Counter(zip(random_string, random_string[1:]))
bi_grams = [print(bigrams)]
trigrams = Counter(zip(random_string, random_string[1:]))
tri_grams = [print(trigrams)]

# Generating Pseudowords

# Phonological rule selection
# Out-put pseudowords