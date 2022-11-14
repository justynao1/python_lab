
import re


def switchWords():
    sentence = "The original logo was in use from its launch in March 2006 until September 2010."
    to_replace = {
        "was": "is",
        "original": "copied",
        "March": "May",
        "2010": "2012"
    }
    for key, value in to_replace.items():
        sentence = sentence.replace(key, value)

    print(sentence)


switchWords()
