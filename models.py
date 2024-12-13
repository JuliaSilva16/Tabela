from sqlalchemy import *
from sqlalchemy.orm import *
engine = create_engine('sqlite:///Pessoas')
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String, index=True, nullable=False)

    def __repr__(self):
        return '<pessoa: {}, {}'.format(self.id, self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize(self):
        dados_pessoa = {
            'id': self.id,
            'nome': self.nome}

        return dados_pessoa

def init_db():
    Base.metadata.create_all(engine)
if __name__ == '__main__':
    init_db()