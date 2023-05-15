from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("index.html", titulo_pagina="Página inicial")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html", titulo_pagina="Sobre nós")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/frequencia")
def freq():
    return render_template("freq.html", titulo_pagina="Frequência")

@app.route("/lista_de_funcionarios")
def employee_list():
    return render_template("list.html", titulo_pagina="Lista de Funcionarios")

@app.route("/registro_funcionarios")
def regisf():
    return render_template("registro_funcionarios.html", titulo_pagina="registro de funcionarios")

@app.route("/registro_de_horas_extras")
def register():
    return render_template("/registro_de_horas_extras.html", titulo_pagina="registro de horas extras")

if __name__ == "__main__":
    app.run(debug=True)
