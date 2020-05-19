num1 = float(input("Insira um número: "))
op = input("Escolha um operador: ")
num2 = float(input("Insira mais um número: "))

if op == "+":
	print(num1 + num2)
elif op == "-":
	print(num1 - num2)
elif op == "*":
	print(num1 * num2)
elif op == "/":
	print(num1 / num2)
else:
	print("Operador Inválido...")