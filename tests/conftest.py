import psycopg2
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from alembic import command
from alembic.config import Config
from src.app.shared.config.settings import settings

# -------------------------
# Configurações do banco
# -------------------------
DB_NAME = "dio_bank_test"
DB_USER = "docker"
DB_PASS = "docker"
DB_HOST = "localhost"
DB_PORT = 5432

# Define a URL do banco de teste antes de importar qualquer coisa
settings.database_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"



@pytest_asyncio.fixture
async def db():
    # --- Conecta no banco "postgres" para criar o banco de teste ---
    conn = psycopg2.connect(
        dbname="postgres", user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    # Cria o banco se não existir
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}';")
    if not cur.fetchone():
        cur.execute(f"CREATE DATABASE {DB_NAME};")
        print(f"Banco {DB_NAME} criado.")

    cur.close()
    conn.close()
    
    from src.app.shared.database.database_config import database

    await database.connect()
    
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

    yield  # 👈 Aguarda o teste

    await database.disconnect()
    
    conn = psycopg2.connect(
        dbname="postgres", user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
    print(f"Banco {DB_NAME} removido.")
    cur.close()
    conn.close()



@pytest_asyncio.fixture
async def client(db):
    from src.main import app

    transport = ASGITransport(app=app)  # corrigido nome
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    async with AsyncClient(base_url="https://test", transport=transport, headers=headers) as client:
        yield client

@pytest_asyncio.fixture
async def access_token(client: AsyncClient):
    payload = {
        "name": "Ana Clara Souza",
        "email": "ana.clara.souza@test.com",
        "password": "Teste1234",
        "cpf": "168.995.350-09"
    }

    await client.post("/register", json=payload)
    response = await client.post("/auth", json={"cpf": payload["cpf"], "password": payload["password"]})
    return response.json()["access_token"]