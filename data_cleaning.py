import numpy as np
import pandas as pd

df = pd.read_csv('data/all_data_frame.csv', low_memory=False)
df.drop_duplicates()




