from flask import Flask
from flask import render_template
import datetime
from flask import request
from flask import flash
import os
from flask import session
from flask import redirect
from flask import url_for
from config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.secret_key = 'hola'

    class User:
        def __init__(self, username, password):
            self.username = username
            self.password = password
        
        def validacion_password(self, password):
            return self.password == password
        
    usuario = User('mario', '123')
    listaDeUsuarios = {usuario.username:usuario}

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
        
            user = listaDeUsuarios.get(username, None)
            if user and usuario.validacion_password(password):
                message = 'Bienvenido {}'.format(username)
                flash(message, 'success')
                session['user'] = username
                return redirect(url_for('dashboard'))
            else:
                flash('Ususario o password Invalidos', 'danger')
                return render_template('login.html')
        else:
            return render_template('login.html')

    @app.route('/dashboard')
    def dashboard():
        username = session['user']
        return render_template('dashboard.html', username=username)

    @app.route('/logout')
    def logout():
        session.pop('user')
        return redirect(url_for('login'))


    return app

"""
@aplicacion.route("/parametros")
def parametros():
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    print (username)
    print (password)
    return render_template('login.html')

@aplicacion.route("/post", methods=['POST'])    
def post():
    
    username = request.form.get('username')
    password = request.form.get('password')
    print(username," ", password)
    
    return render_template('login.html')
    """

