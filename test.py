from modules.read_csv import read_csv
from modules.sma import sma

title, train_data = read_csv('./data/train/training_data_vnindex.csv') # Test
# print(train_data[10])
# print(title)

sma(train_data, title, 10, 10)
# print(title)
print(train_data[1])