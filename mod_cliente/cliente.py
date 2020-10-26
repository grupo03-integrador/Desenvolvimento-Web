#coding: utf-8
from flask import Blueprint, render_template, request, redirect
from mod_cliente.clienteBD import Clientes
from mod_login.login import validaSessao

bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

#@bp_cliente.route("/", methods=['GET', 'POST'])
#def formListaClientes():
#   return render_template("formListaClientes.html")

#@bp_cliente.route("/formCliente", methods=['POST'])
#def formCliente():
#    return render_template("formCliente.html")

@bp_cliente.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaClientes():
    cliente = Clientes()
    res = cliente.selectALL()
    return render_template('formListaClientes.html', result=res, content_type='application/json')

@bp_cliente.route("/formCliente", methods=['POST'])
@validaSessao
def formCliente():
    cliente=Clientes()
    return render_template('formCliente.html', cliente=cliente, content_type='application/json')

@bp_cliente.route("/formEditCliente", methods=['POST'])
@validaSessao
def formEditCliente():
    cliente=Clientes()
    cliente.id_cliente = request.form['id_cliente']
    cliente.selectONE( )
    return render_template('formCliente.html', cliente=cliente, content_type='application/json')

@bp_cliente.route('/addCliente', methods=['POST'])
@validaSessao
def addCliente():
    cliente=Clientes()
    cliente.id_cliente = request.form['id_cliente']
    cliente.nome = request.form['nome']
    cliente.endereco = request.form['endereco']
    cliente.numero = request.form['numero']
    cliente.observacao = request.form['observacao']
    cliente.cep = request.form['cep']
    cliente.bairro = request.form['bairro']
    cliente.cidade = request.form['cidade']
    cliente.estado = request.form['estado']
    cliente.telefone = request.form['telefone']
    cliente.email = request.form['email']
    cliente.login = request.form['login']
    cliente.senha = request.form['senha']
    cliente.grupo = request.form['grupo']
        
    cliente.insert()
    return redirect('/cliente/')

@bp_cliente.route('/editCliente', methods=['POST'])
@validaSessao
def editCliente():
    cliente=Clientes()
    cliente.id_cliente = request.form['id_cliente']
    cliente.nome = request.form['nome']
    cliente.endereco = request.form['endereco']
    cliente.numero = request.form['numero']
    cliente.observacao = request.form['observacao']
    cliente.cep = request.form['cep']
    cliente.bairro = request.form['bairro']
    cliente.cidade = request.form['cidade']
    cliente.estado = request.form['estado']
    cliente.telefone = request.form['telefone']
    cliente.email = request.form['email']
    cliente.login = request.form['login']
    cliente.senha = request.form['senha']
    cliente.grupo = request.form['grupo']
        
    if 'salvaEditaUsuarioDB' in request.form:
        cliente.update()
    elif 'salvaExcluiUsuarioDB' in request.form:
        cliente.delete()
        
    return redirect('/cliente/')
