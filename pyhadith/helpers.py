# -*- coding: utf-8 -*-
"""Helps in the pre-processing, analysis, post-processing and standardisation of ahadith."""

from . import connector
from nltk.stem.isri import ISRIStemmer
# Import NTLK word_tokenize. If it fails, download 'punkt' and import again.
try:
	from nltk import word_tokenize
except:
	print("The NLTK 'punkt' tokenizor could not be located. We are going to try downloading the tokenizor.")
	from nltk import download
	download('punkt')
	from nltk import word_tokenize
	print("The NLTK 'punkt' tokenizor was successfully downloaded.")
import csv
import pyarabic.araby as araby

# This function preprocesses a text so that it may be processed later by the statistical models.
def preprocess(text, words):
	"""Returns a string without punctuation, numbers, additional whitespace. Also adds whitespace before the arabic word 'wa' (and)."""
	# A pre-defined list of tokens which must be removed from the text.
	reps = ['.','/','<','>','?','؟','-','[',']','!',':','1','2','3','4','5','6','7','8','9','0','{','}','"',"'",'(',')',',','،','\n','\t']
	for rep in reps:
		text = text.replace(rep, ' ')
	# Get rid of extra white space.
	text = " ".join(text.split())
	tokens = word_tokenize(text)

	cleanedText = []
	# If the arabic word 'wa' is in the token, add extra whitespace.
	for token in tokens:
		if isWa(token, words):
			cleanedText.append(token[0:2])
			if len(token) > 2:
				cleanedText.append(token[2:])
		else:
			cleanedText.append(token)
	# Join cleanedText and replace extra whitespace.
	cleanedText = " ".join((" ".join(cleanedText)).split())
	return cleanedText

def arabicWords():
	"""Returns a list of arabic words stored in language/words.ar."""
	words = []
	# Open the words list.
	with open('language/words.ar', encoding='utf-8-sig') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		csv_reader = list(csv_reader)
	csv_file.close()
	# Flatten csv_reader.
	for item in csv_reader:
		if item != []:
			words.append(item[0])
	return words

# This function checks where a join term is 'وَ' (meaning 'and'.) This uses the same method as Motaz Saad's 'split-waw-arabic' python module.
def isWa(token, words):
	"""Detects whether a given token contains the arabic word 'وَ', returning either True or False.
	This uses the same method as Motaz Saad's 'split-waw-arabic' python module and, therefore, requires an Arabic word list."""
	# Remove extra whitespaces.
	token = " ".join(token.split())
	# Check if the first two characters of the token are 'وَ'.
	if token[:2] == 'وَ':
		# If 'وَ' are the only characters, it is 'وَ'.
		if len(token) == 2:
			return True
		# If 'وَ' is followed by a space, it is 'وَ'.
		if token[2] == ' ':
			return True
		# Check if 'و' is not in the beginning of the stem of the token, if so, it is 'وَ'.
		if ISRIStemmer().stem(token).replace(' ','')[0:1] != 'و':
			return True
		# Check if token w/o 'waw' (tashkeel stripped) is in Arabic words list, if so, it is 'وَ'.
		if araby.strip_tashkeel(token[2:]) in words:
			return True
	# Default to not 'wa'.
	return False

def deconstruct(text):
	"""Deconstructs a hadith into a matn and an isnad, using the 'rawa' model.
	Returns matn and isnad objects."""
	
	doc = connector.process(text, 'rawa')

	isnad = {
			"raw" : text, # Defaults to entire text.
			"start_char" : 0,
			"end_char" : len(text)-1,
			"narrators" : []
		}
	
	matn = {
			"raw" : "",
			"start_char" : None,
			"end_char" : None,
		}
	
	# Set a closed class of stemmed join terms.
	joinTerms = ['حدث','عن','قال','ثنا','خبر','نا','وقل','نبأ','ان','انا', 'قلا','انه','سمع','أخبر','يقل','وقل','غدد','قرء','أصب',
	'قلت','مرو','عنى','بمك','وعن','في','بمك','كوف','ملء','ذكر','من','لفظ','او','وهذا','هذا', 'كلهم','تقل','وكانت','كان']
	# Add entities found by spaCy to isnad['narrators'].
	for ent in doc.ents:
		entText = ent.text
		label_ = ent.label_
		start_char = ent.start_char
		end_char = ent.end_char
		add = True

		# Deal with cases where first word of ent is a join term.
		stemmer = ISRIStemmer()
		words = (" ".join(entText.split())).split(" ")
		firstWord = words[0]
		firstStem = stemmer.stem(araby.strip_tashkeel(firstWord))
		if firstWord in joinTerms:
			# Don't add this ent if its in the join terms AND its only one word.
			if len(words) == 1:
				add = False
			else:
				del words[0]
				entText = " ".join(words)
				start_char = start_char+len(words)
				end_char = end_char+len(end_char)
		# Add to isnad['narrators'] if there is a still name after having removed join terms.
		if add == True:
			isnad['narrators'].append({'text' : entText, 'label_' : label_,'start_char' : start_char, 'end_char' : end_char})
	
	# Split the hadith into a 'isnad' and 'matn' at the last occurrence of narrator's name.
	lastIsnadEnd = isnad['narrators'][len(isnad['narrators'])-1]['end_char']
	if (lastIsnadEnd != len(text)-1):
		isnad['raw'] = text[:lastIsnadEnd]
		isnad['end_char'] = lastIsnadEnd
		matn['raw'] = text[lastIsnadEnd:]
		matn['start_char'] = lastIsnadEnd
		matn['end_char'] = len(text)-1

	return isnad, matn

def categorize(text):
	"""Uses the 'asl' model to categorize a hadith as either an atar or a khabar.
	Returns the label of the category and the score assigned to the categorization by the 'asl' model."""

	doc = connector.process(text, 'asl')

	# Set the category to be athar if the athar score is greater than the khabar score, or else default to khabar.
	if doc.cats['athar'] > doc.cats['khabar']:
		name = 'atar'
		score = doc.cats['athar']
	else:
		name = 'khabar'
		score = doc.cats['khabar']
	
	return {"name" : name, "score" : score}
	
def treeify(isnad, words):
	"""Reconstructs the isnad of a given hadith.
	Returns a tree-like data structure representing narrational relationships of narrators in the isnad."""
	tree = []
	ents = isnad['narrators']
	text = isnad['raw']
	# Create a In-Out list for tokens in the isnad.
	narrators = []
	IOisnad = []
	count = 0
	for ent in ents:
		count = count+1
		entText = ent['text']
		label = ent['label_']
		start_char = ent['start_char']
		end_char = ent['end_char']
		# If ent is out of isnad, break the loop.
		if end_char > isnad['end_char']:
			break
		# If ent isn't the first token, add the text before it.
		if start_char != 0:
			# If ent isn't the first ent, add the text from the prev ent until this ent, else add all the previous text.
			if count != 1:
				prevEnd = narrators[count-2]['end_char']
				# If there's text in-between, add to IOisnad.
				if prevEnd != start_char:
					IOisnad.append({'label' : 'OUT', 'raw' : text[prevEnd:start_char], 'start_char' : prevEnd, 'end_char' : end_char})
			else:
				IOisnad.append({'label' : 'OUT', 'raw' : text[0:start_char], 'start_char' : 0, 'end_char' : start_char})
		# Add ent to narrators list.
		narrators.append({'text' : entText, 'label' : label, 'start_char' : start_char, 'end_char' : end_char})
		IOisnad.append({'label' : 'RAWI', 'raw' : entText, 'start_char' : start_char, 'end_char' : end_char})
	
	# Create a tree-like structure which stores narratorial relationships.
	IOisnad.reverse()
	count = 0
	narratorCount = 0
	for item in IOisnad:
		count = count+1
		# If narrator, deal with parents.
		if item['label'] == 'RAWI':
			narratorCount = narratorCount+1
			# If last narrator, no parents.
			if narratorCount == 1:
				parents = None
			# If prev. item is OUT and is wa, assume parents of previous narrator.
			elif IOisnad[count-2]['label'] == 'OUT' and isWa(" ".join(IOisnad[count-2]['raw'].split()).split(' ')[0], words):
				parents = tree[narratorCount-2]['parents']
			# Else, look for parents.
			else:
				parents = []
				# Set possible parents to be all those items before this one.
				possibleParents = IOisnad[:(count-1)]
				possibleParents.reverse()

				parentsCounter = 0
				possibleCounter = 0
				for possibleParent in possibleParents:
					possibleCounter = possibleCounter+1
					# Add to the parentsCounter if this is a narrator.
					if possibleParent['label'] == 'RAWI':
						parentsCounter = parentsCounter+1
						# Make sure this isn't the last possible parent.
						if possibleCounter != len(possibleParents):
							# If the succeeding item is RAWI, or is not Wa, break.
							succParent = possibleParents[possibleCounter]
							if succParent['label'] == 'RAWI' or isWa(" ".join(succParent['raw'].split()).split(' ')[0], words) == False:
								break
				
				# Assign parents.
				pCount = 0
				for i in range(parentsCounter):
					pCount = pCount+1
					# Append narratorCount-pCount to parents.
					parents.append(narratorCount-pCount)
				
			# Append to narrators
			tree.append(
				{
					"id" : narratorCount,
					"name" : item['raw'],
					'parents' : parents,
					"start_char" : item['start_char'],
					"end_char" : item['end_char']
				}
			)
	return tree