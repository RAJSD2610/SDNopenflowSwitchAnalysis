import os
import pandas as pd
import matplotlib.pyplot as plt

import seaborn


path= os.path.expanduser("~/Desktop/ece671/udpt8")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
u8=[]
i=0
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
while i<(num_files/2) :
 #      df+=[]
    j=i+1

    path ="/home/vetri/Desktop/ece671/udpt8/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<0:
        y=0 
        
    u8.append(y)
    
    i+=1
print(u8)
path= os.path.expanduser("~/Desktop/ece671/udpnone")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
u=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/udpnone/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<0:
        y=0 
    u.append(y)
    i+=1

print(u)
path= os.path.expanduser("~/Desktop/ece671/tcpnone")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
t=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/tcpnone/fpersec."+str(j)+".csv"
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
path= os.path.expanduser("~/Desktop/ece671/tcpt8")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
t8=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/tcpt8/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<0:
        y=0 
    t8.append(y)
    i+=1

print(t8)

#plt.figure(figsize=(4, 5))
#plt.figure(figsize=(4, 5))
plt.plot(list(range(1,len(u8)+1)),u8, '.-',label="udpt8")
plt.plot(list(range(1,len(u)+1)),u, '.-',label="udpnone")
plt.plot(list(range(1,len(t)+1)),t, '.-',label="tcpnone")
plt.plot(list(range(1,len(t8)+1)),t8, '.-',label="tcpt8")
plt.title("Flows Programmed per Sec")
plt.xlabel("time(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()
