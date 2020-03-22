def convert_hexa(num_dec):
	list_hexa = []
	list_letra = ['A', 'B', 'C', 'D', 'E', 'F']
	list_num = [10, 11, 12, 13, 14, 15, 16]
	num = num_dec
	num_hexa = ''

	while True:
		rest_div = num % 16
		div_int = num // 16

		if div_int < 16:
			list_hexa.append(rest_div)
			list_hexa.append(div_int)
			break
		else:
			list_hexa.append(rest_div)
			num = div_int

	for i in list_hexa:
		if i in list_num:
			pos_num = list_num.index(i)
			pos_num_list = list_hexa.index(i)
			list_hexa[pos_num_list] = list_letra[pos_num]

	list_hexa.reverse()

	for i in list_hexa:
		num_hexa += str(i)

	return num_hexa

def convert_hexa_from_dec(num_hex):
	list_num_dec = []
	list_letra = ['A', 'B', 'C', 'D', 'E', 'F']
	list_num = [10, 11, 12, 13, 14, 15, 16]
	num_dec = 0
	num = list(num_hex)
	tamanho = len(num)

	for i in num:
		if i in list_letra:
			pos_letra = list_letra.index(i)
			pos_num = list_num[pos_letra]
			pos_letra = num.index(i)
			num[pos_letra] = pos_num

	for i in range(tamanho):
		num[i] = int(num[i])

	num.reverse()

	for i in range(tamanho):
		list_num_dec.append(num[i] * (16 ** i))

	for i in list_num_dec:
		num_dec += i

	return num_dec