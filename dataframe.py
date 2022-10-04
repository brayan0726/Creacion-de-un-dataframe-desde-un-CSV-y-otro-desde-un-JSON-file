from importlib.resources import path
import pandas as pd
path ='C:\Users\micri\Documents\IA\TAREA1\\'
file ='data.json'
df = pd.read_json (path + file)

print(df)