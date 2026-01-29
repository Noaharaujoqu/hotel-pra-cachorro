import flask as fl
import flask_jwt_extended as wt
from controller.controllerUsuario import usuarioBp
from controller.controllerReserva import reservaBp
from config import Config
import os

app = fl.Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = 'cookies'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
jwt = wt.JWTManager(app)

app.register_blueprint(usuarioBp)
app.register_blueprint(reservaBp)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', debug=False, port=port)