# Gen_pseudo_words


Generation of pseudo words

This Pseudoword generator is more like a simulator that lets you choose rules used to create these pseudowords.

The aim is to create pseudowords using both orthographical and phonological rules. Making this model relevant to both reading tasks as well as auditory tasks. 

The generator is only working with one language - English


How would the generator run?

Step 1: User will have to select the database to use it as a pre-processed word list in the language - default setting - English

Step 2: They, will then have to select the phonological rules they wish to abide - eg: all 3, only 1, or any 2. (The rule should be manually selected by the user)


Phonological rules avaliable :

- "Voiceless stops /p/, /t/, and /k/ are asiprated in word initially and in intially stressed syllables"

- "All vowels and dipthalongs are nasalized before a nasal"

- "All vowels or dipthongs are pronounced lobger when followed by a voiced consonant"

>> This step helps shortlisting a set of words from the database to use it for creating pseudowords.

Step 3: A word list will be created of all the words in the database that follows rule(s) specified. 

Step 4: They then have to choose the generation setting - Tri-grams or Bi-grams (each of the two setting decomposes each word in the word list into 2 different frequencies).

Step 5: Finally, user have to select the number of pseudowords it wants the generator to create.

Step 6: The generator will then create a set of pseudowords in the output screen.



Work plan
- upload the selected database
- add the phonological rules in form of options
- link the rules with the database for shortlisting words
- generate code to create bi-grams or tri-gram of the shotlisted words
- Create a screen to project the generated pseudowords