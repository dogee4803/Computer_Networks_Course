import pandas as pd

def read_data(file_path):
    data = pd.read_excel(file_path)

    data = [tuple(x) for x in data.values]
    return data