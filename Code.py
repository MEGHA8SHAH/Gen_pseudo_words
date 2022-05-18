# importing libraries
import pandas
import random
import string
import re
# Uploading the selected data
lexique = pandas.read_csv('lexique383.tsv.gz', sep='\t')
words= list(lexique.ortho)
print(words)
words2 = [str(w) for w in words]
# Extracting bi-grams and tri-grams
def extract_bigrams(token):
    return [token[i:i+2] for i in range(len(token) - 1)]

def extract_trigrams(token):
    return [token[i:i+3] for i in range(len(token) - 1)]
# Using the data to create bi-grams and tri-grams
all_bi_grams = []
for w in words2:
    all_bi_grams.extend(extract_bigrams(w))
all_tri_grams = []
for w in words2:
    all_tri_grams.extend(extract_trigrams(w))
# Generating pseudowords
pwb6 = ["".join(random.sample(all_bi_grams, 3)) for _ in range(10000)]
pattern_bi = re.compile("^([ptkbdgcqwjfshlxvnmlrz][aeuio]|[aeuio][ptkbdgcqwjfshlxvnmlrz]|[aeuio][aeuio]|[ptkbdgcqwjfshlxvnmlrz][ptkbdgcqwjfshlxvnmlrz])+$")
list_bi =[w for w in pwb6 if pattern_bi.match(w) is not None]
pwt6 = ["".join(random.sample(all_tri_grams, 2)) for _ in range(10000)]
pattern_tri = re.compile("^([ptkbdgcqwjfshlxvnmlrz][aeuio]|[aeuio][ptkbdgcqwjfshlxvnmlrz]|[aeuio][aeuio]|[ptkbdgcqwjfshlxvnmlrz][ptkbdgcqwjfshlxvnmlrz])+$")
list_tri = [w for w in pwt6 if pattern_tri.match(w) is not None]
print(list_tri)
print(list_bi)
# Phonological features and phonological rule
for i in range(len(list_tri)):
    if ["s"] in list_tri:
        ["s"] += ["z"]
print(list_tri)
for i in range(len(list_bi)):
    if ["s"] in list_bi:
        ["s"] += ["z"]
print(list_bi)

# Printing Pseudowords
print(list_tri)
print(list_bi)
