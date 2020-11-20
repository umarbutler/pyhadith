# -*- coding: utf-8 -*-
# Import the pyHadith package.
import pyhadith
# Create a 'Hadith' object.
hadithObj = pyhadith.Hadith()
# Set the hadith to be pre-processed.
text = u'حَدَّثَنَا مُحَمَّدُ بْنُ بَشَّارٍ، حَدَّثَنَا أَبُو أَحْمَدَ، حَدَّثَنَا سُفْيَانُ، عَنْ يَزِيدَ أَبِي خَالِدٍ الدَّالاَنِيِّ، عَنْ رَجُلٍ، عَنْ جَابِرِ بْنِ عَبْدِ اللَّهِ، قَالَ صَنَعَ أَبُو الْهَيْثَمِ بْنُ التَّيْهَانِ لِلنَّبِيِّ صلى الله عليه وسلم طَعَامًا فَدَعَا النَّبِيَّ صلى الله عليه وسلم وَأَصْحَابَهُ فَلَمَّا فَرَغُوا قَالَ ‏"‏ أَثِيبُوا أَخَاكُمْ ‏"‏ ‏.‏ قَالُوا يَا رَسُولَ اللَّهِ وَمَا إِثَابَتُهُ قَالَ ‏"‏ إِنَّ الرَّجُلَ إِذَا دُخِلَ بَيْتُهُ فَأُكِلَ طَعَامُهُ وَشُرِبَ شَرَابُهُ فَدَعَوْا لَهُ فَذَلِكَ إِثَابَتُهُ ‏"‏ ‏.‏'
# Pre-process the hadith.
hadithObj.preprocess(text)
# Print the resulting attributes.
print({
	"raw" : hadithObj.raw,
	"clean" : hadithObj.clean
})
# Call the 'segment' function.
hadithObj.segment()
# Print the resulting attributes.
print({
	"matn" : hadithObj.matn,
	"isnad" : hadithObj.isnad
})
# Call the 'categorize' function.
hadithObj.categorize()
# Print the resulting attributes.
print(hadithObj.category)
# Call the 'treeify' function.
hadithObj.treeify()
# Print the resulting attributes.
print(hadithObj.tree)
# Store all of the available attributes.
result = {
	"raw" : hadithObj.raw,
	"clean" : hadithObj.clean,
	"matn" : hadithObj.matn,
	"isnad" : hadithObj.isnad,
	"category" : hadithObj.category,
	"tree" : hadithObj.tree
}
# Print all of the available attributes.
print('All of the available attributes:\n',result)
# Import json.dumps so that all of the available attributes can be printed in JSON format.
import json
# Print all of the available attributes, in JSON format.
print('All of the available attributes (JSON format):\n',json.dumps(result))