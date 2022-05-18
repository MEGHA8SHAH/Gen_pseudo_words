# Gen_pseudo_words


Generation of pseudo words

This Pseudoword generator is more like a simulator that first generates bi-grams and tri-grams using a dataset of french words, and then applies phonological rules to print 2 lists of pseudowords that abid those rules.

The aim is to create pseudowords using both orthographical and phonological rules. Making this model relevant to both reading tasks testing orthographical and phological understanding. 

Project plan:
1. Import dataset
2. create bi-grams and tri-gram
3. Apply phonological rules
4. Generate pseudowords


This generator is specifically created to generate French pseudowords


How does the generator run?

step 1: Dataset consisting french words is imported.

>> This dataset helps in creating a reference frame work for the bi-grams and tri-gram. 

step 2: Bi-grams and tri-grams and extracted.

step 3: Using the data all bi-grams and tri-grams are created

step 4: Generating a list of pseudowords using created bi-grams and tri-grams

>> It is important to give a structure too the bi-grams and tri-grams. Therefore, CV, VC, CC, VV rules have been imposed in the structure; where "C" denotes consonants, and "V" denotes for Vowels.

step 5: Phonological rules are applied to the pseudowords

>> Phonolex package was used to apply a structure rule to the generated pseudowords. The package allowed to form multiple phonological rules given the syntax of the program and those rules were finally applied to final list of pseudowords to filter the list. 

step 6: All pseudowords are printed


Phonological rules used by the project are :

>> [+fricitives +stops] -> [-voicing]

>> [+vowel] -> [+voicing]

Two phonological rules have been used to filter the psuedowords. The first rule makes every fricitives stops voiceless. The second rule voices every vowel.

special packages  to be downloaded:
use `pip install phonolex` in terminal



