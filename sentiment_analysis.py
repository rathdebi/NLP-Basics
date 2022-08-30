import nltk
import csv
import os
import numpy as np

#nltk download
#nltk.download('punkt')

# change path as required (input data)
os.chdir("C:\\Users\\2000080516\\Downloads\\TextExtraction\\input_data")

def create_words():
	positive_words, negative_words = [],[]
	positive_filename = "words_positive.csv"
	negative_filename = "words_negative.csv"
	with open(positive_filename,"rt") as filename: # text mode
		file_reader = csv.reader(filename)
		for row in file_reader:
			positive_words.append(row)
	with open(negative_filename,"rt") as filename: # text mode
		file_reader = csv.reader(filename)
		for row in file_reader:
			negative_words.append(row)
	return positive_words,negative_words


# create positive and negative words
positive_words,negative_words = create_words()

def predict_sentiment(input_text,positive_words,negative_words):
	text_sentence = nltk.sent_tokenize(input_text)
	for sentence in text_sentence:
		positive_count = 0
		negative_count = 0
		words_sentence = nltk.word_tokenize(sentence)
		for word in words_sentence:
			for positive in positive_words:
				if word == positive[0]:
					positive_count+= 1
			for negative in negative_words:
				if word == negative[0]:
					negative_count+= 1
		if positive_count > 0 and negative_count == 0:
			print(f"positive :{sentence}")
		elif negative_count % 2 > 0:
			print(f"negative :{sentence}")
		elif negative_count % 2 == 0 and negative_count > 0:
			print(f"positive :{sentence}")
		else:
			print(f"neutral :{sentence}")

# call function and predict sentiment
predict_sentiment("I am happy that I met you.",positive_words,negative_words)


