import pandas

lexique = pandas.read_csv('Lexique383.tsv.gz', sep='\t')

words = list(lexique.ortho)

print(words)
