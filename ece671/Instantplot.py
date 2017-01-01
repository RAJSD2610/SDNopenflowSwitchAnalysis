import os
import pandas as pd
import matplotlib.pyplot as plt

import seaborn

path= os.path.expanduser("~/Desktop/ece671/SwitchAnalysis/PlotDump")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
t=[]
i=0
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
while i<(num_files/2) :
 #      df+=[]
    j=i+1

    path ="/home/vetri/Desktop/ece671/SwitchAnalysis/PlotDump/ftotal."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<0:
        y=0 
        
    t.append(y)
    
    i+=1
print(t)
path= os.path.expanduser("~/Desktop/ece671/SwitchAnalysis/PlotDump")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
f=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/SwitchAnalysis/PlotDump/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=1:
        y=0 
    f.append(y)
    i+=1

print(f)
plt.plot(list(range(1,len(t)+1)),t, '.-',label="traffic type and timeout")
plt.title("Total Flows Present after 1st flow")
plt.xlabel("time(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()
plt.plot(list(range(1,len(f)+1)),f, '.-',label="traffic type and timeout")
plt.title("Flows programmed per sec")
plt.xlabel("time(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()

