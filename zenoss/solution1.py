"""
author  Julio Ruano
email   jruano03@gmail.com

Simple program to discover the missing letters from the ascii set
of characters for a given string.
"""
from string import ascii_lowercase


class PangramDetector:
    def findMissingLetters(self, sentence):
        letters = ""
        for char in ascii_lowercase:
            if char not in sentence.lower():
                letters += char
        return letters


# Test PangramDetector
p1 = PangramDetector()
print p1.findMissingLetters("The quick brown fox jumps over the lazy dog")
print p1.findMissingLetters(
    "The slow purple oryx meanders past the quiescent canine"
)
print p1.findMissingLetters("We hate Bagginses")
print p1.findMissingLetters("")