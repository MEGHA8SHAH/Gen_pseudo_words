# importing libraries
import pandas
import random
import string
import re
from phonolex.phonology import Phonology
# Uploading the selected data
lexique = pandas.read_csv('lexique383.tsv.gz', sep='\t')
wordz= list(lexique.ortho)
print(wordz)
words2 = [str(w) for w in wordz]
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
all_pseudo_words = [list_bi,list_tri]
print(all_pseudo_words)
# Phonological Featurisation and rule
final_pseudowords = []
ph = Phonology()
word_features = [
{'SYLLABLES': [2, 3], 
'CHARACTERS':[6, 9], 
'CONTAINS_DIPTHONGS': 'false'}]
phone_feature = [{'TYPE': 'C', 'FRICATIVE': 1.0, 'STOP': 0,' VOICE': 0},{'TYPE': 'V', 'NASAL': 1.0}]
rule = ph.match(word_features, phone_feature, mode = 'CONTAINS', frequency = 'ALL')
for items in all_pseudo_words:
    if rule in all_pseudo_words:
        final_pseudowords.append
print(final_pseudowords)


