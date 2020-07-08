# -*- coding: utf-8 -*-
"""Handles calls to spaCy models."""

# Import spaCy.
import spacy
import pkg_resources

# This function handles the passing of text to a spaCy model.
def process(text, model):
	"""Returns a proccessed doc from a specified spaCy model in models/."""
	# Load model.
	nlp = spacy.load(pkg_resources.resource_filename('pyhadith','models/'+model))
	# Pass the text to the model. Save output as 'doc.'
	doc = nlp(text)
	# Return the doc.
	return doc
