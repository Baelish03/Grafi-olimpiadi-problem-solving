print ('Il programma dispone di un file di input e uno di istruzioni, essenziali per la buona esecuzione del programma.')
import networkx as nx
from pandas import option_context
from pandas import DataFrame
from os import chdir as cd

G=nx.DiGraph()

def n(node,*costo):
    G.add_node(node,pedaggio=costo)
    
def r(primonodo,secondonodo,*valore):
    G.add_edge(primonodo, secondonodo, peso=valore)
    G.add_edge(secondonodo, primonodo, peso=valore)

def o(primonodo,secondonodo,*valore):
    G.add_edge(primonodo, secondonodo, peso=valore)

def rn(nodo):
    if nodo in G.nodes:
        G.remove_node(nodo)
    else:
        print('Il nodo del comando rimuovin non esiste')

def ro(primo_nodo,secondo_nodo):
    if primo_nodo in G.nodes and secondo_nodo in G.nodes and (primo_nodo, secondo_nodo) in G.edges:
        G.remove_edge(primo_nodo, secondo_nodo)
    else:
        print('I nodi e/o il ramo del comando rimuovio non esistono') 

def rr(primo_nodo,secondo_nodo):
    if primo_nodo in G.nodes and secondo_nodo in G.nodes and (primo_nodo, secondo_nodo) in G.edges and (secondo_nodo, primo_nodo) in G.edges:
        G.remove_edge(primo_nodo, secondo_nodo)
        G.remove_edge(secondo_nodo, primo_nodo)
    else:
        print('I nodi e/o il ramo del comando rimuovir non esistono')

def p(nodo_partenza,nodo_arrivo):
    if nodo_partenza in G.nodes and nodo_arrivo in G.nodes:

        #percorsi
        liste_percorsi=list(nx.all_simple_paths(G,nodo_partenza,nodo_arrivo))

        #lungezza percorsi
        lista_somma_valori=[]
        for lista in liste_percorsi:
            valori_rami_un_percorso=[]
            for k in range(len(lista)-1):
                valore=G.edges[str(lista[k]),str(lista[k+1])]['peso']
                for elem in valore:
                    valori_rami_un_percorso.append(elem)
            lista_somma_valori.append(sum(valori_rami_un_percorso))

        #numero di nodi attraversati
        nodi_attraversati=[]
        for lista2 in liste_percorsi:
            nodi_attraversati.append(len(lista2))

        #costo pedaggio
        #se il nodo non ha l'attributo pedaggio va dati default 0
        lista_somma_pedaggi=[]
        for lista2 in liste_percorsi:
            pedaggio_un_percorso=[]
            for ax in lista2:
                try:
                    pedaggio=G.nodes[ax]['pedaggio']
                except KeyError:
                    G.nodes[ax]['pedaggio']=(0,)
                    pedaggio=G.nodes[ax]['pedaggio']
                for e in pedaggio:
                    pedaggio_un_percorso.append(e)
            lista_somma_pedaggi.append(sum(pedaggio_un_percorso))

        with option_context('display.max_rows',None,'display.max_columns',None,'display.expand_frame_repr',False):
            df=DataFrame()
            df['Percorsi']=liste_percorsi
            df['Valore percorso']=lista_somma_valori
            df['Nodi']=nodi_attraversati
            df['Costo pedaggio']=lista_somma_pedaggi

            df.sort_values(by=['Valore percorso'], inplace = True)
            print('Valore percorso in ordine crescente')
            print(df,'\n')

            df.sort_values(by=['Nodi'], inplace = True)
            print('Numero di nodi attraversati in ordine crescente')
            print(df,'\n')

            df.sort_values(by=['Costo pedaggio'], inplace = True)
            print('Costo del pedaggio in ordine crescente')
            print(df,'\n')
            
    else:
        print('Il nodo di partenza e/o il nodo di arrivo del comando p non esistono')

#pià tabelle ordinate diversamente
try:
    cd('C:\\Users\\user\\Desktop\\grafi')
except FileNotFoundError:
    try:
        print('Il percorso del file di input non esiste, prova a inserirlo manualmente.')
        path=input('Percorso del file di input: ')
        cd(path)
    except FileNotFoundError:
        print('Il percorso inserito non è corretto.')
        esci2=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
        exit()

try:
    with open('input grafi v5.txt', 'r') as file:
        lista_riga_comandi=file.readlines()
    listacomando=[]
    for riga_comandi in lista_riga_comandi:
        comando=riga_comandi.split(' ')
        listacomando.append(comando)
except FileNotFoundError:
    print('Il file di input non esiste. Ricontrollare il percorso o il nome del file.')
    esci3=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
    exit()
    
#si creano più liste. per mettere tutto in una lista
c=[]
for a in listacomando:
    for b in a:
        c.append(b)

listaunica=[]
for el in c:
    el=el.replace('\n','')
    listaunica.append(el)

t=listaunica.count('')
for m in range(t):
    listaunica.remove('')

#pulizia input da parentesi e virgole
def pul(inp):
    inp=inp.replace('(','')
    inp=inp.replace(')','')
    inp=inp.replace('[','')
    inp=inp.replace(']','')
    inp=inp.replace('{','')
    inp=inp.replace('}','')
    inp=inp.split(',')
    return inp

for icu in listaunica:
    try:
        if icu[0]=='n':
            icu2=icu[1:]
            icu2=pul(icu2)
            if len(icu2)==2:
                try:
                    n(icu2[0],float(icu2[1]))
                except IndexError:
                    print('Inserire due variabili')
                except ValueError:
                    print('Inserire un numero al comando n')
            if len(icu2)==1:
                try:
                    n(icu2[0],float(0))
                except IndexError:
                    print('Inserire una variabile')

        elif icu[0:8]=='pedaggio':
            icu2=icu[8:]
            icu2=pul(icu2)
            if len(icu2)==2:
                try:
                    n(icu2[0],float(icu2[1]))
                except IndexError:
                    print('Inserire due variabili')
                except ValueError:
                    print('Inserire un numero al comando n')
            if len(icu2)==1:
                try:
                    n(icu2[0],float(0))
                except IndexError:
                    print('Inserire una variabile')
          
        elif icu[0]=='a':
            if icu[0:4]=='arco':
                icu2=icu[4:]
                icu2=pul(icu2)
            else:
                icu2=icu[1:]
                icu2=pul(icu2)
            if len(icu2)==3:
                try:
                    r(icu2[0],icu2[1],float(icu2[2]))
                except IndexError:
                    print('Inserire tre variabili')
                except ValueError:
                    print('Inserire un numero al comando a')
            elif len(icu2)==2:
                try:
                    r(icu2[0],icu2[1])
                except IndexError:
                    print('Inserire due variabili')

        elif icu[0]=='o':
            icu2=icu[1:]
            icu2=pul(icu2)
            if len(icu2)==3:
                try:
                    o(icu2[0],icu2[1],float(icu2[2]))
                except IndexError:
                    print('Inserire tre variabili')
                except ValueError:
                    print('Inserire un numero al comando o')
            elif len(icu2)==2:
                try:
                    o(icu2[0],icu2[1])
                except IndexError:
                    print('Inserire due variabili')

        elif icu[0:8]=='rimuovin':
            icu2=icu[8:]
            icu2=pul(icu2)
            try:
                rn(icu2[0])
            except IndexError:
                print('Inserire una variabili al comando rimuovin')

        elif icu[0:8]=='rimuovir':
            icu2=icu[8:]
            icu2=pul(icu2)
            try:
                rr(icu2[0],icu2[1])
            except IndexError:
                print('Inserire due variabili al comando rimuovir')

        elif icu[0:8]=='rimuovio':
            icu2=icu[8:]
            icu2=pul(icu2)
            try:
                ro(icu2[0],icu2[1])
            except IndexError:
                print('Inserire due variabili al comando rimuovio')

        elif icu[0:8]=='percorso':
            icu2=icu[8:]
            icu2=pul(icu2)
            try:
                p(icu2[0],icu2[1])
            except IndexError:
                print('Inserire due variabili al comando percorso')

    except IndexError:
        print('File di input vuoto')

esci=input('Sviluppato da Baelish03\nPremere Invio per uscire.')
#Aggiornato il 23/02/2023
