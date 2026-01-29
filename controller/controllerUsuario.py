import flask as fl
import flask_jwt_extended as wt
from flask_jwt_extended import jwt_required
from server.serverUsuario import usuarioS
from server.serverReserva import reservaS

usuarioBp = fl.Blueprint('usuario', __name__)

# rotas get

@usuarioBp.route('/', methods=['GET'])
def index():
    return fl.render_template('index.html')

@usuarioBp.route('/loginGet', methods=['GET'])
def loginGet():
    return fl.render_template('login.html')

@usuarioBp.route('/cadastroGet', methods=['GET'])
def cadastroGet():
    return fl.render_template('cadastro.html')

@usuarioBp.route('/cadastroPost', methods=['POST'])
def cadastroPost():
    
    usuario = {
        "nome": fl.request.form.get('nome'),
        "email": fl.request.form.get('email'),
        "tel": fl.request.form.get('tel'),
        "senha": fl.request.form.get('senha')
    }

    usuarioS.cadastro(usuario)
    fl.flash(f'Cadastro de {usuario["nome"]} realizado!')
    return fl.redirect(fl.url_for('usuario.loginGet'))

@usuarioBp.route('/loginPost', methods=['POST'])
def loginPost():

    usuario = {
        "email": fl.request.form.get('email'),
        "senha": fl.request.form.get('senha')
    }
    logado = usuarioS.login(usuario)

    if not logado:
        return fl.render_template('login.html', msg='E-mail ou senhas incorretos')
    
    token = wt.create_access_token(identity=str(logado))

    print(logado)

    r = fl.redirect(fl.url_for('usuario.hotel'))
    wt.set_access_cookies(r, token)

    return r

@usuarioBp.route('/hotelGet', methods=['GET'])
@jwt_required()
def hotel():

    id = wt.get_jwt_identity()

    reservas = reservaS.reserva()
    reservasUser = reservaS.reservaUser(id)

    return fl.render_template('hotel.html', reservas=reservas, reservasUser=reservasUser)

@usuarioBp.route('/sairGet', methods=["GET"])
@jwt_required()
def sair():

    r = fl.redirect(fl.url_for('usuario.index'))
    wt.unset_jwt_cookies(r)

    return r

@usuarioBp.route('/reservaPost', methods=['POST'])
@jwt_required()
def reservaPost():

    id = wt.get_jwt_identity()

    cachorro = {
        "nomepet": fl.request.form.get('nomepet'),
        "raca": fl.request.form.get('raca'),
        "idade": fl.request.form.get('idade'),
        "datareserva": fl.request.form.get('datareserva'),
    }

    reserva = usuarioS.reserva(cachorro, id)

    if not reserva:
        fl.flash('Infelizmente não é possível fazer reserva nessa data.')
    else:
        fl.flash('Reserva feita com sucesso!')
    return fl.redirect(fl.url_for('usuario.hotel'))