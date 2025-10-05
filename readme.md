Dio Bank App

Aplicação bancária desenvolvida em Python, estruturada com Domain-Driven Design (DDD) e princípios SOLID. O projeto visa simular operações bancárias básicas, como criação de contas, depósitos, saques e transferências, promovendo uma arquitetura limpa e escalável.

🚀 Tecnologias Utilizadas

Python 3.10+

FastApi como framework

Poetry para gerenciamento de dependências

Docker para containerização

Alembic para migração de banco de dados

pytest para testes automatizados



📂 Estrutura do Projeto

A estrutura do projeto segue os princípios do DDD, organizando o código em domínios específicos:


```text
alembic/                       # Scripts de migração do banco de dados

src/
├── app/
│   ├── auth/
│   │   ├── application/
│   │   │   ├── dtos/
│   │   │   │   ├── authenticate_user_input_dto.py
│   │   │   │   ├── authenticate_user_output_dto.py
│   │   │   │   └── register_user_input_dto.py
│   │   │   ├── expections/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth_exceptions.py
│   │   │   │   ├── password_exceptions.py
│   │   │   │   └── user_exceptions.py
│   │   │   └── use_cases/
│   │   │       ├── authenticate_user_use_case.py
│   │   │       └── register_user_use_case.py
│   │   ├── domain/
│   │   │   ├── entities/
│   │   │   │   └── user.py
│   │   │   ├── repositories/
│   │   │   │   └── user_repository.py
│   │   │   ├── services/
│   │   │   │   ├── hash_password_service.py
│   │   │   │   └── token_service.py
│   │   │   └── value_objects/
│   │   │       └── email.py
│   │   ├── infrastructure/
│   │   │   ├── orm/
│   │   │   │   └── repositories/
│   │   │   │       └── user_repository_sql_alchemy.py
│   │   │   └── services/
│   │   │       ├── hash_password_bcrypt_service.py
│   │   │       └── token_jwt_service.py
│   │   └── interfaces/
│   │       ├── controllers/
│   │       │   ├── authenticate_controller.py
│   │       │   └── register_user_controller.py
│   │       ├── factories/
│   │       │   ├── make_authenticate_user_use_case.py
│   │       │   └── make_register_user_usecase.py
│   │       ├── routes/
│   │       │   └── user.py
│   │       └── schemas/
│   │           ├── autheticate_schema.py
│   │           └── register_user_schema.py
│   ├── core_banking/
│   │   ├── __init__.py
│   │   ├── application/
│   │   │   ├── dto/
│   │   │   │   ├── get_account_balance_input_dto.py
│   │   │   │   ├── get_account_balance_output_dto.py
│   │   │   │   ├── open_account_input_dto.py
│   │   │   │   └── transfer_funds_input_dto.py
│   │   │   ├── expections/
│   │   │   │   ├── account_exceptions.py
│   │   │   │   ├── core_banking_error.py
│   │   │   │   ├── customer_exceptions.py
│   │   │   │   └── transactions_exceptions.py
│   │   │   └── use_cases/
│   │   │       ├── get_account_balance_use_case.py
│   │   │       ├── open_account_use_case.py
│   │   │       └── transfer_founds_use_case.py
│   │   ├── domain/
│   │   │   ├── entities/
│   │   │   │   ├── account.py
│   │   │   │   ├── customer.py
│   │   │   │   └── transaction.py
│   │   │   ├── repositories/
│   │   │   │   ├── account_repository.py
│   │   │   │   ├── customer_repository.py
│   │   │   │   └── transaction_repository.py
│   │   │   └── value_objects/
│   │   │       └── money.py
│   │   ├── infrastructure/
│   │   │   └── orm/
│   │   │       ├── models/
│   │   │       │   ├── account.py
│   │   │       │   └── transaction.py
│   │   │       └── repositories/
│   │   │           ├── account_repository_sqlalchemy.py
│   │   │           ├── customer_repository_sqlalchemy.py
│   │   │           └── transaction_repository_sqlalchemy.py
│   │   └── interfaces/
│   │       ├── controllers/
│   │       │   ├── get_account_balance_controller.py
│   │       │   ├── open_account_controller.py
│   │       │   └── transfer_accounts_funds_controller.py
│   │       ├── factories/
│   │       │   ├── make_get_account_balance_use_case.py
│   │       │   ├── make_open_accont_use_case.py
│   │       │   └── make_transfer_founds_use_case.py
│   │       ├── routes/
│   │       │   └── accounts.py
│   │       └── schemas/
│   │           ├── get_account_balance_schema.py
│   │           ├── open_account_schema.py
│   │           └── transfer_founds_schema.py
│   └── shared/
│       ├── __init__.py
│       ├── config/
│       │   ├── __init__.py
│       │   └── settings.py
│       ├── database/
│       │   ├── __init__.py
│       │   ├── database_config.py
│       │   └── models/
│       │       ├── __init__.py
│       │       └── user.py
│       ├── domain/
│       │   ├── base_entity.py
│       │   └── objects_values/
│       │       ├── cpf.py
│       │       └── unique_entity_id.py
│       ├── dto/
│       │   └── base_dto.py
│       ├── security/
│       │   ├── __init__.py
│       │   └── validation_token.py
│       └── validators/
│           ├── __init__.py
│           └── uuid_validator.py

└── main.py

tests/
├── __init__.py
├── conftest.py
├── e2e/
│   ├── auth/
│   │   ├── test_authenticate_user_e2e.py
│   │   └── test_register_user_e2e.py
│   └── core_banking/
│       ├── test_get_balance_account_e2e.py
│       ├── test_open_account_e2e.py
│       └── test_transfer_accounts_funds_e2e.py
├── factories/
│   └── use_cases/
│       ├── authenticat_user.py
│       ├── get_account_balance_use_case_factory.py
│       ├── open_account_use_case_factory.py
│       ├── register_use_case_factory.py
│       └── transfer_founds_use_case_fa

```

⚙️ Como Executar o Projeto
1. Clonar o Repositório
git clone https://github.com/paulorfsantos17/dio-bank-app.git
cd dio-bank-app

2. Instalar as Dependências
poetry install

3. Iniciar o banco de dados no docker
docker-compose up

4. Executar as Migrações do Banco de Dados
poetry run alembic upgrade head


5. Rodar a aplicação
poetry run uvicorn src.main:app --reload

6. Rodar os Testes Automatizados
```bash poetry run pytest ```

🧪 Testes

Os testes são organizados utilizando o framework pytest, abrangendo os principais cenários de operações bancárias. Para rodar os testes, utilize o comando:

poetry run pytest

