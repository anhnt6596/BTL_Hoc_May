def sma(list, title, number, index = 10):
    title.append('<sma' + str(number) + '>')
    new_list = []
    for counter, item in enumerate(list):
        if counter == 0:
            print(item)
        n_back = 0 # Số ngày lùi lại (number - 1) không tính ngày hiện tại
        total = 0. # Tổng
        # print(counter)
        if counter < number: n_back = counter
        else: n_back = number - 1
        # print(n_back)
        for i in list[counter - n_back : counter + 1]:
            total += i[index]
        sma_val = total / (n_back + 1) 
        item.append(sma_val)
        new_list.append(item)
    list = new_list