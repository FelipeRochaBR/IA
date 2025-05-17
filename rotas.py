from main import app
import json
from flask import render_template, request, jsonify
from backEnd.listaEncadeada import listaDuplaEncadeada as lista
from backEnd import funcoes_auxiliares as fa
from backEnd.busca import buscaGrid 
from backEnd.buscaPeso import buscaGridPeso
from backEnd.mainGrid import MainGrid

busca = buscaGrid()  
buscaPeso= buscaGridPeso()
caminho = [] 
peso =int
nx, ny = 10, 15
mapa = MainGrid.Gera_Problema(nx,ny,qtd=26)

@app.route("/", methods=['GET', 'POST'])
def resposta():
    if request.method == 'POST':
      
        inicio = request.form.get("inicio")
        objetivo = request.form.get("objetivo")
        metodo = request.form.get("metodo")
        if metodo in ['profundidade_limitada']:
            limite = request.form.get("limite")
            limite = int(limite) 
         
        try:
            inicio = [int(x) for x in inicio.strip("()").split(',')]
            objetivo = [int(x) for x in objetivo.strip("()").split(',')]
            
            if mapa[inicio[0]][inicio[1]] == 9:
                return render_template("homepage.html", 
                                    mapa=mapa,
                                    mensagem='ERRO: Ponto inicial é um obstáculo!')
            
            if mapa[objetivo[0]][objetivo[1]] == 9:
                return render_template("homepage.html", 
                                    mapa=mapa,
                                    mensagem='ERRO: Ponto objetivo é um obstáculo!')
            
            if not (0 <= inicio[0] < nx and 0 <= inicio[1] < ny and
                   0 <= objetivo[0] < nx and 0 <= objetivo[1] < ny):
                return render_template("homepage.html", mapa=mapa, mensagem='Coordenadas Fora do Grid')
            
            mapa_peso = [[0 if cell == 9 else 1 for cell in row] for row in mapa]
            
                
            if metodo in ["aestrela", "aiaestrela", "custouniforme", "greedy"]:
                if metodo == "aestrela":
                    caminho, peso = buscaPeso.a_estrela(inicio, objetivo, mapa_peso, nx, ny)
                elif metodo == "aiaestrela":
                    caminho, peso = buscaPeso.aia_estrela(inicio, objetivo, mapa_peso, nx, ny, limite=limite if 'limite' in locals() else 5)
                elif metodo == "custouniforme":
                    caminho, peso = buscaPeso.custo_uniforme(inicio, objetivo, mapa_peso, nx, ny)
                elif metodo == "greedy":
                    caminho, peso = buscaPeso.greedy(inicio, objetivo, mapa_peso, nx, ny)

            elif metodo == "amplitude":
                caminho = busca.amplitude(inicio, objetivo, nx, ny, mapa)
                print(caminho)

            elif metodo == "aprof_iterativo": 
                caminho = busca.aprof_iterativo(inicio, objetivo, nx, ny, mapa,10)
                print(caminho)

            elif metodo == "bidirecional":
                caminho = busca.bidirecional(inicio, objetivo, nx, ny, mapa)
                print(caminho)

            elif metodo == "profundidade":
                caminho = busca.profundidade(inicio, objetivo, nx, ny, mapa)
                print(caminho)

            elif metodo == "profundidade_limitada": 
                caminho = busca.prof_limitada(inicio, objetivo, nx, ny, mapa,limite)
           
            else:
                return "Método de busca inválido." 

            
            if caminho and caminho != "Caminho não encontrado":
                return render_template("homepage.html", 
                                    caminho=caminho,
                                    mapa=mapa,
                                    inicio=inicio,
                                    objetivo=objetivo,
                                    valor=f"Custo: {peso}" if 'peso' in locals() else "")
            else:
                return render_template("homepage.html", 
                                    mapa=mapa,
                                    mensagem='CAMINHO NÃO ENCONTRADO')
        except Exception as e:
            print(f"Erro: {str(e)}")
            return render_template("homepage.html", 
                                mapa=mapa,
                                mensagem=f"Erro: {str(e)}")
    
    return render_template("homepage.html", mapa=mapa)
