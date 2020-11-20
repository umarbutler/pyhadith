# -*- coding: utf-8 -*-
"""Handles the segmentation of, categorization of, and extraction of narrators from, ahadith."""

from . import helpers

# Import packages necessary for the loading in of spaCy models.
import spacy
import pkg_resources

class Hadith:
	"""Initializes a Hadith object by loading necessary spaCy models and Arabic words list.
	No arguments are required for initialization."""
	def __init__(self):
		# Initialize necessary variables.
		self.isnad = None
		self.matn = None
		self.category = None
		self.tree = None

		# Load in masdar, muqasim, musaid and rawa models.
		self.masdar = spacy.load(pkg_resources.resource_filename('pyhadith','models/masdar'))
		self.muqasim = spacy.load(pkg_resources.resource_filename('pyhadith','models/muqasim'))
		self.musaid = spacy.load(pkg_resources.resource_filename('pyhadith','models/musaid'))
		self.rawa = spacy.load(pkg_resources.resource_filename('pyhadith','models/rawa'))

		# Load in words list.
		self.words = helpers.arabicWords()

	"""Preprocesses a hadith by cleaning it and storing it for use by other functions."""
	def preprocess(self, raw):
		self.raw = raw
		self.clean = helpers.preprocess(self.raw, self.words)

		return True

	def segment(self):
		"""Segments the hadith into a 'matn' and an 'isnad', creating the 'matn' and 'isnad' attributes.
		Preprocess must have been previously called before you can call segment."""
		segmented = helpers.segment(self.clean, self.muqasim, self.musaid, self.rawa)

		self.isnad = segmented[0]
		self.matn = segmented[1]
		return True
	
	def categorize(self):
		"""Categorizes the hadith as either an 'athar' or a 'khabar'.
		The result is saved in the 'category' attribute.
		Preprocess must have been previously called before you can call categorize."""
		self.category = helpers.categorize(self.clean, self.masdar)
		return True

	def treeify(self):
		"""Reconstructs the isnad of the hadith.
		Creates a tree-like data structure stored in the 'tree' attribute.
		Segment and preprocess must have been previously called before you may call treeify."""
		if self.isnad == None:
			return {"error" : "There is no internal 'isnad' attribute to process. Did you forget to call the 'segment' function?"}
		
		self.tree = helpers.treeify(self.isnad, self.words)
		return True