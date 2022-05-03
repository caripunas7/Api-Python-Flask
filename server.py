

from flask import Flask

empregados = [
                {'nome':'Caripunas', 'cargo':'Analista', 'salario':5000},
                {'nome':'Tiago', 'cargo':'Analista', 'salario':4000},
                {'nome':'Natacha', 'cargo':'Desenvolvedor', 'salario':5000},
                ]

app =  Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

@app.route("/empregados")
def get_empregados():
    return {'empregados':empregados}

@app.route("/empregados/<cargo>")
def get_empregados_cargo(cargo):
    out_empregados = []
    for empregado in empregados:
        if cargo == empregado['cargo'].lower():
            out_empregados.append(empregado)
    return {'empregados': out_empregados}

if __name__ == "__main__":
    app.run(debug=True)