from minizinc import Instance, Model, Solver
import numpy as np
import json


# Morse dictionary for conversion
MORSE_CODE_DICT = {'A': [1, 2], 'B': [2, 1, 1, 1],
                   'C': [2, 1, 2, 1], 'D': [2, 1, 1], 'E': [1],
                   'F': [1, 1, 2, 1], 'G': [2, 2, 1], 'H': [1, 1, 1, 1],
                   'I': [1, 1], 'J': [1, 2, 2, 2], 'K': [2, 1, 2],
                   'L': [1, 2, 1, 1], 'M': [2, 2], 'N': [2, 1],
                   'O': [2, 2, 2], 'P': [1, 2, 2, 1], 'Q': [2, 2, 1, 2],
                   'R': [1, 2, 1], 'S': [1, 1, 1, ], 'T': [2],
                   'U': [1, 1, 2], 'V': [1, 1, 1, 2], 'W': [1, 2, 2],
                   'X': [2, 1, 1, 2], 'Y': [2, 1, 2, 2], 'Z': [2, 2, 1, 1]}


# Getting vars from txt file
def getVarsFromJSON(filename):
    f = open(filename)
    data = json.loads(f.read())
    return data


# Input morse converter to number
def morse_converter(m):
    return [1 if i=='.' else 2 for i in m]


# Input vocabulary converter to number
def word_converter(word):
    var=[]
    if len(word)>=20 and len(word)<=0:
        print("Parola troppo lunga.")
        return
    for j in range(len(word)):
            var = var+MORSE_CODE_DICT[word[j]]
    return var


# Words of vocabulary's length calculator
def len_calculator(v):
    leng = np.array([len(word_converter(i)) for i in v])
    leng = np.append(leng,0)
    return leng


# Matrix generation from vocabulary
def vocabulary_matrix(v,l):
    voc=np.zeros((len(v)+1,max(l)))
    k=[]
    for i in range(len(v)):
        k=np.concatenate([word_converter(v[i]),np.zeros(max(l)-len(word_converter(v[i])))])
        voc[i,:]=+k
    return voc.astype(int)


# Solution cycle
def result_printer(result):
    for sol in result.solution:
        print(sol.frase)
    if len(result.solution)>=0 and len(result.solution)<2^63:
        print(len(result.solution))
    else:
        print("Number of solutions is too high.")


# Create a MiniZinc model
gecode = Solver.lookup("gecode")

model=Model()
model.add_file("TheResistance.mzn")


# Transform Model into a instance
inst = Instance(gecode, model)


# Instantiate variables from file
data = getVarsFromJSON("data.json")

inst["n"] = data["n"]+1
inst["morse"] = morse_converter(data["morse"])
inst["len"] = len_calculator(data["vocabulary"])
inst["c"] = vocabulary_matrix(data["vocabulary"],len_calculator(data["vocabulary"]))
inst["lmax"]= len(morse_converter(data["morse"]))


# Output
result = inst.solve(all_solutions=True)
result_printer(result)