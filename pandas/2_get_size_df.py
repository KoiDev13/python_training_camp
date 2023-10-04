import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    row, col = players.shape
    return [row, col]

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

print(df)