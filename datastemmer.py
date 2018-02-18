#This program takes in the data file generated from the stopping program and does the stemming.
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import string

input_file = open("stoppeddata.txt","r")
output_file = open("stemmeddata.txt","w")

testinput_file = open("stoppedtestdata.txt","r")
testoutput_file = open("stemmedtestdata.txt","w")

stemmer = SnowballStemmer("english", ignore_stopwords=True)


for line in input_file :
	line_words = word_tokenize(line)

	stemmed_words = list()
	for x in line_words: 		 
		stemmed_words.append(stemmer.stem(x))
		
#print(filtered_words)
#print()

	stemmed_string = (' '.join(stemmed_words))
	output_file.write(stemmed_string)
	output_file.write("\n")

#Repeat the stemming procedure for test data file.
for line in testinput_file :
	line_words = word_tokenize(line)

	stemmed_words = list()
	for x in line_words: 		 
		stemmed_words.append(stemmer.stem(x))

	stemmed_string = (' '.join(stemmed_words))
	testoutput_file.write(stemmed_string)
	testoutput_file.write("\n")