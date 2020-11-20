# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - INSERT_DATE

### Added

- Added a filter for "\u200f" unicode character (right-to-left mark) in preprocess function of helpers.py.
- Added a preprocess function in Hadith class. This will allow Hadith objects to be re-used.

### Changed

- Changed initialization function of Hadith class to load in necessary spaCy models and Arabic words list. This will improve performance by allowing a Hadith object to be re-used.
- Fixed bug with installing pyHadith on Windows by specifying that [README.md](INSERT_LINK) is encoded in UTF-8, in [setup.py](INSERT_LINK).
- Renamed the *asl* model to *masdar*.
- Renamed the *ajza* model to *muqasim*.
- Renamed the *deconstruct* function of Hadith class, to *segment*.
- Renamed *atar* attribute to *athar*.
- Changed installation requirements to require PyArabic version 0.6.10 or greater.

### Removed

- Removed pre-processing of hadiths in initialization function of Hadith class. Pre-processing is now handled by a new function (named preprocess).
- Removed the ability to use a custom Arabic words list.
- Removed non-Arabic words and characters from [words.ar](INSERT_LINK).
- Removed [hadith.py](INSERT_LINK).
- Removed [connector.py](INSERT_LINK).

## [0.1.2] - 2020-07-10

### Changed

- Corrected typos in the deconstruct function of [helpers.py](https://github.com/umarbutler/pyhadith/blob/v0.1.2/pyhadith/helpers.py).
- Fixed bug in the deconstruct function of [helpers.py](https://github.com/umarbutler/pyhadith/blob/v0.1.2/pyhadith/helpers.py). The matn and isnad are now split at the last occurrence of a narrator name, preceding the last 'BEGINMATN' tag.

## [0.1.1] - 2020-07-08

### Changed

- Fixed typos and errors in [README.md](https://github.com/umarbutler/pyhadith/blob/v0.1.1/README.md).
- Fixed major issues with the importation of spaCy models and the arabic words list. [MANIFEST.in](https://github.com/umarbutler/pyhadith/blob/v0.1.1/MANIFEST.in) and [pkg_resources](https://setuptools.readthedocs.io/en/latest/pkg_resources.html) are now used to import and access data files.
- Fixed the download_url for the pyhadith package.

## [0.1.0] - 2020-06-24

### Added

- Introduced two new separate [spaCy](https://spacy.io/) statistical models: the *ajza* Text Classification model, and *musaid* Named Entity Recognition model.
- Created new distinct functions in the *Hadith* class, for deconstructing, categorizing, and reconstructing the asnad, of ahadith.
- Introduced three new algorithms for processing of ahadith.

### Changed

- The *Hadith* class is now available directly from the *pyhadith* package.
- Updated P,R,F scores for the *ajza*, *asl*, *rawa* and *musaid* models in [README.md](https://github.com/umarbutler/pyhadith/blob/v0.1.0/README.md).
- Updated [README.md](https://github.com/umarbutler/pyhadith/blob/v0.1.0/README.md) to reflect changes in how ahadith are proccessed and deconstructed by pyHadith.
- The *matn*, *isnad* and *category* attributes of the *Hadith* class are now only available from the new *deconstruct*, *treeify* and *categorize* functions.
- Re-trained the *rawa* and *musaid* [spaCy](https://spacy.io/) statistical models.

### Removed

- Removed the *hadith* module.
- Removed the *ahadith* [spaCy](https://spacy.io/) statistical model from code and documentation.

## [0.0.3] - 2020-04-13

### Added

- Introduced two new separate [spaCy](https://spacy.io/) statistical models: the *rawa* NER model, and, the *asl* Text Classification model.
- Added a CHANGELOG.md file to track version changes.

### Changed

- Updated P,R,F scores for the, now separate, *rawa* and *asl* models in [README.md](https://github.com/umarbutler/pyhadith/blob/v0.0.2-pre_alpha/README.md).
- Changed version name to conform with [Semantic Versioning](https://semver.org/spec/v2.0.0.html) standards.

### Removed

- Removed the *ahadith* [spaCy](https://spacy.io/) statistical model from code and documentation.

## [0.0.2] - 2020-04-13

### Changed

- Fixed errors in the description of [spaCy](https://spacy.io/) statistical models in [README.md](https://github.com/umarbutler/pyhadith/blob/v0.0.2-pre_alpha/README.md).

## [0.0.1] - 2020-04-13

### Added

- *ahadith* [spaCy](https://spacy.io/) statistical model.
- Ahadith deconstruction functionality.
- Asnad Reconstruction Algorithm integration.
