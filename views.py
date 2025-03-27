from main import app
from flask import render_template, request, redirect
from backEnd.listaEncadeada import listaDuplaEncadeada as lista
from backEnd import funcoes_auxiliares as fa
from backEnd.busca import buscaGrid  
from backEnd.mainGrid import MainGrid

busca = buscaGrid()  
caminho = [] 
nx, ny = 10, 15
mapa = MainGrid.Gera_Problema(nx,ny,qtd=6)
l_max = 10

@app.route("/", methods=['GET', 'POST'])
def resposta():
    print(mapa)
    if request.method == 'POST':
      
        inicio = request.form.get("inicio")
        objetivo = request.form.get("objetivo")
        obstaculos = request.form.get("obstaculos") 
        metodo = request.form.get("metodo")

        try:
            # Converte 
            inicio = list(map(int, inicio.split(',')))
            objetivo = list(map(int, objetivo.split(',')))
            obstaculos = int(obstaculos) 
            metodo = str(metodo)

            
            print(f"Valor recebido: {inicio} {objetivo} {obstaculos} {metodo}")
            
            
            if metodo == "amplitude":
                caminho = busca.amplitude(inicio, objetivo, nx, ny, mapa)
                print(caminho)

            elif metodo == "aprof_iterativo": 
                caminho = busca.aprof_iterativo(inicio, objetivo, nx, ny, mapa, l_max)
                print(caminho)

            elif metodo == "bidirecional":
                caminho = busca.bidirecional(inicio, objetivo, nx, ny, mapa)
                print(caminho)

            elif metodo == "profundidade":
                caminho = busca.profundidade(inicio, objetivo, obstaculos, nx, ny, mapa)
                print(caminho)

            elif metodo == "profundidade_limitada": 
                caminho = busca.prof_limitada(inicio, objetivo, obstaculos, nx, ny, mapa)
                print(caminho)
           
           
            else:
                return "Método de busca inválido." 

            
            if caminho:
                
                return render_template("homepage.html", caminho=caminho)
            else:
                return "Caminho não encontrado."
        
        except ValueError:
            
            return "Erro: Algum valor inserido não é válido."

    return render_template("homepage.html")
