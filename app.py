from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Meu estoque inicial
estoque = {
    "Cimento": 500,
    "Cal": 300,
    "Piso ref. 4343": 300,
}

@app.route("/")
def index():
    return render_template("index.html", estoque=estoque)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    produto = request.form.get("produto").strip()
    quantidade = request.form.get("quantidade", type=int)
    
    if produto and quantidade is not None:  # Essa é a minha garantia para que os dados não sejam nulos
        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade
    return redirect(url_for("index"))

@app.route("/remover", methods=["POST"])
def remover():
    produto = request.form.get("produto").strip()
    quantidade = request.form.get("quantidade", type=int)
    
    if produto in estoque and quantidade is not None:  # Aqui é minha garantia para que os dados sejam válidos
        estoque[produto] -= quantidade
        if estoque[produto] <= 0:
            del estoque[produto]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
