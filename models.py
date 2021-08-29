from sqlalchemy import create_engine, Column, String, Integer,ForeignKey
# responsável por criar a sessão
from sqlalchemy.orm import scoped_session, sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

# criar banco
engine = create_engine('sqlite:///atividades.db', convert_unicode = True)
# criar sessão - para fazer Alterações e Consultas
# bind=engine - para saber qual banco vai abrir a sessão
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
# Default do Sqlalchemy
# Necessário p/criar banco dados e fazer alterações e consultas
Base = declarative_base()
Base.query = db_session.query_property()

# criar tabelas
class Pessoas(Base):
    __tablename__="pessoas"
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    # representação da classe
    # Quando mandar imprimir objeto vai imprimir o que estiver na função
    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

# representação da classe
    # Quando mandar imprimir objeto vai imprimir o que estiver na função
    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

