import csv

def read_csv(file):
    rows = open(file).read().split('\n')
    title = rows[0].split(',')    
    result = []
    for row in rows[1:]:
        str_list = row.split(',')
        float_list = []
        float_list.append(str_list[0])              # Cột đầu là string
        for item in str_list[1:]:
            float_list.append(float(item))          # Các cột khác đổi sang float
        result.append(float_list)
    return title, result[:-1]                       # Éo hiểu sao hàng cuối nó cũng đọc vào

def export_csv(list, title, file):
    myFile = open(file, 'w', newline='')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows([title])
        writer.writerows(list[:])
        
    print("Writing complete")
# title, train_data = preprocessing('../data/train/training_data_vnindex.csv') # Test
# print(train_data[10])
# print(title)
