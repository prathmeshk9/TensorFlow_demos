import pandas
data = pandas.read_csv('examples/brain_size.csv', sep=';', na_values=".")
print(data )