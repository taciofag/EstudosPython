from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint

# Criar uma API Flask
app = Flask(__name__)

# Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'SSB1-Adm1n'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db:SQLAlchemy

#Definir a estrutura da tabela Postagem

#id_postagem, titulo, autor
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))
    # autor

class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

# Executar o comando para criar o banco de dados
with app.app_context():
    db.drop_all()
    db.create_all()

#Criar usuários administradores
    autor = Autor(nome='Tacio', email='tacio_frota@hotmail.com', senha='tac123io@', admin=True)
    db.session.add(autor)
    db.session.commit()


#Definir a estrutura da tabela Autor
