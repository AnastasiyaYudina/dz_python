Код для colab.research.google.com

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

# import pandas as pd
# df=pd.read_csv('/content/sample_data/california_housing_train.csv')
# df[df['population']<500][['median_house_value']]

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

# min_mhv=df['population'].min()
# df['population']==min_mhv
# df[df['population']==min_mhv].households.max()
