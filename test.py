# -*- coding: utf-8 -*-
# Import the pyHadith package.
import pyhadith
# Set the hadith to be processed.
text = u'حَدَّثَنَا مُحَمَّدُ بْنُ بَشَّارٍ، حَدَّثَنَا أَبُو أَحْمَدَ، حَدَّثَنَا سُفْيَانُ، عَنْ يَزِيدَ أَبِي خَالِدٍ الدَّالاَنِيِّ، عَنْ رَجُلٍ، عَنْ جَابِرِ بْنِ عَبْدِ اللَّهِ، قَالَ صَنَعَ أَبُو الْهَيْثَمِ بْنُ التَّيْهَانِ لِلنَّبِيِّ صلى الله عليه وسلم طَعَامًا فَدَعَا النَّبِيَّ صلى الله عليه وسلم وَأَصْحَابَهُ فَلَمَّا فَرَغُوا قَالَ ‏"‏ أَثِيبُوا أَخَاكُمْ ‏"‏ ‏.‏ قَالُوا يَا رَسُولَ اللَّهِ وَمَا إِثَابَتُهُ قَالَ ‏"‏ إِنَّ الرَّجُلَ إِذَا دُخِلَ بَيْتُهُ فَأُكِلَ طَعَامُهُ وَشُرِبَ شَرَابُهُ فَدَعَوْا لَهُ فَذَلِكَ إِثَابَتُهُ ‏"‏ ‏.‏'
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
	"matn" : x.matn,
	"isnad" : x.isnad
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