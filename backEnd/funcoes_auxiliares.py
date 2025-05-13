import numpy as np
import random as rd
from math import sqrt

# Carrega Grafo para Lista de Adjacência e Lista de Nós
def Gera_Problema_Grafo(arquivo):
    f = open(arquivo,"r")
    
    i=0
    nos = []
    grafo = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        if i==0:
            nos = str1
        else:
            grafo.append(str1)
        i += 1       
    
    return nos, grafo


# Carrega Grafo para Lista de Adjacência e Lista de Nós
def Gera_Problema_Grid_Fixo(arquivo):
    f = open(arquivo,"r")
    
    mapa = []
    for str1 in f:
        str1 = str1.strip("\n")
        #str1 = str1.split(",")
        str1 = str1.split(";")
        int_str1 = []
        for s in str1:
            int_str1.append(int(s))
        mapa.append(int_str1)
    
    return mapa


def Gera_Problema_Grid(n,m,qt_ob):
    mapa = np.zeros((n,m),int)
    
    if qt_ob>n*m:
        return "ERRO"
    o = 0
    while o<qt_ob:
        i = rd.randrange(0,n)
        j = rd.randrange(0,m)
        if mapa[i][j]==0:
            mapa[i][j]=9
            o +=1
    return mapa
        
"""    
    f = open(arquivo,"r")
    
    mapa = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        for i in range(len(str1)):
            str1[i] = int(str1[i])
        mapa.append(str1)
    return mapa
"""    

def sucessor_grid(x,y,dx,dy,mapa):

    f = []

    # acima
    if y+1<dy:
        if mapa[x][y+1]!=9:
            linha = []
            linha.append(x)
            linha.append(y+1)
            f.append(linha)
    
    # esquerda
    if x-1>=0:
        if mapa[x-1][y]!=9:
            linha = []
            linha.append(x-1)
            linha.append(y)
            f.append(linha)

    # direita
    if x+1<dx:
        if mapa[x+1][y]!=9:
            linha = []
            linha.append(x+1)
            linha.append(y)
            f.append(linha)

    # abaixo
    if y-1>=0:
        if mapa[x][y-1]!=9:
            linha = []
            linha.append(x)
            linha.append(y-1)
            f.append(linha)
    
    if x+1<dx and y-1>=0:
        if mapa[x+1][y-1]!=9:
            linha = []
            linha.append(x+1)
            linha.append(y-1)
            f.append(linha)
    
    if x+1<dx and y+1<dy:
        if mapa[x+1][y+1]!=9:
            linha = []
            linha.append(x+1)
            linha.append(y+1)
            f.append(linha)
    
    if x-1>=0 and y-1>=0:
        if mapa[x-1][y-1]!=9:
            linha = []
            linha.append(x-1)
            linha.append(y-1)
            f.append(linha)
    
    if x-1>=0 and y+1<dy:
        if mapa[x-1][y+1]!=9:
            linha = []
            linha.append(x-1)
            linha.append(y+1)
            f.append(linha)
    
    return f

# Rotina sucessores para Grade de Ocupação
def sucessores(atual,mapa,dim_x,dim_y):
    f = []
    x = atual[0]
    y = atual[1]
    
    if y+1!=dim_y:
        if mapa[x][y+1]==1:
            linha = []
            linha.append(x)
            linha.append(y+1)
            custo = 1
            linha.append(custo)
            f.append(linha)
            
    if x+1!=dim_x:
        if mapa[x+1][y]==1:
            linha = []
            linha.append(x+1)
            linha.append(y)
            custo = 3
            linha.append(custo)
            f.append(linha)
            
    
    if x-1>=0:
        if mapa[x-1][y]==1:
            linha = []
            linha.append(x-1)
            linha.append(y)
            custo = 2
            linha.append(custo)
            f.append(linha)
            
    
    if y-1>=0:
        if mapa[x][y-1]==1:
            linha = []
            linha.append(x)
            linha.append(y-1)
            custo = 4
            linha.append(custo)
            f.append(linha)
            
    return f

def Gera_Ambiente(arquivo):
    f = open(arquivo,"r")
    
    mapa = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        for i in range(len(str1)):
            str1[i] = int(str1[i])
        mapa.append(str1)
    
    return mapa, len(mapa), len(mapa[0])

def h(p1,p2):
    if p1[0]<p2[0]:
        m1 = 3 # valor do custo da rotina sucessores para esta acao
    else:
        m1 = 2 # valor do custo da rotina sucessores para esta acao
    
    if p1[1]<p2[1]:
        m2 = 1 # valor do custo da rotina sucessores para esta acao
    else:
        m2 = 4 # valor do custo da rotina sucessores para esta acao
    
    # heurística SEM movimento em diagonal
    h = abs(p1[0]-p2[0])*m1 + abs(p1[1]-p2[1])*m2
    # heurística COM movimento em diagonal
    #h = sqrt(m1*(p1[0]-p2[0])*(p1[0]-p2[0]) + m2*(p1[1]-p2[1])*(p1[1]-p2[1]))
    return h

