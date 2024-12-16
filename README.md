# GRAFI PROBLEM SOLVING

## ISTRUZIONI PROGRAMMA

Il file di input si deve chiamare "input grafi v5" in formato .txt e il percorso consigliato è "C:\Users\(nome utente variabile)\Desktop\grafi".
Due nodi non possono avere lo stesso nome.
Un ramo può essere non orientato quindi a x-y corrisponde y-x, oppure orientato.
I diversi comandi DEVONO essere staccati da uno spazio o più. All'interno dello stesso comando NON inserire spazi.
    Es. a(n6,n2,7) a(n3,n5,6) 		NO a (n1, n6,5).
1) "n" più "pedaggio" per aggiungere un nuovo nodo. Scrivere accanto alla "n" il nome del nodo e, se presente, il pedaggio del nodo, staccato da una virgola. Il pedaggio è un valore legato al nodo.
    Es. nA oppure n(A) oppure nA,8.
2) "a" oppure "arco" per aggiungere un nuovo ramo non orientato, seguito dai nomi dei nodi e dal valore del ramo, separati da virgole. Se il ramo non è pesato, non aggiungere il valore. I nodi vollegati vengono creati automaticamente.
    Es. aA,B,8 oppure arco(A,B,8) oppure a(A,B,8).
3) "o" per aggiungere un nuovo ramo orientato, specificando i nodi collegati. Il metodo di inserimento dei dati è lo stesso del comando "a".
4) "rimuovin" per rimuovere un nodo specificato, seguendo le istruzioni del comando "n". 
5) "rimuovir" per rimuover un ramo orientato. Seguire le istruzioni del comando "a", senza specificare il valore dell'arco.
6) "rimuovio" per rimuovere un ramo orientato.
7) "percorso" per mostrare tutti i possibili percorsi tra un nodo di partenza e uno di arrivo. Seguire le istruzioni del comando "a", senza specificare il valore dell'arco.
    Es. percorso(B,A).

## ESEMPIO
    
![](./esempio/grafo.png#center)

Inserire questi comandi nel file ```input grafi v5.txt```


```o(n4,n2,4) a(n3,n5,5) a(n1,n7,2) a(n6,n10,7) a(n5,n2,4) a(n4,n1,6)
o(n4,n12,3) a(n7,n4,3) a(n2,n9,4) a(n6,n3,2) a(n6,n11,3) o(n9,n7,3)
a(n1,n12,4) a(n8,n11,1) a(n8,n10,2) a(n8,n12,6) o(n10,n5,4)
p(n1,n3)
o(n4,n10,1) o(n10,n4,10)
p(n1,n3)```
