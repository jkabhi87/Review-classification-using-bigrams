#This code creates a sentiment table with corresponding line numbers. Then the program would create a table of bigrams and associate
# the bigrams with the list of all the line numbers where the bigrams appear. Then bigrams are generated for the test data file
# and the line number set of all the bigrams in every review line of the test data are appended to form the feature vector.
# Finally the vector is used to determine the 5 most repeated line numbers to find the 5 nearest reviews in the training set.
# Finally, every review is assigned a postive or negative sentiment based on the plus or minus score.
import nltk
import collections
from nltk.tokenize import word_tokenize
from collections import defaultdict

def find_bigrams(input_list):
	bigram_list = []
	for i in range(len(input_list)-1):
		bigram_list.append((input_list[i]+ " " + input_list[i+1]))
	return bigram_list

input_file = open("stemmeddata.txt","r")
testinput_file = open("stemmedtestdata.txt","r")

#review_file = open("inputtest.txt","r")
output_file = open("prediction.txt","w")
bigram_table = defaultdict(set)
linenum_sentiment = dict()
testline_bigrams = list()
linenum = 1
#list_of_linenums = []

for line in input_file :
	linenum_sentiment[linenum] = line[0:2]
	line_bigrams = []
	line_words = word_tokenize(line)
	line_bigrams = find_bigrams(line_words)
	#print(line_bigrams)
	
	for bigram in line_bigrams :
		if bigram not in bigram_table.keys() :
			bigram_table[bigram].add(linenum)
		else:
			bigram_table[bigram].add(linenum)
	
	linenum = linenum + 1

#print(bigram_table)
#print(linenum_sentiment)

for testline in testinput_file :
	#for line in review_file:
	testline_bigrams = []
	testline_words = word_tokenize(testline)
	testline_bigrams = find_bigrams(testline_words)
	#print(testline_bigrams)
	list_of_linenums = list()
	#list_of_linenums.clear()
	
	for testbigram in testline_bigrams :
		if testbigram in bigram_table.keys():
			list_of_linenums = list_of_linenums + list(bigram_table.get(testbigram))			
		else:
			continue
	
	#this section generates the 5 nearest neighbors based on their similarity to the current review.
	maxlinelist = collections.Counter(list_of_linenums).most_common(5) 
	maxlinedict = dict(maxlinelist) #maxlinedict has the 5 line numbers that are the most similar ones in the training set.
	pluscount = 0
	minuscount = 0
	for maxline in maxlinedict.keys() :
		if linenum_sentiment[maxline] == '+1' :
			pluscount = pluscount + 1.0
		elif linenum_sentiment[maxline] == '-1' :
			minuscount = minuscount + 1.15
	
	if pluscount < minuscount :
		output_file.write("-1")
		output_file.write("\n")
	else :
		output_file.write("+1")
		output_file.write("\n")
		
