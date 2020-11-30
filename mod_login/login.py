#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps

bp_login = Blueprint('login', __name__, url_prefix="/", template_folder='templates')

@bp_login.route("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")

@bp_login.route("/login", methods=['POST'])
def validaLogin():
    _name = request.form['usuario']
    _pass = request.form['senha']

    if _name == "grupo03" and _pass == "abcbolinhas":
        # abre a aplicação na tela home
        session.clear()
        session['usuario'] = _name
        return redirect(url_for('home.home'))
    else:
        # retorna para a tela de login
        return redirect(url_for('login.login', falhaLogin=1))



@bp_login.route("/loginoff", methods=['POST'])
def logoff():
    session.pop('usuario',None)
    session.clear()
    return redirect(url_for('login.login'))

# valida se o usuário esta ativo na sessão
def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            #descarta os dados copiados da função original e retorna a tela de login
            return redirect(url_for('login.login',falhaSessao=1))
        else:
            #retorna os dados copiados da função original
            return f(*args, **kwargs)

    #retorna o resultado do if acima
    return decorated_function