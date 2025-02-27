import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'SP500 or NDX.xlsx'
df = pd.read_excel(file_path)
print(df);

index=range(1,9974)
index1=range(253,9974)
index2=range(32,9974)

SP=df.iloc[index,4]
NDX=df.iloc[index,5]
Data=df.iloc[index,6]

Scng=df.iloc[index1,10]
Ncng=df.iloc[index1,11]

Mn=df.iloc[index,13]
indice_s=Mn[Mn=='S'].index.to_list()
indice_n=Mn[Mn=='N'].index.to_list()
value_s=[10000]*len(indice_s)
value_n=[11000]*len(indice_n)

pro=df.iloc[index,16]
SIG1=df.iloc[index2,17]
SIG2=df.iloc[index2,18]

#plt.figure(1)
#plt.plot(index,Data,color='blue')
#plt.title('Data(blue)')
#plt.grid()

plt.figure(2)
plt.plot(index,SP,color='green')
plt.plot(index,NDX,color='red')
plt.scatter(indice_s,value_s,color='green')
plt.scatter(indice_n,value_n,color='red')
plt.title('S&P500(green) & Nasdaq100(red)')
plt.grid()

plt.figure(3)
plt.plot(index1,100*Scng,color='green')
plt.plot(index1,100*Ncng,color='red')
plt.title('Change 250 days SP(green) & NDX(red)')
plt.grid()

#plt.figure(4)
#plt.plot(index,100*pro,color='green')
#plt.title('pro(green)')
#plt.grid()

#plt.figure(5)
#plt.plot(index2,SIG1,color='red')
#plt.plot(index2,SIG2,color='blue')
#plt.title('SIGN1(red) & SIGN2(blue)')
#plt.grid()
plt.show()
