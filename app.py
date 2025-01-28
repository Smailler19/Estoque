from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Meu estoque inicial
estoque = {
    "Cimento": 500,
    "Cal": 300,
    "Piso ref. 4343": 300,
    "Telha": 500,
}

@app.route("/")
def index():
    return render_template("index.html", estoque=estoque)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    produto = request.form.get("produto", "").strip()
    quantidade = request.form.get("quantidade", type=int)
    
    if not produto or quantidade is None or quantidade <= 0:
        return redirect(url_for("index"))
    
    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade
    return redirect(url_for("index"))

@app.route("/remover", methods=["POST"])
def remover():
    produto = request.form.get("produto", "").strip()
    quantidade = request.form.get("quantidade", type=int)
    
    if not produto or quantidade is None or quantidade <= 0:
        return redirect(url_for("index"))
    
    if produto in estoque:
        estoque[produto] -= quantidade
    else:
        estoque[produto] = -quantidade
    return redirect(url_for("index"))

@app.route("/pesquisa", methods=["POST"])
def pesquisa():
    nome = request.form.get("nome", "").strip().lower()
    resultados = None

    if nome:
        # Filtra os produtos pelo nome fornecido
        resultados = {k: v for k, v in estoque.items() if nome in k.lower()}

    return render_template("index.html", estoque=estoque, resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)
