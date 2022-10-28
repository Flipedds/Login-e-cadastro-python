from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
login_entry = ""
senha_entry = ""
nome_usuario = ""
conf_senha = ""

def cadastrar():
	
	nome = nome_usuario.get()
	login_bdd = login_entry.get()
	senha_bdd = senha_entry.get()
	conf_senha_bd = conf_senha.get()
	if senha_bdd == conf_senha_bd and login_bdd != "" and senha_bdd != "":
		try:
			banco = sqlite3.connect('banco.db')
			cursor = banco.cursor()
			cursor.execute("CREATE TABLE IF NOT EXISTS cadastro(nome text,login text,senha text)")
			cursor.execute("INSERT INTO cadastro VALUES('"+nome+"','"+login_bdd+"','"+senha_bdd+"')")
			banco.commit()
			banco.close()
			messagebox.showinfo(title=" ",message= "cadastro efetuado com sucesso")
			login_entry.delete(0, END)
			senha_entry.delete(0, END)
			nome_usuario.delete(0, END)
			conf_senha.delete(0, END)
		except sqlite3.Error as erro:
			print("Erro ao inserir os dados:",erro)
	else:
		if login_bdd == "" and senha_bdd == "":
			messagebox.showinfo(title=" ",message="Senha ou login com campos vazios")    
def logar():
	bd_l = l_entry.get()
	bd_s = s_entry.get()
	banco = sqlite3.connect('banco.db')
	cursor = banco.cursor()
	try:
		cursor.execute("SELECT senha FROM cadastro WHERE login ='{}'".format(bd_l))
		senha_bd = cursor.fetchall()
		banco.close()
	except:
		messagebox.showinfo(title=" ",message= "login ou senha incorretos")
	try:
		if bd_s == (senha_bd[0][0]) and bd_l != "":
			messagebox.showinfo(title=" ",message= "validação completa")
			l_entry.delete(0, END)
			s_entry.delete(0, END)
		else:
			messagebox.showinfo(title=" ",message= "login ou senha incorretos") 
	except:
		messagebox.showinfo(title=" ",message= "login ou senha incorretos")
		l_entry.delete(0, END)
		s_entry.delete(0, END)
#janela main
def modo_dark():
				tela_login.configure(bg="black")
				tela_cadastro.configure(bg="black")

window = Tk()
window.title("Login")
window.geometry("290x350")

nb=ttk.Notebook(window)
nb.place(x=0, y=0, width=500, height=350)

tela_login=Frame(nb)
nb.add(tela_login,text="tela de login")
tela_login.configure(bg="white")
tela_cadastro=Frame(nb)
tela_cadastro.configure(bg="white")
nb.add(tela_cadastro,text="tela de cadastro")

#descrição
topo = Label(tela_login,text='LOGIN',font=('Arial 12'))
topo.place(x=30,y=30)
#entrada login
login = Label(tela_login,text="Usuário")
login.place(x=30,y=90)
l_entry = Entry(tela_login,text="",width=28)
l_entry.place(x=30,y=120)

#entrada senha
senha = Label(tela_login,text="Senha")
senha.place(x=30,y=150)

s_entry = Entry(tela_login,text="",show="*",width=28)
s_entry.place(x=30,y=180)
#botão login
button = Button(tela_login,text="Logar",command=logar,width=25,height=2)
button.place(x=30,y=220)
#
#botão sair
button = Button(tela_login,text="Sair",command=window.destroy,width=25,height=1)
button.place(x=30,y=268)
#-----------------------#
#------------------------#
top = Label(tela_cadastro,text='preencha os campos abaixo para cadastrar um novo usuário',font=('Arial 7'))
top.place(x=0,y=10)
	#-------------------------------------#
usuario = Label(tela_cadastro,text="Digite o seu nome")
usuario.place(x=30,y=41)
nome_usuario = Entry(tela_cadastro,text="",width=28)
nome_usuario.place(x=30,y=63)
#------------------------#
cadastro_login = Label(tela_cadastro,text="Digite o login que deseja cadastrar")
cadastro_login.place(x=30,y=90)
login_entry = Entry(tela_cadastro,text=" ",width=28)
login_entry.place(x=30,y=120)
	#-------‐-------------------------#
cadastro_senha = Label(tela_cadastro,text="Digite a senha que deseja cadastrar")
cadastro_senha.place(x=30,y=150)
senha_entry = Entry(tela_cadastro,text="",show="*",width=28)
senha_entry.place(x=30,y=180)
confirmacao_senha = Label(tela_cadastro,text="Confirme a senha")
confirmacao_senha.place(x=30,y=210)
conf_senha = Entry(tela_cadastro,text="",show="*",width=28)
conf_senha.place(x=30,y=240)
bt_cadastrar=Button(tela_cadastro,command=cadastrar,text='cadastrar',width=9,height=1)
bt_cadastrar.place(x=30,y=270)

botao_dark_white=Button(tela_login,command=modo_dark,text="🌒",width=4,height=1)
botao_dark_white.place(x=195,y=30)

window.mainloop()

	
