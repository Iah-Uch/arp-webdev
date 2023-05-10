# API Flask de cadastro de pacientes e agendamento de consultas

Esta é uma API Flask simples para cadastro de pacientes e agendamento de consultas. A API permite que o usuário crie, liste e obtenha detalhes de pacientes e consultas.

## Instalação

Para rodar a aplicação, é necessário ter Python 3 instalado. Clone o repositório e instale as dependências:

```bash
git clone https://github.com/Iah-Uch/arp-webdev.git
cd arp
pip install -r requirements.txt
```

## Configuração

A aplicação utiliza o SQLite como banco de dados. Para criar o banco de dados e adicionar algumas informações iniciais, execute os seguintes comandos:

```bash
flask shell
from app import db
db.create_all()
exit()
```

## Uso

Para executar a aplicação, execute o seguinte comando:

```bash
python app.py
```

A API estará disponível em `http://localhost:5000`. A partir daí, você pode utilizar um cliente HTTP, como o Postman, para testar as rotas da API.

### Rotas

A API possui as seguintes rotas:

#### Pacientes

- `GET /pacientes`: retorna uma lista com todos os pacientes cadastrados.
- `GET /pacientes/<int:id>`: retorna os detalhes de um paciente específico.
- `POST /pacientes`: cria um novo paciente.

Os dados devem ser enviados no corpo da requisição no formato JSON, como no exemplo abaixo:

```json
{
    "nome": "João Silva",
    "data_nascimento": "1980-01-01",
    "cpf": "111.111.111-11",
    "telefone": "(11) 1111-1111",
    "endereco": "Rua A, 123"
}
```

#### Consultas

- `GET /consultas`: retorna uma lista com todas as consultas agendadas.
- `GET /consultas/<int:id>`: retorna os detalhes de uma consulta específica.
- `POST /consultas`: agenda uma nova consulta.

Os dados devem ser enviados no corpo da requisição no formato JSON, como no exemplo abaixo:

```json
{
    "paciente_id": 1,
    "data_hora": "2023-05-16T14:00:00"
}
```