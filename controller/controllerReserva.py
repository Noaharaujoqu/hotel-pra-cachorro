import flask as fl
import flask_jwt_extended as wt
from flask_jwt_extended import jwt_required
from server.serverUsuario import usuarioS
from server.serverReserva import reservaS

reservaBp = fl.Blueprint('reserva', __name__)

@reservaBp.route('/cancelarPost', methods=["POST"])
@jwt_required()
def cancelarPost():
    
    id = fl.request.form.get('idreserva')
    resultado = reservaS.cancelar(id)

    if resultado:
        fl.flash('Reserva cancelada com sucesso!')
        return fl.redirect(fl.url_for('usuario.hotel'))