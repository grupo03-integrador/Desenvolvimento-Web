#coding: utf-8
from flask import Blueprint, render_template, request, redirect
from mod_funcionario.funcionarioDB import Funcionario
#from mod_login.login import validaSessao

bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

# FormListaFuncionario
@bp_funcionario.route("/", methods=['GET', 'POST'])
#@validaSessao
def formListaFuncionarios():
    funcionario = Funcionario()
    res = funcionario.selectALL()
    return render_template('formListaFuncionarios.html', result=res, content_type='application/json')

# FormCadastroFuncionario
@bp_funcionario.route("/formCadastroFuncionario", methods=['POST'])
#@validaSessao
def formCadastroFuncionario():
    #cliente=Clientes()
    return render_template('formCadastroFuncionario.html', content_type='application/json')

#-----------------------------------------------------------------------------------------------------------------------

