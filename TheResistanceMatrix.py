from minizinc import Instance, Model, Solver
import numpy as np

MORSE_CODE_DICT = {'A': [1, 2], 'B': [2, 1, 1, 1],
                   'C': [2, 1, 2, 1], 'D': [2, 1, 1], 'E': [1],
                   'F': [1, 1, 2, 1], 'G': [2, 2, 1], 'H': [1, 1, 1, 1],
                   'I': [1, 1], 'J': [1, 2, 2, 2], 'K': [2, 1, 2],
                   'L': [1, 2, 1, 1], 'M': [2, 2], 'N': [2, 1],
                   'O': [2, 2, 2], 'P': [1, 2, 2, 1], 'Q': [2, 2, 1, 2],
                   'R': [1, 2, 1], 'S': [1, 1, 1, ], 'T': [2],
                   'U': [1, 1, 2], 'V': [1, 1, 1, 2], 'W': [1, 2, 2],
                   'X': [2, 1, 1, 2], 'Y': [2, 1, 2, 2], 'Z': [2, 2, 1, 1]}


# Input vocabulary converter to number
def converter(word):
    var=[]
    if len(word)>=20 and len(word)<=0:
        print("Parola troppo lunga.")
        return
    for j in range(len(word)):
            var = var+MORSE_CODE_DICT[word[j]]
    return var

# Create a MiniZinc model

gecode = Solver.lookup("gecode")

model=Model()
model.add_string("""
include "globals.mzn";

0..pow(10,5): n;
0..pow(10,5): lmax;
array[1..n] of int: len;
array[1..n,1..max(len)] of int: c;
array[1..lmax] of int: morse;
array [1..lmax] of var 1..n: frase; 
array [1..lmax] of var int: sa;

constraint frase[1] !=n ;
constraint forall(i in 2..lmax)(if sum(j in 1..i-1)(len[frase[j]])<lmax then frase[i]!= n else frase[i]= n endif);
constraint forall(i in 1..len[frase[1]])(sa[i]=c[frase[1],i]);
constraint forall(i in 2..lmax)(forall(j in 1..len[frase[i]])(sa[sum(k in 1..i-1)(len[frase[k]])+j]=c[frase[i],j]));
constraint sa = morse;

output[show(sa)++show(frase)]
""")

# Transform Model into a instance

inst = Instance(gecode, model)

vocabulary = ["HELL","HELLO","OWORLD","WORLD","TEST"]
morse = [1,1,1,1,1,1,2,1,1,1,2,1,1,2,2,2,1,2,2,2,2,2,1,2,1,1,2,1,1,2,1,1]
leng = np.array([len(converter(i)) for i in vocabulary])
leng=np.append(leng,0)

voc=np.zeros((len(vocabulary)+1,max(leng)))
k=[]
for i in range(len(vocabulary)):
    k=np.concatenate([converter(vocabulary[i]),np.zeros(max(leng)-len(converter(vocabulary[i])))])
    voc[i,:]=+k

inst["n"] = 6
inst["morse"] = morse
inst["len"] = leng
inst["c"] = voc.astype(int)
inst["lmax"]= len(morse)

result = inst.solve(all_solutions=True)

# Output
for sol in result.solution:
    print(sol.frase)
if len(result.solution)>=0 and len(result.solution)<2^63:
    print(len(result.solution))
else:
    print("Number of solutions is too high.")