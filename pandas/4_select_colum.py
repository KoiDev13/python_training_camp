import pandas as pd

data = {
    'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
    'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
    'area': [8.516, 17.100, 3.286, 9.597, 1.221],
    'population': [200.40, 143.50, 1252.00, 1357.00, 52.98]
}

df = pd.DataFrame(data)
print(df.iloc[:, 
              [2, 5]])