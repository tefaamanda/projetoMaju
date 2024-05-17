from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
    # Ler senha
    mensagem1 = ""
    mensagem2 = ""
    mensagem3 = ""
    mensagem4 = ""
    mensagem5 = ""
    mensagem6 = ""
    mensagem = ""
    if request.method == "POST":
        usuario = request.form['usuario']
        senha = request.form['senha']
    # Atribuindo valores

        quantidade = 0
        minuscula = 0
        maiuscula = 0
        caracter = 0
        numero = 0
        igual = 0

        # Cálculos de caracteres
        quant = len(senha)

        # Contando caracteres
        if quant >= 8:
            quantidade = 1

        if senha != usuario:
            igual = 1

        # Atribuindo condições
        for i in (senha):

            if i.isupper():
                maiuscula = 1

            if i.islower():
                minuscula = 1

            if i.isdigit():
                numero = 1

            if ((not i.isalpha()) and (not i.isdigit())):
                caracter = 1

        # Realizando impressões
        if numero == 0:
            mensagem1  = 'Sua senha precisa de números'
        if minuscula == 0:
            mensagem2 = 'Sua senha precisa de letras minúscula'
        if caracter == 0:
            mensagem3 = 'Sua senha precisa de caracteres especiais'
        if quantidade == 0:
            mensagem4 = 'Sua senha precisa de pelo menos 8 caracteres'
        if maiuscula == 0:
            mensagem5 = 'Sua senha precisa de letras maiúsculas'
        if igual == 0:
            mensagem6 = 'Seu usuário não pode ser igual a sua senha'
        if (quantidade == 1) and (numero == 1) and (caracter == 1) and (maiuscula == 1) and (minuscula == 1) and (igual == 1):
            mensagem = 'Senha cadastrada com sucesso!'
    return render_template('index.html', mensagem1 = mensagem1,mensagem2 = mensagem2, mensagem3 = mensagem3, mensagem4 = mensagem4, mensagem5 = mensagem5, mensagem6 = mensagem6, mensagem = mensagem )

if __name__ == "__main__":
    app.run(debug=True)