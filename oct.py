def convert_oct(num_dec):
	list_oct = []
	num = num_dec
	num_oct = ''

	while True:
		rest_div = num % 8
		div_int = num // 8

		print('rest_div', rest_div)
		print('div_int', div_int)

		if div_int < 8:
			list_oct.append(rest_div)
			list_oct.append(div_int)
			break
		else:
			list_oct.append(rest_div)
			num = div_int

	list_oct.reverse()

	for i in list_oct:
		num_oct += str(i)

	return int(num_oct)

def convert_oct_from_dec(num_oct):
	list_num_dec = []
	num_dec = 0
	num = str(num_oct)
	num = list(num)
	tamanho = len(num)

	for i in range(tamanho):
		num[i] = int(num[i])

	num.reverse()

	for i in range(tamanho):
		list_num_dec.append(num[i] * (8 ** i))

	for i in list_num_dec:
		num_dec += i

	return num_dec