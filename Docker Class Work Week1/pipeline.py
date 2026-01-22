# Pipeline takes inputs and produce output
import sys    #(What is sys and how we can learn about it)
import pandas as pd

month= sys.argv[1]

df = pd.DataFrame({"day": [1,2], "number_passengers": [100, 200]})
df['month'] = month



print(df.head())

df.to_parquet(f"output_{month}.parquet")

print("System arguments", sys.argv)

print(f'Today month is {month} ')