from estudo import app
from flask import render_template, request

itens = ['carne', 'banana']

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        novo_item = request.form.get('item')
        if novo_item:
            itens.append(novo_item)
    
    if request.method == 'POST' and 'remover_item':
        item_remover = request.form.get('remover_item')
        if item_remover in itens:
            itens.remove(item_remover)

    return render_template('index.html', itens=itens)



@app.route('/segundapagina/')
def segundapagina():
    return render_template('segundapagina.html')


