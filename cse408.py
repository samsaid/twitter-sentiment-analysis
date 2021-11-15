import csv

# read text file as string
#with open('positive.csv', newline='') as csvfile:

positive_file = open('positive.csv', 'r')
pos = positive_file.read()
positive_file.close()

negative_file = open('negative.csv', 'r')
neg = negative_file.read()
negative_file.close()

print(neg)
print(pos)

#sentiment lexicon
lexicon = {
    'beautiful': 10,
    'hard': 7}

# clean up string (remove any chars )

# find matches and calculate score



