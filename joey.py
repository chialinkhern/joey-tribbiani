import string
from nltk.corpus import wordnet as wn
import random

class Joey:
	
	def __init__(self, fin):
		self.puncPresent = False
		self.fin_list = []

		with open(fin, "r") as f:
			for line in f:
				# self.fin_list = line.split(" ")
				self.fin_list.append(line.split(" "))
				
	def countPunctuations(self, word):
		count = 0
		for char in word:
			if char in string.punctuation:
				count += 1

		return count

	def detectPunctuation(self, word):
		for char in word:
			if char in string.punctuation:
				self.puncPresent = True
				
	def handlePunctuations(self, word):
		numPunctuations = self.countPunctuations(word)
		wordlen = len(word)
		wo = word[:wordlen-numPunctuations]
		pu = word[wordlen-numPunctuations:]

		return wo, pu
		
	def joeyfy(self):
		fout_list = []

		for paragraph in self.fin_list:
			fout_paragraph = []
			for word in paragraph:
				self.detectPunctuation(word)
				if self.puncPresent:
					wo, pu = self.handlePunctuations(word)
					wo = self.pickSynonym(wo)
					word = wo + pu
				else:
					word = self.pickSynonym(word)
				self.puncPresent = False
				fout_paragraph.append(word)
			fout_list.append(fout_paragraph)

		fout = open("Output/output.txt", "w")
		
		for i, paragraph in enumerate(fout_list):
			paragraph_str = " ".join(paragraph)
			fout_list[i] = paragraph_str

		for paragraph in fout_list:
			fout.write(paragraph)

		fout.close()

	def pickSynonym(self, word):
		try:
			synset = wn.synsets(str(word))[0]
			pickedSyn = random.choice(random.choice(synset.hypernyms()[0].hyponyms()).lemma_names())
		except IndexError:
			pickedSyn = word

		
		return pickedSyn


