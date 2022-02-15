include "globals.mzn";

%Variables definition
0..pow(10,5): n;
0..pow(10,5): lmax;
array[1..n] of int: len;
array[1..n,1..max(len)] of int: c;
array[1..lmax] of int: morse;
array [1..lmax] of var 1..n: frase; 
array [1..lmax] of var int: sa;

%Constraints
constraint frase[1] !=n ;
constraint forall(i in 2..lmax)(if sum(j in 1..i-1)(len[frase[j]])<lmax then frase[i]!= n else frase[i]= n endif);
constraint forall(i in 1..len[frase[1]])(sa[i]=c[frase[1],i]);
constraint forall(i in 2..lmax)(forall(j in 1..len[frase[i]])(sa[sum(k in 1..i-1)(len[frase[k]])+j]=c[frase[i],j]));
constraint sa = morse;