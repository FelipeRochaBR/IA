from main import app
from flask import render_template, request, jsonify
from backEnd.listaEncadeada import listaDuplaEncadeada as lista
from backEnd import funcoes_auxiliares as fa
from backEnd.busca import buscaGrid  
from backEnd.mainGrid import MainGrid

busca = buscaGrid()  
caminho = [] 
nx, ny = 10, 15
mapa = MainGrid.Gera_Problema(nx,ny,qtd=26)

@app.route("/", methods=['GET', 'POST'])
def resposta():
    print(mapa)
    if request.method == 'POST':
      
        inicio = request.form.get("inicio")
        objetivo = request.form.get("objetivo")
        metodo = request.form.get("metodo")
        if metodo in ['profundidade_limitada', 'aprof_iterativo']:
            limite = request.form.get("limite")
            limite = int(limite) 

        try:
         
            inicio = list(map(int, inicio.split(',')))
            objetivo = list(map(int, objetivo.split(',')))
            metodo = str(metodo)
              # while True:
    #            x1  = inicio[0]
    #            y1 = inicio[1]
    #            if mapa[x][y]==0:
    #             break
    #            origem = [x,y]

    #           while True:
    #    
    #            x2 =objetivo=[0]
    #            y2 = objetivo=[1]
    #            if mapa[x][y]==0:
    #             break
    #           
    #             objetivo = [x,y]

            if metodo == "aestrela":
                caminho = busca.aestrela(inicio, objetivo, mapa, nx, ny)
                print(caminho)

            elif metodo == "aiaestrela":
                caminho = busca.aiaestrela(inicio, objetivo, mapa, nx, ny, limite=5)
                print(caminho)

            elif metodo == "amplitude":
                caminho = busca.amplitude(inicio, objetivo, nx, ny, mapa)
                print(caminho)

            elif metodo == "aprof_iterativo": 
                caminho = busca.aprof_iterativo(inicio, objetivo, nx, ny, mapa, limite)
                print(caminho)

            elif metodo == "bidirecional":
                caminho = busca.bidirecional(inicio, objetivo, nx, ny, mapa)
                print(caminho)

            elif metodo == "custouniforme":
                caminho = busca.custouniforme(inicio, objetivo, mapa, nx, ny)
                print(caminho)

            elif metodo == "greedy":
                caminho = busca.greedy(inicio, objetivo, mapa, nx, ny)
                print(caminho)

            elif metodo == "profundidade":
                caminho = busca.profundidade(inicio, objetivo, nx, ny, mapa)
                print(caminho)

            elif metodo == "profundidade_limitada": 
                caminho = busca.prof_limitada(inicio, objetivo, nx, ny, mapa,limite)
           
            else:
                return "Método de busca inválido." 

            
            if caminho:
                print(inicio)
                print(objetivo)
                return render_template("homepage.html", caminho=caminho,mapa=mapa,inicio=inicio,objetivo=objetivo)
            else:
                return render_template("homepage.html",mapa=mapa,mensagem='CAMINHO NÃO ENCONTRADO')
        
        except ValueError:
            
            return "Erro: Algum valor inserido não é válido."

    return render_template("homepage.html",mapa=mapa)
