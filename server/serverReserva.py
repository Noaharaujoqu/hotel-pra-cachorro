from repository.repositoryReserva import reservaR

class reservaS:
    @staticmethod
    def reserva():
        
        reservas = reservaR.reserva()

        return reservas
    
    @staticmethod
    def reservaUser(id):

        reservas = reservaR.reservaUser(id)

        return reservas
    
    @staticmethod
    def cancelar(id):

        resultado = reservaR.cancelar(id)

        return resultado