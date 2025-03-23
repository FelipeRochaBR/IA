from main import app
from flask import render_template, request, redirect

# rotas
@app.route("/")
def Gridpage():
    return render_template("homepage.html")

# rotas
@app.route("/", methods=['GET','POST'])
def resposta():
    if request.method == 'POST':
        inicioX = request.form.get("inicioX")
        inicioY = request.form.get("inicioY")
        objetivoX = request.form.get("objetivoX")
        objetivoY = request.form.get("objetivoY")
        obstaculos = request.form.get("obstaculos")
        metodo = request.form.get("metodo")

        if inicioX:  
            try:
                inicioX = int(inicioX)
                inicioY = int(inicioY)
                objetivoX = int(objetivoX) 
                objetivoY = int(objetivoY) 
                obstaculos = int(obstaculos) 
                metodo = str(metodo)
                print(f"Valor recebido: {inicioX} {inicioY} {objetivoX} {objetivoY} {obstaculos} {metodo}")  
                return redirect("/") 
            except ValueError:
                return "Erro: O valor inserido não é um número válido."
        else:
            return "Erro: O campo 'inicio' não foi preenchido."
        
        
         
    else: 
        return render_template("homepage.html")
        