# pyHadith

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![PyUp](https://pyup.io/repos/github/umarbutler/pyhadith/shield.svg)](https://pyup.io/account/repos/github/umarbutler/pyhadith/yt2mp3/)
[![PyPi Version](https://img.shields.io/pypi/v/pyhadith.svg)](https://pypi.python.org/pypi/pyhadith/)
[![Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)](https://pypi.python.org/pypi/yt2mp3/)

pyHadith is a python package which automatically segments and categorizes ahadith.

The package works by feeding raw text to custom natural language processing (NLP) models and algorithms. The resulting data is them aggregated and returned in a standardized format.

## 1. How It Works

### 1.1. Statistical Natural Language Processing Models

pyHadith uses four statistical natural language processing (NLP) models to deconstruct, extract narrators from, and categorize (i.e. [atar](https://en.wikipedia.org/wiki/Hadith#Distinction_from_other_literature), [khabar](https://en.wikipedia.org/wiki/Hadith#Distinction_from_other_literature)), ahadith. These are: a Text Classification model, known as *asl* (responsible for categorization); a Part-of-Speech tagging (POS tagging) model, known as *ajza* (responsible for deconstruction); a Named Entity Recognition (NER) model, known as *musaid* (responsible for deconstruction); and, a Named Entity Recognition (NER) model, trained only on asnad, known as *rawa* (responsible for narrator extraction).

The models were trained on manually annotated ahadith by the Saudi Arabian *[Permanent Committee for Scholarly Research and Ifta](https://sunnah.alifta.gov.sa/)*. Due to copyright, the data used to train the models cannot be reproduced. The models themselves, however, are not copyrighted (except under our own GNU GPLv3 license) as they come under the fair use doctrine.

The models were generated by [spaCy](https://spacy.io/) version 2.2.4. The training corpus contained 102,153 annotated ahadith, taken from [sunnah.alifta.gov.sa](https://sunnah.alifta.gov.sa/). For the *rawa* model, duplicate asnad were removed from the corpus, resulting in the inclusion of 96,887 asnad. 20% of the ahadith in the datasets were withheld and used for evaluating models. After training models for 100 iterations, the best performing models were selected.

The results of the final models are displayed in the table below:

| Model | Model Type | Accuracy | Precision | Recall | F-Score |
|--|--|--|--|--|--|
| Asl   | Text Classification |  |  |  | 97.32 |
| Ajza   | Part-of-Speech Tagging | 99.48 |  |  |  |
| Musaid   | Named Entity Recognition |  | 98.99 | 99.20 | 99.10 |
| Rawa  | Named Entity Recognition |  | 99.05 | 99.44 | 99.25 |

### 1.2. Pre-Processor

Before a hadith is passed to a spaCy model, it is first 'cleaned' by a pre-processor.

The pre-processor strips away punctuation and extra white space.

The pre-processor also uses [Motaz Saad](https://github.com/motazsaad)'s '[split-waw-arabic](https://github.com/motazsaad/split-waw-arabic)' method to identify and add whitespaces after the word 'وَ'. This is necessary to differentiate between the letter 'و‎' and the word 'وَ' (meaning 'and').

### 1.3. Rawa Post-Processor

To ensure that the names extracted by the *rawa* model are accurate, a post-processor looks for common joining terms at the beginning of each name (i.e. where the word 'min' (meaning from) is included as part of the name of a narrator). If a common joining term is found, it is removed from the name.

### 1.4. Hadith Deconstruction Algorithm

To deconstruct a hadith into a matn and an isnad, a custom algorithm is employed. This algorithm relies on the *ajza* and *musaid* models. It first splits a matn at the last occurrence of a 'BEGINMATN' tag (identified by *ajza*). It then searches for narrators within text the before the last 'BEGINMATN' tag. If a narrator has not been found after 6 or more tokens, it assumes that the last narrator identified to be the actual last narrator. All the text before the token immediately succeeding that narrator is then labelled as the isnad. The text after it is labelled the matn.

### 1.5. Asnad Reconstruction Algorithm

An Asnad Reconstruction algorithm is employed to standardize narrational relationships in a tree-like data structure.

There are two possible relationships recognized by the algorithm: A **from** B, and, A **from** B **and** C. Thus, where a term joins two or more narrators to a single narratee, that narratee will have multiple 'parent' narrators. Multiple 'parents' are identified by looking for the arabic word 'وَ'.

## 2. Installation

pyHadith is available on pip. You can install pyHadith using the following command:

    pip install pyHadith

The following python packages will also be automatically installed as dependencies of pyHadith:

| Package | Version | Description |
|--|--|--|
| [spaCy](https://github.com/explosion/spaCy) | 2.2.4 | Used to interact with the *rawa* and *asl* models.
| [pyArabic](https://github.com/linuxscout/pyarabic) | >= 0.6.7 | Used to remove diacritics from arabic strings.
| [nltk](https://github.com/nltk/nltk) | >= 3.4.5 | Used to tokenize arabic strings.

## 3. Usage

### 3.1. Import pyHadith

The first step in using pyHadith is to import the package to your code. You can do so with the following line:

    # Import the pyHadith package.
    import pyHadith

### 3.2. Create a 'Hadith' Object

Before you can deconstruct and analyse a hadith, you must first create a 'Hadith' object. This requires the passing of a single argument, a UTF-8 encoded Arabic text with diacritics.

The code below demonstrates how a 'Hadith' object can be created:

    # Continue on from example code in 3.1.
    # Set the hadith to be processed.
    text = u'حَدَّثَنِي يَحْيَى، عَنْ مَالِكٍ، أَنَّهُ بَلَغَهُ أَنَّ سَعِيدَ بْنَ الْمُسَيَّبِ، وَسُلَيْمَانَ بْنَ يَسَارٍ، كَانَا يَقُولاَنِ عِدَّةُ الأَمَةِ إِذَا هَلَكَ عَنْهَا زَوْجُهَا شَهْرَانِ وَخَمْسُ لَيَالٍ ‏.‏'
    # Create a 'Hadith' object using the text of the hadith.
    x = pyhadith.Hadith(text)
    # Print the resulting attributes.
    print({
        "raw" : x.raw,
        "clean" : x.clean
    })

Once a 'Hadith' object is created, the following attributes will become available:

| Attribute | Data Type | Description |
|--|--|--|
| raw | String | The original raw text. |
| clean | String | The cleaned raw text. |

### 3.3. Deconstruct a Hadith

To deconstruct a hadith into a matn and an isnad, you must call the 'deconstruct' function of a 'Hadith' object. The 'deconstruct' function takes no arguments (other than the object itself).

The code below demonstrates how this is done:

    # Continue on from example code in 3.2.
    # Call the 'deconstruct' function.
    x.deconstruct()
    # Print the resulting attributes.
    print({
        "matn" : x.matn,
        "isnad" : x.isnad
    })

Once the function has been called, the following attributes will become available:
| Attribute | Data Type | Description |
|--|--|--|
| matn | Dictionary | A dictionary containing the 'raw' text, 'start_char' index (in the cleaned text), and 'end_char' index (in the cleaned text), of the matn. |
| isnad | Dictionary | A dictionary containing the 'raw' text, 'start_char' index (in the cleaned text), and 'end_char' index (in the cleaned text), of the isnad, along with a 'narrators' list which contains the names and character indices of narrators. |

### 3.4. Categorize a Hadith

To categorize a hadith, you must call the 'categorize' function of your 'Hadith' object. Like the 'deconstruct' function, this function does not require the passing of any arguments. This function does not require you to have previously called the 'deconstruct' function.

The code below demonstrates how you can call the function:

    # Continue on from example code in 3.2.
    # Call the 'categorize' function.
    x.categorize()
    # Print the resulting attributes.
    print(x.category)

Once the 'categorize' function has been called, the 'category' attribute will become available.

| Attribute | Data Type | Description |
|--|--|--|
| category | Dictionary | A dictionary containing the 'name' (either 'atar' or 'khabar') and 'score' (from .5 to 1) of the assigned category. |

### 3.5. Reconstruct an Isnad

To reconstruct the isnad of your 'Hadith' object, you must call the 'treeify' function of a 'Hadith' object. Before calling the function, however, you must have already called the 'deconstruct' function.

The code below demonstrates how you can call the 'treeify' function:

    # Continue on from example code in 3.3.
    # Call the 'treeify' function.
    x.treeify()
    # Print the resulting attributes.
    print(x.tree)

Once the 'treeify' function has been called, the 'tree' attribute will be created. This attribute is a list which contains 'narrator' dictionaries.

A 'narrator' dictionary in the 'tree' list will contain the following keys:

| Key | Data Type | Description |
|--|--|--|
| id | Integer | A unique identifier number. |
| name | String | The raw text of the narrator's name. |
| start_char | Integer | The character index in the cleaned text where the name begins. |
| end_char | Integer | The character index in the cleaned text where the name ends. |
| parents | List | A list of the ids of the narrator's parents within the isnad. |

## 4. Changelog

The changelog for pyHadith is available in the [CHANGELOG.md](https://github.com/umarbutler/pyhadith/blob/master/CHANGELOG.md) file.

## 5. License

pyHadith is licensed under [GPLv3](https://github.com/umarbutler/pyhadith/blob/master/LICENSE). pyArabic, spaCy and NLTK are licensed under [GPLv3](https://github.com/linuxscout/pyarabic/blob/master/LICENSE), [MIT](https://github.com/explosion/spaCy/blob/master/LICENSE), and [Apache 2.0](https://github.com/nltk/nltk/blob/develop/LICENSE.txt), respectively. These licenses are all GPL compatible.
