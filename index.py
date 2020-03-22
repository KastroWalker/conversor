from bin import *
from hexa import *
from oct import *

def convert(value, op):
	if op == 1:
		return convert_bin(value)
	elif op == 2:
		return convert_oct(value)
	elif op == 3:
		return convert_hexa(value)
	else:
		return false

def main():
	list_op = [1, 2, 3, 4]
	msg_inicial = """
|----------------------------------|
| Olá Bem Vindo ao Conversor!      |
| O que você deseja fazer?         |
|                                  |
| [1] - Converter para binário     |
| [2] - Converter para octal       |
| [3] - Converter para hexadecimal |
| [4] - Converter para decimal     |
| [0] - Sair                       |
|----------------------------------|
	"""
	msg_decimal = """
|-------------------------------------|
| De qual base você deseja converter? |
|                                     |
| [4] - Converter para binário        |
| [5] - Converter para octal          |
| [6] - Converter para hexadecimal    |
| [0] - Sair                          |
|-------------------------------------|
	"""

	while True:
		op = 0
		if not op == 4:
			print(msg_inicial)
			op = int(input())
		else:
			if op == 0:
				print("\nObrigado por usar nosso conversor!")
				break
			elif op == 4:
				print(msg_decimal)
				op = int(input())
				if op == 1:
					return convert_bin_from_dec(value)
				elif op == 2:
					return convert_oct_from_dec(value)
				elif op == 3:
					return convert_hexa_from_dec(value)
				elif op == 0:
					print("\nObrigado por usar nosso conversor!")
					break
				else:
					print("Operação Inválida tente novamente.\n")
					op = 4
			elif op in list_op:
				pass
			else:
				print("Operação Inválida tente novamente.\n")

main()
