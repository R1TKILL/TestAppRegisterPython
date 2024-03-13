# Trabalhando com Banco de Dados.
import mysql.connector


def open_conexao(host, usuario, senha, banco):
    # Retorna a conexão.
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)


def close_conexao(con):
    return con.close()
