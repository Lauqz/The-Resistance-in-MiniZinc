include "globals.mzn";

%Variables definition
0..pow(10,5): n;
0..pow(10,5): lmax;
array[1..n] of int: len;
array[1..n,1..max(len)] of int: voc;
array[1..lmax] of int: morse;
array [1..lmax] of var 1..n: words; 
array [1..lmax] of var int: out;

%Constraints
constraint words[1] != n;
constraint forall(i in 2..lmax)(if sum(j in 1..i-1)(len[words[j]])<lmax then words[i]!= n else words[i]= n endif);
constraint forall(i in 1..len[words[1]])(out[i]=voc[words[1],i]);
constraint forall(i in 2..lmax)(forall(j in 1..len[words[i]])(out[sum(k in 1..i-1)(len[words[k]])+j]=voc[words[i],j]));
constraint out = morse;