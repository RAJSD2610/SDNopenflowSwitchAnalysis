import os
import pandas as pd
import matplotlib.pyplot as plt

import seaborn

path= os.path.expanduser("~/Desktop/ece671/pro/u_ow/FinSnaps")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
a=[]
df=[]
i=0
while i<num_files :
 #      df+=[]
        j=i+1
        try:
            path="~/Desktop/ece671/pro/u_ow/ModFl."+str(j)+".csv"
            df.append(pd.read_csv(path,header=1))
#       a+=[]
            a.append(len(df[i].index))
        except:
            a.append(0)
        i+=1
print(a)
plt.figure(figsize=(4, 5))
seaborn.barplot(x=list(range(1,len(a)+1)),y=a)
plt.xlabel("time(s)")
plt.ylabel("flows")
plt.show()
