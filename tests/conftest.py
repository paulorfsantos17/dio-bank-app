import psycopg2
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, make_url
from sqlalchemy.orm import sessionmaker

from alembic import command
from alembic.config import Config
from src.app.shared.config.settings import settings
from src.app.shared.database.database_config import Base
from src.main import app

engine = create_engine(settings.database_url_test)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

url = make_url(settings.database_url_test)

DB_USER = url.username
DB_PASSWORD = url.password
DB_HOST = url.host
DB_PORT = url.port
DB_NAME_TEST = url.database


def create_test_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {DB_NAME_TEST} WITH (FORCE);")
    cur.execute(f"CREATE DATABASE {DB_NAME_TEST} OWNER {DB_USER};")
    cur.close()
    conn.close()
    
    test_conn = psycopg2.connect(
        dbname=DB_NAME_TEST,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    test_conn.autocommit = True
    test_cur = test_conn.cursor()
    test_cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    test_cur.close()
    test_conn.close()


def drop_test_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {DB_NAME_TEST} WITH (FORCE);")
    cur.close()
    conn.close()





@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    
    create_test_database()

    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", settings.database_url_test)

    # Roda todas as migrations
    command.upgrade(alembic_cfg, "head")

    yield  # ⚡ os testes rodam aqui
    breakpoint()

    # Opcional: dropar todas as tabelas ao final da sessão de teste
    drop_test_database()


@pytest.fixture()
def db_session():
    session = TestingSessionLocal()
    yield session
    session.rollback()
    session.close()


@pytest.fixture()
def client(db_session):

    with TestClient(app) as c:
        yield c
