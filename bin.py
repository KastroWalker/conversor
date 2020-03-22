def convert_bin(num_dec):
    list_bin = []
    num = num_dec
    num_bin = ''

    while True:
        rest_div = num % 2
        div_int = num // 2

        if div_int == 1 or div_int == 0:
            list_bin.append(rest_div)
            list_bin.append(div_int)
            break
        else:
            list_bin.append(rest_div)
            num = div_int

    list_bin.reverse()

    for i in list_bin:
        num_bin += str(i)

    return int(num_bin)

def convert_bin_from_dec(num_bin):
    list_num_dec = []
    num_dec = 0
    num = str(num_bin)
    num = list(num)
    tamanho = len(num)

    for i in range(tamanho):
        num[i] = int(num[i])

    num.reverse()

    for i in range(tamanho):
        list_num_dec.append(num[i] * (2 ** i))

    for i in list_num_dec:
        num_dec += i

    return num_dec