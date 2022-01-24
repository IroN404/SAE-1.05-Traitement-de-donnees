import os, glob, shutil
import pandas as pd
joined_files=os.path.join("U:\Documents\sae15\data\data_raw", "netflix*.csv")

joined_list = glob.glob(joined_files)

df= pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)
export_csv = df.to_csv('merged.csv', index=None, header=True, encoding='utf-8',sep=',')

shutil.move('U:\Documents\sae15\merged.csv', 'U:\Documents\sae15\data\data_merged\merged.csv')