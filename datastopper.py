#This piece of code is intended to remove the punctuations and stopwords from both test data and training data files.
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

input_file = open("traingsetdata.txt","r")
output_file = open("stoppeddata.txt","w")

testinput_file = open("testsetdata.txt","r")
testoutput_file = open("stoppedtestdata.txt","w")

stop_words = set(stopwords.words("english"))

for line in input_file :
	line_words = word_tokenize(line)
	nopunc_line_words = list() 
	for x in line_words: 
		if x not in string.punctuation: 
			nopunc_line_words.append(x)
		else:
			continue	

	filtered_words = list()
	for x in nopunc_line_words: 
		if x not in stopwords.words('english'): 
			filtered_words.append(x)
		else:
			continue

	stopped_string = (' '.join(filtered_words))
	output_file.write(stopped_string)
	output_file.write("\n")


#Repeat the process for Test data file.
for line in testinput_file :
	line_words = word_tokenize(line)
	nopunc_line_words = list()
	for x in line_words: 
		if x not in string.punctuation: 
			nopunc_line_words.append(x)
		else:
			continue

	filtered_words = list()
	for x in nopunc_line_words: 
		if x not in stopwords.words('english'): 
			filtered_words.append(x)
		else:
			continue

	stopped_string = (' '.join(filtered_words))
	testoutput_file.write(stopped_string)
	testoutput_file.write("\n")
