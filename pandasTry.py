import pickle

data = [1,2,3,4,5]
file = open('file.txt','rb')
print(type(pickle.load(file)))
