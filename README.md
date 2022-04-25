# The-Resistance-in-MiniZinc
MiniZinc CSP applied to a coding game: "The Resistance"
https://www.codingame.com/training/expert/the-resistance

# Introduction
“*You work in the National Resistance Museum and you just uncovered hundreds of documents which contain coded Morse transmissions. In the documents, none of the spaces have
been transcribed to separate the letters and the words hidden behind the Morse sequence.
Therefore, there may be several interpretations of any single decoded sequence.*”

Given the description, it is easy to derive that the program must be able to determine the
exact number of different messages that it is possible to obtain from one Morse sequence,
given a dictionary.
In fact, Morse is a code composed of dots and dashes representing the letters of the alphabet.
Since none of the spaces have been transcribed, there may be several possible interpretations
(for example, the sequence -....–.-. could be any of the following, if they are present in the
dictionary: BAC, BANN, DUC, DU, TETE).
If we consider only short Morse sequences and small dictionaries, the problem could be simple
to implement. On the other hand, only an optimized algorithm can compute long sequences.

# Usage
Inside the folder, the file requirements.txt is included in order to retrieve the dependencies
needed to run the Python script.
After that, the program can be run using command line in its folder (dataname is the name
of the JSON file inside the data folder that needs to be used):
```
python TheResistance.py dataname.json
```

# Requirements
Can be found inside the requirements.txt
