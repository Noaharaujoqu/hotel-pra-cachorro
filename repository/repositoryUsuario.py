import psycopg2 as ps
import psycopg2.extras as pse
import bcrypt
from model.modelUsuario import usuarioM
from model.modelCachorro import cachorroM
from config import Config

class usuarioR:
    @staticmethod
    def cadastro(usuario: usuarioM):

        con = ps.connect(host=Config.DB_HOST, database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWORD, port=Config.DB_PORT)

        cur = con.cursor()

        cur.execute("insert into usuarios (id, nome, email, telefone, senha) values (%s, %s, %s, %s, %s)", (usuario.id, usuario.nome, usuario.email, usuario.tel, usuario.senha))

        con.commit()

        return
    
    @staticmethod
    def login(usuario):

        con = ps.connect(host=Config.DB_HOST, database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWORD, port=Config.DB_PORT)

        cur = con.cursor(cursor_factory=pse.RealDictCursor)

        cur.execute("select id, senha from usuarios where email=%s", (usuario['email'],))

        logado = cur.fetchone()

        if not logado or not bcrypt.checkpw(usuario['senha'].encode("utf-8"), logado["senha"].encode("utf-8")):
            return False
        return logado['id']
    
    @staticmethod
    def reserva(cachorro: cachorroM, id):
        
        con = ps.connect(host=Config.DB_HOST, database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWORD, port=Config.DB_PORT)

        cur = con.cursor(cursor_factory=pse.RealDictCursor)

        cur.execute("select id, vagas_total, vagas_ocupadas from disponibilidade where data=%s", (cachorro.datareserva,))

        vagas = cur.fetchone()

        if vagas and vagas['vagas_total'] - vagas['vagas_ocupadas'] > 0:
            cur.execute("update disponibilidade set vagas_ocupadas = vagas_ocupadas + 1 where id=%s", (vagas['id'],))
        elif not vagas:
            cur.execute("insert into disponibilidade (data) values (%s)", (cachorro.datareserva,))
        else:
            return False
        
        cur.execute("insert into reservas (usuario_id, nomepet, raca, idade, data_reserva) values (%s, %s, %s, %s, %s)", (id, cachorro.nomepet, cachorro.raca, cachorro.idade, cachorro.datareserva))

        con.commit()

        return True


