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
while i<(num_files/2) :
 #      df+=[]
    j=i+1
    try:
        path="~/Desktop/ece671/SwitchAnalysis/PlotDump/ftotal."+str(j)+".csv"

    #    except:       pass
        df.append(pd.read_csv(path,header=None))        
#       a+=[]
        y=len(df[i].index)-1   #1 row added by default so that table has a entry
        if y>0:
            y-=2              ##1 row added by default so that table has column entry due to 7,8 at i=0
    except:
        y=0
        
    a.append(y)
print(a)
plt.figure(figsize=(4, 5))
seaborn.barplot(x=list(range(1,len(a)+1)),y=a)
plt.title("Total flow Present")
plt.xlabel("time(s)")
plt.ylabel("flows")
plt.show()
