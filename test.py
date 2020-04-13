# -*- coding: utf-8 -*-
# Import the 'hadith' module of pyHadith.
import pyhadith.hadith as hadith
# Set the hadith to be processed.
text = u'حَدَّثَنِي يَحْيَى، عَنْ مَالِكٍ، أَنَّهُ بَلَغَهُ أَنَّ سَعِيدَ بْنَ الْمُسَيَّبِ، وَسُلَيْمَانَ بْنَ يَسَارٍ، كَانَا يَقُولاَنِ عِدَّةُ الأَمَةِ إِذَا هَلَكَ عَنْهَا زَوْجُهَا شَهْرَانِ وَخَمْسُ لَيَالٍ ‏.‏'
# Create a hadith object using the text of the hadith.
x = hadith.Hadith(text)
# Print the resulting attributes.
print({
	"raw" : x.raw,
	"clean" : x.clean,
	"matn" : x.matn,
	"isnad" : x.isnad,
	"category" : x.category
})