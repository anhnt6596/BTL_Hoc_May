def sma(list, title, number, index = 10):
    title.append('<SMA(' + str(number) + ')>')
    new_list = []
    for counter, item in enumerate(list):
        n_back = 0 # Số ngày lùi lại (number - 1) không tính ngày hiện tại
        total = 0. # Tổng
        if counter < number: n_back = counter
        else: n_back = number - 1
        for i in list[counter - n_back : counter + 1]:
            total += i[index]
        sma_val = total / (n_back + 1) 
        item.append(round(sma_val))
        new_list.append(item)
    list = new_list
    print('adding SMA(' + str(number) + ') completed')

# 3 tham số: List, Mảng tiêu đề, chỉ số ngày trung bình gì gì ý của SMA như kiểu SMA(10), SMA(14) các thứ
# Vị trí của Close. Cái này auto 10 là ok r