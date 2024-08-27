from . import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_turma = db.Column(db.Integer, unique=True, nullable=False)

    alunos = db.relationship('Aluno', backref='turma', lazy=True)

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_disciplina = db.Column(db.String(64), unique=True, nullable=False)

    professores = db.relationship('Professor', backref='disciplina', lazy=True)

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_funcionario = db.Column(db.String(64), unique=True, nullable=False)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_aluno = db.Column(db.String(64), unique=True, nullable=False)
    
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

    notas = db.relationship('Nota', backref='aluno', lazy=True)

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_professor = db.Column(db.String(64), unique=True, nullable=False)
    
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor_nota = db.Column(db.Float, nullable=False)
    
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
