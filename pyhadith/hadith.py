# -*- coding: utf-8 -*-
"""Handles the deconstruction of ahadith."""

import pyhadith.helpers as helpers
import json

class Hadith:
	"""Deconstructs a given hadith, creating 'raw', 'clean', 'isnad', 'matn' and 'category' attributes.
	Initialization requires the passing of a single argument (an arabic unicode encoded string with diacritics which is the text of a hadith).
	You may optionally pass your own list of arabic words (used to detect whether a token contains the arabic word 'wa'), or else, an internal words list will be used."""
	def __init__(self, raw, words=None):
		self.raw = raw

		# Default to our own interal words list.
		if words == None:
			words = helpers.arabicWords()

		self.clean = helpers.clean(self.raw, words)

		# Use helpers.ahadith to extract narrators from, reconstruct the isand of, and categorize, the hadith.
		hadith = helpers.ahadith(self.clean, words)

		# Set internal attributes.
		self.isnad = hadith['isnad']
		self.matn = hadith['matn']
		self.category = hadith['category']
	