# -*- coding: utf-8 -*-
"""Handles the segmention of ahadith."""

from . import helpers

class Hadith:
	"""Segments a given hadith, creating 'raw', 'clean', 'isnad', 'matn' and 'category' attributes.
	Initialization requires the passing of a single argument (an arabic unicode encoded string with diacritics which is the text of a hadith).
	You may optionally pass your own list of arabic words (used to detect whether a token contains the arabic word 'wa'), or else, an internal words list will be used."""
	def __init__(self, raw, words=None):
		# Set vars
		self.raw = raw
		self.isnad = None
		self.matn = None
		self.category = None
		self.tree = None

		# Default to our own internal words list.
		if words == None:
			self.words = helpers.arabicWords()
		else:
			self.words = words 
		
		self.clean = helpers.preprocess(self.raw, self.words)
		
	def segment(self):
		"""Segments the hadith into a 'matn' and an 'isnad', creating the 'matn' and 'isnad' attributes."""
		segmented = helpers.segment(self.clean)

		self.isnad = segmented[0]
		self.matn = segmented[1]
		return True
	
	def categorize(self):
		"""Categorizes the hadith as either an 'atar' or a 'khabar'.
		The result is saved in the 'category' attribute."""
		self.category = helpers.categorize(self.clean)
		return True

	def treeify(self):
		"""Reconstructs the isnad of the hadith.
		Creates a tree-like data structure stored in the 'tree' attribute.
		Segment must have been previously called before you may call treeify."""
		if self.isnad == None:
			return {"error" : "There is no internal 'isnad' attribute to process. Did you forget to call the 'segment' function?"}
		
		self.tree = helpers.treeify(self.isnad, self.words)
		return True