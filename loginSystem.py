import pymysql
from tkinter import *

conn = pymysql.connect(host="localhost",user="root",password="root123",db="foodmenu")
curs = conn.cursor()

class LoginPage():
	def __init__(self, master,shop):
		self.master = master
		self.shop = shop
		master.label_username = Label(master, text="Username")
		master.entry_username = Entry(master)
		master.label_username.grid(row=0,column=0,sticky=E)
		master.entry_username.grid(row=0,column=1)
		
		master.label_password = Label(master, text="Password")
		master.entry_password = Entry(master)
		master.label_password.grid(row=1,column=0,sticky=E)
		master.entry_password.grid(row=1,column=1)
		
		login_button = Button(master,text="Login",command=lambda:self.validate(master.entry_username.get(),master.entry_password.get()))
		login_button.grid(columnspan=2)
		
		label_register = Label(master,text="New User?click here to login")
		register_button = Button(master,text="Register",command=self.register)
		register_button.grid(columnspan=2)
	
	def validate(self,username,passwordB):
		sqlQuery = "SELECT password FROM login_details WHERE username="+repr(username)
		curs.execute(sqlQuery)
		passwordA = curs.fetchone()
		sqlQuery = "SELECT shopname FROM login_details WHERE username="+repr(username)
		curs.execute(sqlQuery)
		shopname = curs.fetchone()
		if not passwordA:
			print("Invalid Username")
		elif passwordA[0] != passwordB:
			print("Invalid Password")
		else:
			print("Login Successful")
			self.shop.name = shopname[0]
			conn.close()
			self.master.destroy()
			self.shop.enter()
	
	def reg(self):
		username = self.master.entry_username.get()
		shopname = self.master.entry_shopname.get()
		password = self.master.entry_password.get()
		sqlQuery = "INSERT INTO login_details VALUES("+repr(username)+", "+repr(shopname)+", "+repr(password)+")"
		try:
			curs.execute(sqlQuery)
			shopname = shopname.replace(" ","_")
			sqlQuery = "CREATE TABLE "+shopname+"_menu(food varchar(20) primary key, price REAL, rank INTEGER)"
			curs.execute(sqlQuery)
			conn.commit()
			self.shop.name = shopname
			print("Registration Successful")
			conn.close()
			self.master.destroy()
			self.shop.enter()
		except:
			print("user already exists")

	def register(self):		
		for widget in self.master.winfo_children():
			widget.destroy()
		self.master.label_username = Label(self.master, text="Username")
		self.master.entry_username = Entry(self.master)
		self.master.label_username.grid(row=0,column=0,sticky=E)
		self.master.entry_username.grid(row=0,column=1)
		
		self.master.label_shopname = Label(self.master, text="Shopname")
		self.master.entry_shopname = Entry(self.master)
		self.master.label_shopname.grid(row=1,column=0,sticky=E)
		self.master.entry_shopname.grid(row=1,column=1)
		
		self.master.label_password = Label(self.master, text="Password")
		self.master.entry_password = Entry(self.master)
		self.master.label_password.grid(row=2,column=0,sticky=E)
		self.master.entry_password.grid(row=2,column=1)
		
		register_button = Button(self.master,text="register",command=self.reg)
		register_button.grid(columnspan=2)
		