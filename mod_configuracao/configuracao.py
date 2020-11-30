#coding: utf-8
from flask import Blueprint, render_template, request

bp_configuracao = Blueprint('configuracao', __name__, url_prefix="/configuracao", template_folder='templates')

# FormConfiguracoes
@bp_configuracao.route("/", methods=['GET', 'POST'])
def formConfiguracao():
    return render_template("formConfiguracao.html") 

#---------------------------------------------------------------------------------------