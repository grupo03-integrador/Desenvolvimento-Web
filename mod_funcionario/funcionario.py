#coding: utf-8
from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from mod_login.login import validaSessao
from mod_funcionario.funcionarioDB import Funcionario

bp_funcionario = Blueprint('funcionario', __name__, url_prefix='/', template_folder='templates')

@bp_funcionario.route("/indexFunc", methods=['GET', 'POST'])
@validaSessao
def indexFunc():
         funcionario=Funcionario()
         res = funcionario.selectALL()
         return render_template('formListaFuncionarios.html', result=res, content_type='application/json')

@bp_funcionario.route("/formFuncionario", methods=['POST'])
@validaSessao
def formFuncionario():
         funcionario=Funcionario()
         return render_template('formCadastroFuncionario.html', funcionario=funcionario, content_type='application/json')

@bp_funcionario.route("/formEditFuncionario", methods=['POST'])
@validaSessao
def formEditFuncionario():
        funcionario=Funcionario()
        funcionario.id_funcionario = request.form['id_funcionario']
        funcionario.selectONE( )
        return render_template('formCadastroFuncionario.html', funcionario=funcionario, content_type='application/json')

@bp_funcionario.route('/addFuncionario', methods=['POST'])
@validaSessao
def addFuncionario():
        funcionario=Funcionario()
        funcionario.id_funcionario = request.form['id_funcionario']        
        funcionario.matricula = request.form['matricula']
        funcionario.grupo = request.form['grupo']
        funcionario.nome = request.form['nome']         
        funcionario.matricula = request.form['cpf']              
        funcionario.telefone = request.form['telefone']
        funcionario.senha = request.form['senha']
        funcionario.compra_fiado = request.form['compra_fiado'] 
        funcionario.data_pagamento = request.form['data_pagamento']       
        funcionario.insert()
        return redirect(url_for('funcionario.indexFunc'))


@bp_funcionario.route('/editFuncionario', methods=['POST'])
@validaSessao
def editFuncionario():
        funcionario=Funcionario()
        funcionario.id_funcionario = request.form['id_funcionario']        
        funcionario.matricula = request.form['matricula']
        funcionario.grupo = request.form['grupo']
        funcionario.nome = request.form['nome']         
        funcionario.matricula = request.form['cpf']              
        funcionario.telefone = request.form['telefone']
        funcionario.senha = request.form['senha']
        funcionario.compra_fiado = request.form['compra_fiado'] 
        funcionario.data_pagamento = request.form['data_pagamento']
        
        if 'salvaEditaFuncionarioDB' in request.form:
            funcionario.update()
        elif 'salvaExcluiFuncionariooDB' in request.form:   
            funcionario.delete()

        return redirect(url_for('funcionario.indexFunc'))
        
@bp_funcionario.route("/funcionarioLista")
@validaSessao
def listaFuncionario():
    return render_template('formListaFuncionarios.html')


@bp_funcionario.route('/verificaSeLoginExiste', methods = ['POST'])
@validaSessao
def verificaSeLoginExiste():
        funcionario = Funcionario       ()
        funcionario.login = request.form['login']
        try:
                result = cliente.verificaSeLoginExiste()
                #Verifica se achou o login no banco
                if len(result) > 0:
                          return jsonify(login_existe = True)
                else:
                         return jsonify(login_existe = False)
        except Exception as e:
                return jsonify(erro = True, mensagem_exception = str(e))