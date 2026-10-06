from sqlalchemy import create_engine
import pandas as pd 
from dotenv import load_dotenv 
import os


# inicio do codigo
# carrega variaveis de ambiente 
load_dotenv()

def conecta_banco():

    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    # URL de conexao com o banco
    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}/{database}' 
    )

    return engine

# chama a funcao que conecta o banco
engine = conecta_banco()

try:
    df_usuarios = pd.read_sql('tb_usuarios', engine)
    print(df_usuarios)
    df_livros = pd.read_sql('tb_livros', engine)
    print(df_livros)
    df_itens_alugados = pd.read_sql('tb_itens_alugados', engine)
    print(df_itens_alugados)
    df_alugados = pd.read_sql('tb_alugados', engine)
    print(df_alugados)




except Exception as e: 
    print(f'erro ao conectar aos dados {e}')

# relacionando os dataframes com merge

try:
    df_merge1 = pd.merge(
        df_livros, df_itens_alugados, on = 'id_livro'
    )
    print(df_merge1)

    df_merge2 = pd.merge(
        df_merge1, df_alugados, on = 'id_aluguel'
    )
    print(df_merge2)

    df_dados = pd.merge(
        df_merge2, df_usuarios, on = 'id_usuario'
    )
    print(df_dados)

except Exception as e: 
    print(f'erro ao relacionar os dataframes {e}')