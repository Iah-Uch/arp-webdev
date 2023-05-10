from flask import Flask, request
from flask_restful import Api, Resource
from database import db, Paciente, Consulta

app = Flask(__name__)
api = Api(app)

# configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicialização do banco de dados
db.init_app(app)
with app.app_context():
    db.create_all()

class Pacientes(Resource):
    def get(self):
        # lista todos os pacientes
        pacientes = Paciente.query.all()
        return [{'id': p.id, 'nome': p.nome, 'cpf': p.cpf, 'telefone': p.telefone, 'email': p.email, 'data_nascimento': p.data_nascimento} for p in pacientes]

    def post(self):
        # cria um novo paciente
        data = request.get_json()
        paciente = Paciente(**data)
        db.session.add(paciente)
        db.session.commit()
        return {'id': paciente.id, 'nome': paciente.nome, 'cpf': paciente.cpf, 'telefone': paciente.telefone, 'email': paciente.email, 'data_nascimento': paciente.data_nascimento}, 201

class PacienteDetalhe(Resource):
    def get(self, id):
        # retorna os detalhes de um paciente específico
        paciente = Paciente.query.get_or_404(id)
        return {'id': paciente.id, 'nome': paciente.nome, 'cpf': paciente.cpf, 'telefone': paciente.telefone, 'email': paciente.email, 'data_nascimento': paciente.data_nascimento}, 200

class Consultas(Resource):
    def get(self):
        # lista todas as consultas
        consultas = Consulta.query.all()
        return [{'id': c.id, 'paciente_id': c.paciente_id, 'data_hora': c.data_hora} for c in consultas], 200

    def post(self):
        # cria uma nova consulta
        data = request.get_json()
        consulta = Consulta(**data)
        db.session.add(consulta)
        db.session.commit()
        return {'id': consulta.id, 'paciente_id': consulta.paciente_id, 'data_hora': consulta.data_hora}, 201

class ConsultaDetalhe(Resource):
    def get(self, id):
        # retorna os detalhes de uma consulta específica
        consulta = Consulta.query.get_or_404(id)
        return {'id': consulta.id, 'paciente_id': consulta.paciente_id, 'data_hora': consulta.data_hora}, 200

api.add_resource(Pacientes, '/pacientes')
api.add_resource(PacienteDetalhe, '/pacientes/<int:id>')
api.add_resource(Consultas, '/consultas')
api.add_resource(ConsultaDetalhe, '/consultas/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)