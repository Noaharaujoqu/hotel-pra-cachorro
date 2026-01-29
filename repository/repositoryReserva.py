import psycopg2 as ps
import psycopg2.extras as pse
from config import Config

class reservaR:
    @staticmethod
    def reserva():
        
        con = ps.connect(host=Config.DB_HOST, database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWORD, port=Config.DB_PORT)

        cur = con.cursor(cursor_factory=pse.RealDictCursor)

        cur.execute("select * from disponibilidade")

        reservas = cur.fetchall()

        if not reservas:
            return False

        for r in reservas:
            r['vagas_disponiveis'] = r['vagas_total'] - r['vagas_ocupadas']

        return reservas
    
    @staticmethod
    def reservaUser(id):

        con = ps.connect(host=Config.DB_HOST, database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWORD, port=Config.DB_PORT)

        cur = con.cursor(cursor_factory=pse.RealDictCursor)

        cur.execute("select id, nomepet, raca, idade, data_reserva from reservas where usuario_id=%s", (id,))

        reservas = cur.fetchall()

        if not reservas:
            return False
        return reservas

    @staticmethod
    def cancelar(id):

        con = ps.connect(host=Config.DB_HOST, database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWORD, port=Config.DB_PORT)

        cur = con.cursor(cursor_factory=pse.RealDictCursor)
        cur.execute('select data_reserva from reservas where id=%s', (id,))

        reservas = cur.fetchone()
        data_reserva = reservas['data_reserva']

        cur.execute('update disponibilidade set vagas_ocupadas = vagas_ocupadas - 1 where data=%s', (data_reserva,))
        cur.execute('delete from reservas where id=%s', (id,))

        con.commit()
        
        return True
