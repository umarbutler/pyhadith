# -*- coding: utf-8 -*-
# Import the pyHadith package.
import pyhadith
# Set the hadith to be processed.
text = u'حَدَّثَنِي يَحْيَى، عَنْ مَالِكٍ، أَنَّهُ بَلَغَهُ أَنَّ سَعِيدَ بْنَ الْمُسَيَّبِ، وَسُلَيْمَانَ بْنَ يَسَارٍ، كَانَا يَقُولاَنِ عِدَّةُ الأَمَةِ إِذَا هَلَكَ عَنْهَا زَوْجُهَا شَهْرَانِ وَخَمْسُ لَيَالٍ ‏.‏'
# Create a 'Hadith' object using the text of the hadith.
x = pyhadith.Hadith(text)
# Print the resulting attributes.
print({
	"raw" : x.raw,
	"clean" : x.clean
})
# Call the 'deconstruct' function.
x.deconstruct()
# Print the resulting attributes.
print({
	"raw" : x.raw,
	"clean" : x.clean
})
# Call the 'categorize' function.
x.categorize()
# Print the resulting attributes.
print(x.category)
# Call the 'treeify' function.
x.treeify()
# Print the resulting attributes.
print(x.tree)
# Store all of the available attributes.
result = {
	"raw" : x.raw,
	"clean" : x.clean,
	"matn" : x.matn,
	"isnad" : x.isnad,
	"category" : x.category,
	"tree" : x.tree
}
# Print all of the available attributes.
print('All of the available attributes:\n',result)
# Import json.dumps so that all of the available attributes can be printed in JSON format.
import json
# Print all of the available attributes, in JSON format.
print('All of the available attributes (JSON format):\n',json.dumps(result))
