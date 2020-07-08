# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2020-07-08

### Changed

- Fixed typos in [README.md](https://github.com/umarbutler/pyhadith/blob/v0.1.1/README.md).

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
