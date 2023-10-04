import pandas as pd

def createDataFrame(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id','age'])

input = [[1,15],[2,11],[3,11],[4,20]]
my_df = createDataFrame(input)

print(my_df)