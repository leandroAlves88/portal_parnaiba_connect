from flask import Flask, render_template, jsonify

from motor_de_busca import motor_pci

app = Flask(__name__)


@app.route("/")
def home():
    """Rota de acesso a pagina a pagina princial."""
    return render_template("home.html")


@app.route("/pciconcursos")
def resultados():
    """Rota de acesso a pagina PCI Concursos."""
    return render_template("/pciconcursos.html")


@app.route("/painel_dengue")
def painel_dengue():
    """Rota de acesso a pagina de jc concursos."""
    return render_template("painel_dengue.html")


@app.route("/painel_transparencia")
def painel_transparencia():
    """Rota de acesso a pagina de jc concursos."""
    return render_template("painel_transparencia.html")


@app.route("/historia")
def historia():
    """Rota de acesso a pagina de jc concursos."""
    return render_template("historia.html")


@app.route("/login")
def login():
    """
    Essa função tem o objetivo exibir a pagina de login.
    """
    # campo_login = request.form["txtUsuario"]
    # campo_senha = request.form["txtSenha"]
    # print(campo_login)
    # print(campo_senha)
    return render_template("/login.html")


@app.route("/sobre")
def sobre():
    """
    Essa função tem o objetivo exibir a pagina de sobre.
    """
    return render_template("sobre.html")


@app.route("/cadastro")
def cadastro():
    """
    Essa função tem o objetivo exibir a pagina de cadastro.
    """
    return render_template("cadastro.html")


"""---ENDPOINTS---"""


@app.route("/buscaVagasPCI/<campo_busca>", methods=["GET"])
def resultados_busca(campo_busca):
    """Essa função tem o objetivo exibir a pagina dos resultados das buscas."""

    print(f"campo pesquisar: {campo_busca}")
    retorno_vagas = motor_pci.get_concursos_pci(campo_busca)
    return jsonify(retorno_vagas)


@app.route("/buscaVagas/cioeste", methods=["GET"])
def busca_cisoeste():
    """Essa função tem o objetivo exibir as vagas das cidades pertencentes ao grupo cisoeste."""
    retorno_vagas = motor_pci.get_concursos_cisoeste()
    return jsonify(retorno_vagas)


@app.route("/buscaVagas/cioeste/<cidade>", methods=["GET"])
def busca_cisoeste_cidade(cidade):
    """Essa função tem o objetivo exibir a pagina dos resultados das buscas."""

    print(f"campo pesquisar: {cidade}")
    retorno_vagas = motor_pci.get_concursos_cisoeste_cidade(cidade)
    return jsonify(retorno_vagas)


if __name__ == "__main__":
    app.run(debug=True)  # <-- Modo Debug
