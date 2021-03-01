import pandas as pd
import numpy as np

def reviewed_tagging(df1, df2, col11, col12, col13, col21, col22, col23):
    
    for ind in df2.index: 
        df1["review_tag"] = np.where((((df1[col11]==df2[col21][ind]) & (df1[col12]==df2[col22][ind])) & (df1[col13]==df2[col23][ind])),True,False)
    return df1


data1 = {'A':['Tom', 'Jack', 'Steve', 'Ricky'],'B':[28,34,29,42],'C':[1,2,3,4]}
data2 = {'A1':['Tom'],'B1':[28],'C1':[1]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


df1 = reviewed_tagging(df1,df2,'A','B','C','A1','B1','C1')