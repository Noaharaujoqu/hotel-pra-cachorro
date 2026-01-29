import uuid
import bcrypt

class usuarioM:
    def __init__(self, nome, email, tel, senha, id=None):
        self.id = id or str(uuid.uuid4())
        self.nome = nome
        self.email = email
        self.tel = tel
        self.senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')