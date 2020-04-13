# -*- coding: utf-8 -*-
"""Handles the deconstruction of ahadith."""

import pyhadith.helpers as helpers
import json

class Hadith:
	"""Deconstructs and standardizes ahadith.
	Initialization requires the passing of a single argument (an arabic unicode encoded string with diacritics which is the text of a hadith).
	You may optionally pass your own list of arabic words (used to detect whether a token contains the arabic word 'wa'), or else, an internal words list will be used."""
	def __init__(self, raw, words=None):
		self.raw = raw

		# Default to our own internal words list.
		if words == None:
			self.words = helpers.arabicWords()

		# Preproccess the raw text.
		self.clean = helpers.preprocess(self.raw, self.words)
		
		# Init vars.
		self.matn = None
		self.isnad = None
		self.category = None

	def deconstruct(self):
		"""Deconstructs a hadith into a matn and an isnad. Creates 'isnad' and 'matn' attributes."""
		# Use helpers.deconstruct to deconstruct the hadith.
		data = helpers.deconstruct(self.clean, self.words)

		# Set internal attributes.
		self.isnad = data[0]
		self.matn = data[1]
		
		return True

	def categorize(self):
		"""Categorizes a hadith as either an atar or a khabar."""
		# Uses helpers.categorize to categorize the hadith.
		data = helpers.categorize(self.clean)
		self.category = {
			"name" : data[0],
			"score" : data[1]
		}

	def treeify(self):
		"""Reconstructs a hadith's isnad, creating a tree-like data structure stored in the 'tree' attribute."""
		# Uses helpers.treeify to reconstruct the hadith's isnad.
		self.tree = helpers.treeify(self.isnad, self.words)
	
	self.deconstruct()
	self.categorize()
	self.treeify()