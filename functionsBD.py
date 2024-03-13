from tkinter import messagebox
from AppRegister.conectionBD import open_conexao, close_conexao
from AppRegister.Frames import *

#Para inserir um usuario.
def inserir_usuario(email, senha):
    con = open_conexao("localhost", "root", "Admin1str@tor", "pycliente")
    cursor = con.cursor() #É o responsavel por fazer a conexão com o banco.
    sql = "INSERT INTO clientes (email, senha) values (%s, %s)"#inserindo os valores.
    valores = (email, senha)
    if email == "" and senha == "":
        messagebox.showwarning("Perigo", "Você não pode salvar um usuário nulo.")
    else:
        cursor.execute(sql, valores) #Executando a conexão com os valores definidos.
        cursor.close()
        con.commit() #Para REALMENTE executar e salvar.
        messagebox.showinfo("Seja muito bem vindo!!!", "Você foi cadastrado com sucesso.")

'''
def exibir_usuarios(con):
    cursor = con.cursor() #quem recebe o cursor fica responsavel por executar os comandos do SQL
    sql = "SELECT id, email, senha FROM clientes"
    cursor.execute(sql)
    #para exibir de fato os valores.
    print("\nConexões Salva no Banco pycliente\n")
    for (id, email, senha) in cursor:
        print("ID = "+str(id)+" Email = "+str(email)+" Password = "+str(senha)+"\n")
'''


'''
def exibir_um_usuario(con, referencia):
    cursor = con.cursor()
    sql = "SELECT id, email, senha FROM clientes where id = (%s)"
    cursor.execute(sql, referencia)
    print("\nCliente Salvo no Banco pycliente\n")
    for (id, email, senha) in cursor:
        print("ID = "+str(id)+" Email = "+str(email)+" Password = "+str(senha)+"\n")
'''

def atualiza_usuario(email, senha, verificador):
    con = open_conexao("localhost", "root", "Admin1str@tor", "pycliente")
    cursor = con.cursor()
    sql = "UPDATE clientes SET senha = (%s) WHERE email = (%s)"
    valores = (senha, email)
    if email == "" and senha == "":
        messagebox.showwarning("Perigo", "Você não pode salvar um usuário nulo.")
    elif senha != verificador:
        messagebox.showwarning("Ops", "As senhas não são iguais senha .")
    else:
        cursor.execute(sql, valores)
        cursor.close()
        con.commit()
        messagebox.showinfo("Conseguimos!", "Você alterou sua senha com sucesso.")



