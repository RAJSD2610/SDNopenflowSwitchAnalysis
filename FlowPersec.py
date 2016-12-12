import os
import pandas as pd
import matplotlib.pyplot as plt

import seaborn


path= os.path.expanduser("~/Desktop/ece671/SwitchAnalysis/PlotDump")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
a=[]
df=[]
i=0
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
while i<(num_files/2) :
 #      df+=[]
    j=i+1

    path ="/home/vetri/Desktop/ece671/SwitchAnalysis/PlotDump/fpersec."+str(j)+".csv"
    y = file_len(path)

    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    
    y-=2
    
    if y<0:
        y=0
        
        
    a.append(y)
    i+=1
    
print(a)
#plt.figure(figsize=(4, 5))
seaborn.barplot(x=list(range(1,len(a)+1)),y=a)
plt.title("Flows Programmed persec")
plt.xlabel("time(s)")
plt.ylabel("flows")
plt.show()
