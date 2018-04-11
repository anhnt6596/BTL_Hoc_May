def rsi(list, title, index = 10):
    tb_lolai_array = tb_lolai(list, index)
    result = []
    for i, item in enumerate(list):
        rs = 0
        rsi = 50
        if (tb_lolai_array[i][0] == 0.) & (tb_lolai_array[i][1] == 0.):
            rsi = 50
        elif tb_lolai_array[i][1] == 0.:
            rsi = 100
        else:
            rs = tb_lolai_array[i][0] / (-1 * tb_lolai_array[i][1])
            rsi = 100 - 100/(1 + rs)
        item.append(round(rsi, 2))
        result.append(item)
    title.append('<RSI>')
    list = result

def tb_lolai(list, index):
    lo_lai_array = lo_lai_theo_ngay(list, index)
    result = [[0., 0.]]
    for i in range(1, len(lo_lai_array)):
        tb_lai = 0
        tb_lo = 0
        tb_lai = (result[i - 1][0] * 13 + lo_lai_array[i][0]) / 14
        tb_lo = (result[i - 1][1] * 13 + lo_lai_array[i][1]) / 14
        result.append([round(tb_lai, 2), round(tb_lo, 2)])
        # print(result[-1])
    return result

def lo_lai_theo_ngay(list, index):
    result = [[0, 0]]
    for i in range(1, len(list)):
        lo = 0.
        lai = 0.
        if list[i][index] >= list[i - 1][index]:
            lai = list[i][index] - list[i - 1][index]
        else: lo = list[i][index] - list[i - 1][index]
        result.append([round(lai, 2), round(lo, 2)])
    return result