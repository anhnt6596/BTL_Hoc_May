from modules.rw_csv import read_csv, export_csv
from modules.sma import sma
from modules.rsi import rsi

title, train_data = read_csv('./data/train/training_data_vnindex.csv') # Test
# print(train_data[10])
# print(title)

sma(train_data, title, 10, 10)
sma(train_data, title, 14)
sma(train_data, title, 20)
sma(train_data, title, 50)
sma(train_data, title, 100)
sma(train_data, title, 200)
rsi(train_data, title)

# print(title)
# print(train_data[-1])

export_csv(train_data, title, './a.csv')