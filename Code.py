# Uploading the selected data
import pandas
lexique = pandas.read_csv('lexique383.tsv.gz', sep='\t')
words= list(lexique.ortho)
print(words)

# 