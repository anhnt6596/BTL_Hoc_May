def preprocessing(file):
    rows = open(file).read().split('\n')            
    result = []
    for row in rows[1:]:
        str_list = row.split(',')
        float_list = []
        float_list.append(str_list[0])              # Cột đầu là string
        for item in str_list[1:]:
            float_list.append(float(item))          # Các cột khác đổi sang float
        result.append(float_list)
    return result

# train_data = preprocessing('../data/train/training_data_vnindex.csv') # Test
# print(train_data[10])