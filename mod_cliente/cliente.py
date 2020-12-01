#coding: utf-8
from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from mod_login.login import validaSessao
from mod_cliente.clienteDB import Clientes

bp_cliente = Blueprint('cliente', __name__, url_prefix='/', template_folder='templates')

@bp_cliente.route("/index", methods=['GET', 'POST'])
@validaSessao
def index():
         cliente=Clientes()
         res = cliente.selectALL()
         return render_template('formListaClientes.html', result=res, content_type='application/json')

@bp_cliente.route("/formCliente", methods=['POST'])
@validaSessao
def formCliente():
         cliente=Clientes()
         return render_template('formCadastroCliente.html', cliente=cliente, content_type='application/json')

@bp_cliente.route("/formEditCliente", methods=['POST'])
@validaSessao
def formEditCliente():
        cliente=Clientes()
        cliente.id_cliente = request.form['id_cliente']
        cliente.selectONE( )
        return render_template('formCadastroCliente.html', cliente=cliente, content_type='application/json')

@bp_cliente.route('/addCliente', methods=['POST'])
@validaSessao
def addCliente():
        cliente=Clientes()
        cliente.id_cliente = request.form['id_cliente']
        cliente.nome = request.form['nome']
        cliente.cpf = request.form['cpf']
        cliente.data_pagamento = request.form['data_pagamento']               
        cliente.telefone = request.form['telefone']
        cliente.senha = request.form['senha']
        cliente.compra_fiado = request.form['compra_fiado']        
        cliente.insert()
        return redirect(url_for('cliente.index'))


@bp_cliente.route('/editCliente', methods=['POST'])
@validaSessao
def editCliente():
        cliente=Clientes()
        cliente.id_cliente = request.form['id_cliente']
        cliente.nome = request.form['nome']
        cliente.cpf = request.form['cpf']
        cliente.data_pagamento = request.form['data_pagamento']                
        cliente.telefone = request.form['telefone']
        cliente.senha = request.form['senha']
        cliente.compra_fiado = request.form['compra_fiado']
        
        if 'salvaEditaUsuarioDB' in request.form:
            cliente.update()
        elif 'salvaExcluiUsuarioDB' in request.form:   
            cliente.delete()

        return redirect(url_for('cliente.index'))
        
@bp_cliente.route("/clienteLista")
@validaSessao
def listaCliente():
    return render_template('formListaClientes.html')


@bp_cliente.route('/verificaSeLoginExiste', methods = ['POST'])
@validaSessao
def verificaSeLoginExiste():
        cliente = Clientes()
        cliente.login = request.form['login']
        try:
                result = cliente.verificaSeLoginExiste()
                #Verifica se achou o login no banco
                if len(result) > 0:
                          return jsonify(login_existe = True)
                else:
                         return jsonify(login_existe = False)
        except Exception as e:
                return jsonify(erro = True, mensagem_exception = str(e))