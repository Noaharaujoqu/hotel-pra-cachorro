from model.modelUsuario import usuarioM
from model.modelCachorro import cachorroM
from repository.repositoryUsuario import usuarioR

class usuarioS:
    @staticmethod
    def cadastro(usuario):

        usuarioC = usuarioM(**usuario)
        usuarioR.cadastro(usuarioC)
        return
    
    @staticmethod
    def login(usuario):

        logado = usuarioR.login(usuario)
        return logado
    
    @staticmethod
    def reserva(cachorro, id):
        
        cachorroC = cachorroM(**cachorro)
        reserva = usuarioR.reserva(cachorroC, id)
        return reserva