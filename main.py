from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
login_entry = ""
senha_entry = ""
nome_usuario = ""
conf_senha = ""

def cadastrar():
	print("próximo passo")
	nome = nome_usuario.get()
	login_bdd = login_entry.get()
	senha_bdd = senha_entry.get()
	conf_senha_bd = conf_senha.get()
	if senha_bdd == conf_senha_bd:
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
		messagebox.showinfo(title=" ",message= "As senhas digitadas estão diferentes")
    
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
	if bd_s == (senha_bd[0][0]):
		messagebox.showinfo(title=" ",message= "validação completa")
		l_entry.delete(0, END)
		s_entry.delete(0, END)
	else:
		messagebox.showinfo(title=" ",message= "login ou senha incorretos")
 
#janela main
window = Tk()
window.title("Login")
window.geometry("290x350")


nb=ttk.Notebook(window)
nb.place(x=0, y=0, width=500, height=350)

tb1=Frame(nb)
nb.add(tb1,text="tela de login")
tb2=Frame(nb)
nb.add(tb2,text="tela de cadastro")

#descrição
topo = Label(tb1,text='LOGIN',font=('Arial 12'))
topo.place(x=30,y=30)
#entrada login
login = Label(tb1,text="Usuário")
login.place(x=30,y=90)
l_entry = Entry(tb1,text="",width=28)
l_entry.place(x=30,y=120)

#entrada senha
senha = Label(tb1,text="Senha")
senha.place(x=30,y=150)

s_entry = Entry(tb1,text="",show="*",width=28)
s_entry.place(x=30,y=180)
#botão login
button = Button(tb1,text="Logar",command=logar,width=25,height=2)
button.place(x=30,y=220)
#
#botão sair
button = Button(tb1,text="Sair",command=window.destroy,width=25,height=1)
button.place(x=30,y=268)
#-----------------------#
#------------------------#
top = Label(tb2,text='preencha os campos abaixo para cadastrar um novo usuário',font=('Arial 7'))
top.place(x=0,y=10)
	#-------------------------------------#
usuario = Label(tb2,text="Digite o seu nome")
usuario.place(x=30,y=41)
nome_usuario = Entry(tb2,text="",width=28)
nome_usuario.place(x=30,y=63)
#------------------------#
cadastro_login = Label(tb2,text="Digite o login que deseja cadastrar")
cadastro_login.place(x=30,y=90)
login_entry = Entry(tb2,text=" ",width=28)
login_entry.place(x=30,y=120)
	#-------‐-------------------------#
cadastro_senha = Label(tb2,text="Digite a senha que deseja cadastrar")
cadastro_senha.place(x=30,y=150)
senha_entry = Entry(tb2,text="",show="*",width=28)
senha_entry.place(x=30,y=180)
confirmacao_senha = Label(tb2,text="Confirme a senha")
confirmacao_senha.place(x=30,y=210)
conf_senha = Entry(tb2,text="",show="*",width=28)
conf_senha.place(x=30,y=240)
bt_cadastrar=Button(tb2,command=cadastrar,text='cadastrar',width=9,height=1)
bt_cadastrar.place(x=30,y=270)

window.mainloop()

	
