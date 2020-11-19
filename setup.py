# Import setup tools
import setuptools

# Set up long description
with open("README.md", mode="r", encoding="utf8") as fh:
    long_description = fh.read()

# Setuptools setup

setuptools.setup(
    name="pyHadith",
    version="0.1.2",
    author="Umar Butler",
    author_email="umar@umarbutler.com",
    description="A package which automatically segments, categorizes and reconstructs the asnad of, ahadith.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umarbutler/pyhadith",
    packages=setuptools.find_packages(),
    keywords='ahadith hadith isnad nlp arabic',
    classifiers=[
		"Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Natural Language :: Arabic",
		"Topic :: Text Processing"
    ],
    python_requires='>=3.6',
    install_requires=["spacy==2.2.4","nltk==3.4.5","pyarabic==0.6.10"],
    include_package_data=True,
    download_url="https://github.com/umarbutler/pyhadith/archive/0.1.2.tar.gz"
)