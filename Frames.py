from tkinter import *
from tkinter import messagebox
from AppRegister.functionsBD import *
from AppRegister.conectionBD import *


def voltar_Login():
    second_frame.place_forget()
    third_frame.place_forget()
    newAccount_frame.place_forget()
    forgotPassword_frame.place_forget()
    first_frame.place(width=800, height=500, cursor=frameLogin())


def verifica_usuarios(email_login, password_login):
    con = open_conexao("localhost", "root", "Admin1str@tor", "pycliente")
    cursor = con.cursor()
    sql = "SELECT email, senha FROM clientes"
    cursor.execute(sql)
    for (email, senha) in cursor:
        if email_login == email and password_login == senha:
            frameMenu()
        elif email_login == "" and password_login == "":
            messagebox.showwarning("Perigo", "Você esta passando um usuário nulo.")
        elif email_login == "ADMIN" and password_login == "0000":
            first_frame.place_forget()
            second_frame.place_forget()
            frameAdmin()
        else:
           messagebox.showerror("Algo de errado aconteceu!", "Usuário ou senha estão incorretos")
    close_conexao(con)


def newAccount():
    first_frame.place_forget()
    second_frame.place_forget()
    third_frame.place_forget()
    forgotPassword_frame.place_forget()
    newAccount_frame.place(width=800, height=500)

    btnVoltar = Button(newAccount_frame, width=7, height=1, text="Voltar")
    btnVoltar.configure(font=("Arial, bold", 12), highlightbackground="Black", highlightthickness=3, bd=3,
            foreground="Black", command=voltar_Login)
    btnVoltar.place(x=30, y=30)

    lb_cadastro = Label(newAccount_frame, background="light blue", font=("Arial", 28), text="Cadastre-se\ne aproveite o nosso app")
    lb_cadastro.place(x=197, y=40)

    lb1 = Label(newAccount_frame, background="light blue", font=("Arial", 23), text="Insira seu Email:")
    lb1.place(x=90, y=185)
    create_user = Entry(newAccount_frame)
    create_user.place(x=330, y=187, width=250, height=35)

    lb2 = Label(newAccount_frame, background="light blue", font=("Arial", 23), text="Crie uma senha:")
    lb2.place(x=90, y=295)
    create_pass = Entry(newAccount_frame, show="*")
    create_pass.place(x=330, y=297, width=250, height=35)

    btnCadastro = Button(newAccount_frame, width=12, height=2, command=lambda: inserir_usuario(create_user.get(), create_pass.get()))
    btnCadastro.configure(font=("Arial", 16), highlightbackground="Black", highlightthickness=3, bd=3, text="Cadastrar-se")
    btnCadastro.place(x=290, y=380)

def forgotPassword():
    first_frame.place_forget()
    second_frame.place_forget()
    third_frame.place_forget()
    newAccount_frame.place_forget()
    forgotPassword_frame.place(width=800, height=500)

    btnVoltar = Button(forgotPassword_frame, width=7, height=1)
    btnVoltar.configure(font=("Arial, bold", 12), highlightbackground="Black", highlightthickness=3, bd=3,
                        text="Voltar", foreground="Black", command=voltar_Login)
    btnVoltar.place(x=30, y=30)

    lb_ajuda = Label(forgotPassword_frame, background="light blue", font=("Ubuntu, BOLD", 20),
                        text="Iremos lhe ajudar\nsiga os passos para recuperar seu acesso")
    lb_ajuda.place(x=137, y=50)

    lb1 = Label(forgotPassword_frame, background="light blue", font=("Arial", 23), text="1 - Informe o seu Email:")
    lb1.place(x=90, y=155)
    insert1 = Entry(forgotPassword_frame)
    insert1.place(x=450, y=157, width=250, height=35)

    lb2 = Label(forgotPassword_frame, background="light blue", font=("Arial", 23), text="2 - Crie uma nova senha:")
    lb2.place(x=90, y=225)
    insert2 = Entry(forgotPassword_frame, show="*")
    insert2.place(x=450, y=227, width=250, height=35)

    lb3 = Label(forgotPassword_frame, background="light blue", font=("Arial", 23), text="3 - repite sua nova senha:")
    lb3.place(x=90, y=295)
    insert3 = Entry(forgotPassword_frame, show="*")
    insert3.place(x=450, y=297, width=250, height=35)

    btnAterar = Button(forgotPassword_frame, width=12, height=2, command=lambda: atualiza_usuario(insert1.get(), insert2.get(), insert3.get()))
    btnAterar.configure(font=("Arial", 16), highlightbackground="Black", highlightthickness=3, bd=3, text="Alterar senha")
    btnAterar.place(x=290, y=380)


def frameMenu():
    first_frame.place_forget()
    third_frame.place_forget()
    newAccount_frame.place_forget()
    forgotPassword_frame.place_forget()
    second_frame.place(width=800, height=500)

    btnVoltar = Button(second_frame, width=7, height=1, text="Voltar")
    btnVoltar.configure(font=("Arial, bold", 12), highlightbackground="Black", highlightthickness=3, bd=3,
            foreground="Black", command=voltar_Login)
    btnVoltar.place(x=30, y=30)

    frase = Label(second_frame, font=("Ubuntu", 35), text="OI")
    frase.configure(background="light green")
    frase.place(x=300, y=25)


def frameAdmin():
    first_frame.place_forget()
    second_frame.place_forget()
    newAccount_frame.place_forget()
    forgotPassword_frame.place_forget()
    third_frame.place(width=800, height=500)


def frameLogin():
    frase = Label(first_frame, font=("Ubuntu", 35), text="Welcome")
    frase.configure(background="light blue")
    frase.place(x=300, y=25)

    lb_name = Label(first_frame, font=("Arial", 23), text="Email:")
    lb_name.configure(background="light blue")
    lb_name.place(x=200, y=140)
    insert_email = Entry(first_frame)
    insert_email.place(x=350, y=145, width=250, height=35)

    lb_pass = Label(first_frame, font=("Arial", 23), text="Password:")
    lb_pass.configure(background="light blue")
    lb_pass.place(x=200, y=240)
    insert_pass = Entry(first_frame, show="*")
    insert_pass.place(x=350, y=245, width=250, height=35)

    btnLogin = Button(first_frame, width=14, height=2,
                      command=lambda: verifica_usuarios(insert_email.get(), insert_pass.get()))
    btnLogin.configure(font=("Arial", 16), highlightbackground="Black", highlightthickness=3, bd=3, text="Login")
    btnLogin.place(x=310, y=330)

    btn_new_account = Button(first_frame, font=("Arial", 15), text="Register new account", command=newAccount)
    btn_new_account.configure(background="light blue", foreground="blue", border=0, bd=0,
                              highlightbackground="light blue", activebackground="light blue", activeforeground="red")
    btn_new_account.place(x=100, y=440)

    btn_new_account = Button(first_frame, font=("Arial", 15), text="I forgot my Password", command=forgotPassword)
    btn_new_account.configure(background="light blue", foreground="blue", border=0, bd=0,
                              highlightbackground="light blue", activebackground="light blue", activeforeground="red")
    btn_new_account.place(x=500, y=440)

# Janela Principal.
window = Tk()
window.title("Register")
window.geometry("800x500+270+100")
window.resizable(width=False, height=False)

# Frames da Janela.
first_frame = Frame(window, background="light blue")
first_frame.place(width=800, height=500, cursor=frameLogin())

second_frame = Frame(window, background="light blue")
third_frame = Frame(window, background="light blue")
newAccount_frame = Frame(window, background="light blue")
forgotPassword_frame = Frame(window, background="light blue")
window.mainloop()
