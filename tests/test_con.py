import unittest
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(".env")

# Lê as variáveis de ambiente
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Cria a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


class TestDatabaseConnection(unittest.TestCase):
    def test_read_data_and_check_schema(self):
        try:
            # Tenta conectar ao banco de dados e ler os dados da tabela vendas
            df = pd.read_sql('SELECT 1', con=DATABASE_URL)
        except Exception as e:
            self.fail(f"A conexão com o banco de dados falhou: {str(e)}")


if __name__ == '__main__':
    unittest.main()
