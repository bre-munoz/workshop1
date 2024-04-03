import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv(".env")

# Lê as variáveis de ambiente
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Cria a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def test_select_data():
    try:
        # Conecta ao banco de dados
        conn = psycopg2.connect(DATABASE_URL)

        # Verificar se o DataFrame não está vazio
        df = pd.read_sql('SELECT * FROM vendas', con=conn)
        assert not df.empty, "O DataFrame está vazio."

        # Verificar o schema (colunas e tipos de dados)
        expected_dtype = {
            'email': 'object',  # object em Pandas corresponde a string em SQL
            'data': 'datetime64[ns]',
            'valor': 'int64',
            'quantidade': 'int64',
            'produto': 'object',
            'categoria': 'object'
        }
        print(df.dtypes.to_dict())
        assert df.dtypes.to_dict(
        ) == expected_dtype, "O schema do DataFrame não corresponde ao esperado."

        print("Os dados foram criados com sucesso e o schema está correto.")

    except psycopg2.Error as e:
        print(f"Erro ao criar os dados ou verificar o schema: {e}")

    finally:
        # Fecha a conexão
        conn.close()
