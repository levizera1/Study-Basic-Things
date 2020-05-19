import sqlite3 

MASTER_PASSWORD = "12345"

senha = input("insira a MASTER PASSWORD: ")

if senha != MASTER_PASSWORD: 
	print("Senha Invalida. Encerrando . . .")
	exit()
	
conn = sqlite3.connect('bancoDeDados.db')

cursor = conn.cursor()