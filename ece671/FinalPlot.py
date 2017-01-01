
# coding: utf-8

# In[6]:

#TCP ftotal
import os
import pandas as pd
import matplotlib.pyplot as plt

import seaborn
seaborn.set()

path= os.path.expanduser("~/Desktop/ece671/ntcp3")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
t3=[]
i=0
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
while i<(num_files/2) :
 #      df+=[]
    j=i+1

    path ="/home/vetri/Desktop/ece671/ntcp3/ftotal."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=3:
        y=0 
        
    t3.append(y)
    
    i+=1
print(t3)
path= os.path.expanduser("~/Desktop/ece671/ntcp10")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
t10=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/ntcp10/ftotal."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=3:
        y=0 
    t10.append(y)
    i+=1

print(t10)
path= os.path.expanduser("~/Desktop/ece671/ntcp8")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
t8=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/ntcp8/ftotal."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=3:
        y=0 
    t8.append(y)
    i+=1

print(t8)
path= os.path.expanduser("~/Desktop/ece671/ntcp15")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
t15=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/ntcp15/ftotal."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=3:
        y=0 
    t15.append(y)
    i+=1

print(t15)
#plt.figure(figsize=(4, 5))
plt.plot(list(range(1,len(t3)+1)),t3, '.-',label="tcpt3")
plt.plot(list(range(1,len(t8)+1)),t8, '.-',label="tcpt8")
plt.plot(list(range(1,len(t10)+1)),t10, '.-',label="tcp10")
plt.plot(list(range(1,len(t15)+1)),t15, '.-',label="tcpt15")
plt.title("Total Flows Present")
plt.xlabel("time(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()


# In[7]:

#UDP ftotal
import os
import pandas as pd
import matplotlib.pyplot as plt

import seaborn
seaborn.set()

path= os.path.expanduser("~/Desktop/ece671/nudp3")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
u3=[]
i=0
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
while i<(num_files/2) :
 #      df+=[]
    j=i+1

    path ="/home/vetri/Desktop/ece671/nudp3/ftotal."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<0:
        y=0 
        
    u3.append(y)
    
    i+=1
print(u3)
path= os.path.expanduser("~/Desktop/ece671/nudp10")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
u10=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/nudp10/ftotal."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<0:
        y=0 
    u10.append(y)
    i+=1

print(u10)
path= os.path.expanduser("~/Desktop/ece671/nudp8")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
u8=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/nudp8/ftotal."+str(j)+".csv"
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
path= os.path.expanduser("~/Desktop/ece671/nudp15")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
u15=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/nudp15/ftotal."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<0:
        y=0 
    u15.append(y)
    i+=1

print(u15)
#plt.figure(figsize=(4, 5))
plt.plot(list(range(1,len(u3)+1)),u3, '.-',label="udpt3")
plt.plot(list(range(1,len(u8)+1)),u8, '.-',label="udpt8")
plt.plot(list(range(1,len(u10)+1)),u10, '.-',label="udpt10")
plt.plot(list(range(1,len(u15)+1)),u15, '.-',label="udpt15")
plt.title("Total Flows Present")
plt.xlabel("time(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()


# In[34]:

#TCP Fpersec
#TCP fpersec
import os
import pandas as pd
import matplotlib.pyplot as plt

import seaborn
seaborn.set()

path= os.path.expanduser("~/Desktop/ece671/ntcp3")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
t3=[]
i=0
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
while i<(num_files/2) :
 #      df+=[]
    j=i+1

    path ="/home/vetri/Desktop/ece671/ntcp3/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=3:
        y=0 
        
    t3.append(y)
    
    i+=1
print(t3)
path= os.path.expanduser("~/Desktop/ece671/ntcp10")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
t10=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/ntcp10/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=3:
        y=0 
    t10.append(y)
    i+=1

print(t10)
path= os.path.expanduser("~/Desktop/ece671/ntcp8")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
t8=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/ntcp8/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=3:
        y=0 
    t8.append(y)
    i+=1

print(t8)
path= os.path.expanduser("~/Desktop/ece671/ntcp15")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
t15=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/ntcp15/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=3:
        y=0 
    t15.append(y)
    i+=1

print(t15)
#sum
s=[]
s3=sum(t3)
s.append(s3)
s8=sum(t8)
s.append(s8)
s10=sum(t10)
s.append(s10)
s15=sum(t15)
s.append(s15)
l=[3,8,10,15]
plt.plot(l,s, '.-',label="total flows")
plt.title("TCP traffic")
plt.xlabel("timeout(s)")
plt.ylabel("flows")
plt.legend()
plt.show()        
#avg
av=[]
av3=s3/(len(t3))
av.append(av3)
av8=s8/(len(t8))
av.append(av8)
av10=s10/(len(t10))
av.append(av10)
av15=s15/(len(t15))
av.append(av15)

plt.plot(l,av, '.-',label="avg flows")
plt.title("TCP traffic")
plt.xlabel("timeout(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()
#frequency
import collections
counter3=collections.Counter(t3)
counter8=collections.Counter(t8)
counter10=collections.Counter(t10)
counter15=collections.Counter(t15)
#frequency of 0
freq0_3=counter[min(t3)]
freq0_8=counter[min(t8)]
freq0_10=counter[min(t10)]
freq0_15=counter[min(t15)]
freq0=[freq0_3,freq0_8,freq0_10,freq0_15]
plt.plot(l,freq0, '.-',label="Frequency of 0 flows")
plt.title("TCP traffic")
plt.xlabel("timeout(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()
#plt.figure(figsize=(4, 5))
plt.plot(list(range(1,len(t3)+1)),t3, '.-',label="tcpt3")
plt.plot(list(range(1,len(t8)+1)),t8, '.-',label="tcpt8")
plt.plot(list(range(1,len(t10)+1)),t10, '.-',label="tcp10")
plt.plot(list(range(1,len(t15)+1)),t15, '.-',label="tcpt15")
plt.title("Flows Programmed per second")
plt.xlabel("time(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()


# In[32]:

#UDP fpersec
#UDP fpersec
import os
import pandas as pd
import matplotlib.pyplot as plt

import seaborn
seaborn.set()

path= os.path.expanduser("~/Desktop/ece671/nudp3")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
u3=[]
i=0
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
while i<(num_files/2) :
 #      df+=[]
    j=i+1

    path ="/home/vetri/Desktop/ece671/nudp3/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=1:
        y=0 
        
    u3.append(y)
    
    i+=1
print(u3)
path= os.path.expanduser("~/Desktop/ece671/nudp10")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
u10=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/nudp10/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=1:
        y=0 
    u10.append(y)
    i+=1

print(u10)
path= os.path.expanduser("~/Desktop/ece671/nudp8")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
u8=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/nudp8/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=1:
        y=0 
    u8.append(y)
    i+=1

print(u8)
path= os.path.expanduser("~/Desktop/ece671/nudp15")
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
print(num_files)
i=0  
j=0
u15=[]
while i<(num_files/2):
    j=i+1

    path ="/home/vetri/Desktop/ece671/nudp15/fpersec."+str(j)+".csv"
    y = file_len(path)
    #    except:       pass
    #df.append(pd.read_csv(path,header=None))        
#       a+=[]
    #y=len(df[i].index)-1 #1 row added by default so that table has a entry
    if y<=1:
        y=0 
    u15.append(y)
    i+=1

print(u15)
#sum
s=[]
s3=sum(u3)
s.append(s3)
s8=sum(u8)
s.append(s8)
s10=sum(u10)
s.append(s10)
s15=sum(u15)
s.append(s15)
l=[3,8,10,15]
plt.plot(l,s, '.-',label="total flows")
plt.title("UDP traffic")
plt.xlabel("timeout(s)")
plt.ylabel("flows")
plt.legend()
plt.show()        
#avg
av=[]
av3=s3/(len(u3))
av.append(av3)
av8=s8/(len(u8))
av.append(av8)
av10=s10/(len(u10))
av.append(av10)
av15=s15/(len(u15))
av.append(av15)

plt.plot(l,av, '.-',label="avg flows")
plt.title("UDP traffic")
plt.xlabel("timeout(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()
#frequency
import collections
counter3=collections.Counter(u3)
counter8=collections.Counter(u8)
counter10=collections.Counter(u10)
counter15=collections.Counter(u15)
#frequency of 0
freq0_3=counter[0]
freq0_8=counter[0]
freq0_10=counter[0]
freq0_15=counter[0]
freq0=[freq0_3,freq0_8,freq0_10,freq0_15]
plt.plot(l,freq0, '.-',label="Frequency of 0 flows")
plt.title("UDP traffic")
plt.xlabel("timeout(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()
#plt.figure(figsize=(4, 5))
plt.plot(list(range(1,len(u3)+1)),u3, '.-',label="udpt3")
plt.plot(list(range(1,len(u8)+1)),u8, '.-',label="udpt8")
plt.plot(list(range(1,len(u10)+1)),u10, '.-',label="udpt10")
plt.plot(list(range(1,len(u15)+1)),u15, '.-',label="udpt15")
plt.title("Flows Programmed per second")
plt.xlabel("time(s)")
plt.ylabel("flows")
#plt.frameon=True
plt.legend()
plt.show()


# In[46]:

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


# In[16]:

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


# In[ ]:



