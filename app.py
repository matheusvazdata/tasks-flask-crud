from flask import Flask

app = Flask(__name__) # __name__ é uma variável que o Python cria automaticamente e que é igual ao nome do módulo em que está sendo usado, como __main__

# Criando uma rota
@app.route('/')
def hello_world():
    return 'Hello, World!' # Retorna uma string

# Criando outra rota (sobre)
@app.route('/about')
def about():
    return 'Página "sobre" da aplicação'

# Rodando a aplicação
if __name__ == '__main__': # Apenas executa o código abaixo se o módulo for executado manualmente, não se for importado
    app.run(debug=True) # debug=True é um argumento que permite que a aplicação seja recarregada automaticamente sempre que houver uma alteração no código