# ISTRUZIONI GRAFO 4.0
Il file di input si deve chiamare "input grafi 4.0" e deve avere il percorso "C:\Users\(nome utente variabile)\Desktop\grafo 4.0"
Due nodi non possono avere lo stesso nome.
Un ramo può essere non orientato quindi a x-y corrisponde y-x, oppure orientato.
I diversi comandi DEVONO essere staccati da uno spazio o più. All'interno dello stesso comando NON inserire spazi.
    Es. a(n6,n2,7) a(n3,n5,6) 		NO a (n1, n6,5)
1) "n" più "pedaggio" per aggiungere un nuovo nodo. Scrivere accanto alla "n" il nome del nodo e, se presente, il pedaggio del nodo, staccato da una virgola. Il pedaggio è un valore legato al nodo.
    Es. nA oppure n(A) oppure nA,8
2) "a" oppure "arco" per aggiungere un nuovo ramo non orientato, seguito dai nomi dei nodi e dal valore del ramo, separati da virgole. Se il ramo non è pesato, non aggiungere il valore. I nodi collegati vengono creati automaticamente, se non ancora esistenti.
    Es. aA,B,8 oppure arco(A,B,8) oppure a(A,B,8).
3) "o" per aggiungere un nuovo ramo orientato, specificando i nodi collegati. Il metodo di inserimento dei dati è lo stesso del comando "a".
4) "rimuovin" per rimuovere un nodo specificato, seguendo le istruzioni del comando "n". 
5) "rimuovir" per rimuover un ramo orientato. Seguire le istruzioni del comando "a", senza specificare il valore dell'arco.
6) "rimuovio" per rimuovere un ramo orientato.
7) "percorso" per mostrare tutti i possibili percorsi tra un nodo di partenza e uno di arrivo. Seguire le istruzioni del comando "a", senza specificare il valore dell'arco.
    Es. percorso(B,A)
