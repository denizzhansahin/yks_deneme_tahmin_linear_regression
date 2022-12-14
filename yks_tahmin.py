# -*- coding: utf-8 -*-
"""yks_tahmin.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#verileri kullanilabilir duruma getirin
veriler = pd.read_csv("yks_deneme_veri.csv")
#print(veriler)

#deneme sayisi
deneme_sayisi = veriler.iloc[:,0:1]
deneme_veri = deneme_sayisi.values
denemeListe = list(deneme_sayisi.shape)
denemeSayisi = denemeListe[0]

#tyt veri islenmesi
turkce = veriler.iloc[:,1:2]
Turkce = turkce.values
matematikTYT = veriler.iloc[:,2:3]
MatematikTYT = matematikTYT.values
sosyalTYT = veriler.iloc[:,3:4]
SosyalTYT = sosyalTYT.values
fenTYT = veriler.iloc[:,4:5]
FenTYT = fenTYT.values

#ayt veri islenmesi
edebiyatAYT = veriler.iloc[:,5:6]
EdebiyatAYT = edebiyatAYT.values
matematikAYT = veriler.iloc[:,6:7]
MatematikAYT = matematikAYT.values
sosyalAYT = veriler.iloc[:,7:8]
SosyalAYT = sosyalAYT.values
fenAYT = veriler.iloc[:,8:9]
FenAYT = fenAYT.values

#Gecmis veriler icin dogrusal regresyon grafigi cizimi
#Bagimsiz degisken deneme sayisi, bagımli degisken TURKCE TYT net sayisi
from sklearn.linear_model import LinearRegression
turkceLR = LinearRegression()
turkceLR.fit(deneme_veri,Turkce)
plt.plot(deneme_veri,Turkce,color="red")
#plt.plot(turkce,lin_reg.predict(Turkce),color="blue")
plt.title("Son {} Deneme TURKCE TYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme Sayisi")
plt.ylabel("Netler")
plt.show()

#Gecmis veriler icin dogrusal regresyon grafigi cizimi
#Bagimsiz degisken deneme sayisi, bagımli degisken MATEMATİK TYT net sayisi
from sklearn.linear_model import LinearRegression
matTYT_LR = LinearRegression()
matTYT_LR.fit(deneme_veri,MatematikTYT)
plt.plot(deneme_veri,MatematikTYT,color="red")
plt.title("Son {} Deneme MATEMATİK TYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme")
plt.ylabel("Netler")
plt.show()

#Gecmis veriler icin dogrusal regresyon grafigi cizimi
#Bagimsiz degisken deneme sayisi, bagımli degisken SOSYAL TYT net sayisi
from sklearn.linear_model import LinearRegression
sosyalTYT_LR = LinearRegression()
sosyalTYT_LR.fit(deneme_veri,SosyalTYT)
plt.plot(deneme_veri,SosyalTYT,color="red")
plt.title("Son {} Deneme SOSYAL TYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme")
plt.ylabel("Netler")
plt.show()

#Gecmis veriler icin dogrusal regresyon grafigi cizimi
#Bagimsiz degisken deneme sayisi, bagımli degisken FEN TYT net sayisi
from sklearn.linear_model import LinearRegression
fenTYT_LR = LinearRegression()
fenTYT_LR.fit(deneme_veri,FenTYT)
plt.plot(deneme_veri,FenTYT,color="red")
plt.title("Son {} Deneme FEN TYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme")
plt.ylabel("Netler")
plt.show()

#Gecmis veriler icin dogrusal regresyon grafigi cizimi
#Bagimsiz degisken deneme sayisi, bagımli degisken EDEBİYAT AYT net sayisi
from sklearn.linear_model import LinearRegression
edebiyatAYT_LR = LinearRegression()
edebiyatAYT_LR.fit(deneme_veri,EdebiyatAYT)
plt.plot(deneme_veri,EdebiyatAYT,color="blue")
plt.title("Son {} Deneme EDEBİYAT AYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme")
plt.ylabel("Netler")
plt.show()

#Gecmis veriler icin dogrusal regresyon grafigi cizimi
#Bagimsiz degisken deneme sayisi, bagımli degisken MATEMATİK AYT net sayisi
from sklearn.linear_model import LinearRegression
matematikAYT_LR = LinearRegression()
matematikAYT_LR.fit(deneme_veri,MatematikAYT)
plt.plot(deneme_veri,MatematikAYT,color="blue")
plt.title("Son {} Deneme MATEMATİK AYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme")
plt.ylabel("Netler")
plt.show()

#Gecmis veriler icin dogrusal regresyon grafigi cizimi
#Bagimsiz degisken deneme sayisi, bagımli degisken SOSYAL AYT net sayisi
from sklearn.linear_model import LinearRegression
sosyalAYT_LR = LinearRegression()
sosyalAYT_LR.fit(deneme_veri,SosyalAYT)
plt.plot(deneme_veri,SosyalAYT,color="blue")
plt.title("Son {} Deneme SOSYAL AYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme")
plt.ylabel("Netler")
plt.show()

#Gecmis veriler icin dogrusal regresyon grafigi cizimi
#Bagimsiz degisken deneme sayisi, bagımli degisken FEN AYT net sayisi
from sklearn.linear_model import LinearRegression
fenAYT_LR = LinearRegression()
fenAYT_LR.fit(deneme_veri,FenAYT)
plt.plot(deneme_veri,FenAYT,color="blue")
plt.title("Son {} Deneme FEN AYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme")
plt.ylabel("Netler")
plt.show()

#Tahmin icin yapilacak gun sayisini yaziniz
print("Tahmin icin yapilacak deneme sayisini yaziniz: ")
deneme_sayisi_deneme = int(input())

#GELCEK GUNLAR ICIN TAHMİN
print("-------------------TURKCE TYT----------------------")
degerList_TURKCE_TYT = []
for i in range(deneme_sayisi_deneme):
  print("Önünüzdeki ",i+1,".deneme TURKCE TYT tahmini")
  print(turkceLR.predict([[i+deneme_sayisi_deneme]]))
  sayi_turkce = turkceLR.predict([[i+deneme_sayisi_deneme]])
  degerList_TURKCE_TYT.append(sayi_turkce)

print("\n-------------------MATEMATİK TYT----------------------")
degerList_MATEMATIK_TYT = []
for i in range(deneme_sayisi_deneme):
  print("Önünüzdeki ",i+1,".deneme MATEMATİK TYT tahmini")
  print(matTYT_LR.predict([[i+deneme_sayisi_deneme]]))
  sayi_matematik_tyt = matTYT_LR.predict([[i+deneme_sayisi_deneme]])
  degerList_MATEMATIK_TYT.append(sayi_matematik_tyt)

print("\n-------------------SOSYAL TYT----------------------")
degerList_SOSYAL_TYT = []
for i in range(deneme_sayisi_deneme):
  print("Önünüzdeki ",i+1,".deneme SOSYAL TYT tahmini")
  print(sosyalTYT_LR.predict([[i+deneme_sayisi_deneme]]))
  sayi_sosyal_tyt = sosyalTYT_LR.predict([[i+deneme_sayisi_deneme]])
  degerList_SOSYAL_TYT.append(sayi_sosyal_tyt)

print("\n-------------------FEN TYT----------------------")
degerList_FEN_TYT = []
for i in range(deneme_sayisi_deneme):
  print("Önünüzdeki ",i+1,".deneme FEN TYT tahmini")
  print(fenTYT_LR.predict([[i+deneme_sayisi_deneme]]))
  sayi_fen_tyt = fenTYT_LR.predict([[i+deneme_sayisi_deneme]])
  degerList_FEN_TYT.append(sayi_fen_tyt)

print("\n-------------------EDEBİYAT AYT----------------------")
degerList_EDEBYAT_AYT = []
for i in range(deneme_sayisi_deneme):
  print("Önünüzdeki ",i+1,".deneme EDEBİYAT AYT tahmini")
  print(edebiyatAYT_LR.predict([[i+deneme_sayisi_deneme]]))
  sayi_edebiyat_ayt = edebiyatAYT_LR.predict([[i+deneme_sayisi_deneme]])
  degerList_EDEBYAT_AYT.append(sayi_edebiyat_ayt)

print("\n-------------------SOSYAL AYT----------------------")
degerList_SOSYAL_AYT = []
for i in range(deneme_sayisi_deneme):
  print("Önünüzdeki ",i+1,".deneme SOSYAL AYT tahmini")
  print(sosyalAYT_LR.predict([[i+deneme_sayisi_deneme]]))
  sayi_sosyal_ayt = sosyalAYT_LR.predict([[i+deneme_sayisi_deneme]])
  degerList_SOSYAL_AYT.append(sayi_sosyal_ayt)

print("\n-------------------MATEMATİK AYT----------------------")
degerList_MATEMATİK_AYT = []
for i in range(deneme_sayisi_deneme):
  print("Önünüzdeki ",i+1,".deneme SOSYAL AYT tahmini")
  print(matematikAYT_LR.predict([[i+deneme_sayisi_deneme]]))
  sayi_matematik_ayt = matematikAYT_LR.predict([[i+deneme_sayisi_deneme]])
  degerList_MATEMATİK_AYT.append(sayi_matematik_ayt)

print("\n-------------------FEN AYT----------------------")
degerList_FEN_AYT = []
for i in range(deneme_sayisi_deneme):
  print("Önünüzdeki ",i+1,".deneme SOSYAL AYT tahmini")
  print(fenAYT_LR.predict([[i+deneme_sayisi_deneme]]))
  sayi_fen_ayt = fenAYT_LR.predict([[i+deneme_sayisi_deneme]])
  degerList_FEN_AYT.append(sayi_fen_ayt)

#GRAFİKLER İCİN DATA FRAME HAZIRLANMASI
#GUN DATAFRAME
ls_deneme_sayisi = []
for i in range(deneme_sayisi_deneme):
  ls_deneme_sayisi.append(i+1)

deneme_sayisi_name = ['gun']
veriseti_deneme = pd.DataFrame(data=ls_deneme_sayisi, columns=deneme_sayisi_name)

#TURKCE DATAFRAME
ls_turkce_tyt = []
for i in range(deneme_sayisi_deneme):
  b = float(degerList_TURKCE_TYT[i])
  ls_turkce_tyt.append(b)

turkce_name = ['turkce']
veriseti_turkce = pd.DataFrame(data=ls_turkce_tyt, columns=turkce_name)

#MATEMATİK TYT DATAFRAME
ls_matematik_tyt = []
for i in range(deneme_sayisi_deneme):
  b = float(degerList_MATEMATIK_TYT[i])
  ls_matematik_tyt.append(b)

matematikTYT_name = ['matematik']
veriseti_matematik_tyt = pd.DataFrame(data=ls_matematik_tyt, columns=matematikTYT_name)

#SOSYAL TYT DATAFRAME
ls_sosyal_tyt = []
for i in range(deneme_sayisi_deneme):
  b = float(degerList_SOSYAL_TYT[i])
  ls_sosyal_tyt.append(b)

sosyalTYT_name = ['sosyal']
veriseti_sosyal_tyt = pd.DataFrame(data=ls_sosyal_tyt, columns=sosyalTYT_name)

#FEN TYT DATAFRAME
ls_fen_tyt = []
for i in range(deneme_sayisi_deneme):
  b = float(degerList_FEN_TYT[i])
  ls_fen_tyt.append(b)

fenTYT_name = ['fen']
veriseti_fen_tyt = pd.DataFrame(data=ls_sosyal_tyt, columns=fenTYT_name)

#EDEBİYAT AYT DATAFRAME
ls_edebiyat_ayt = []
for i in range(deneme_sayisi_deneme):
  b = float(degerList_EDEBYAT_AYT[i])
  ls_edebiyat_ayt.append(b)

edebiyatAYT_name = ['edebiyat']
veriseti_edebiyat_ayt = pd.DataFrame(data=ls_edebiyat_ayt, columns=edebiyatAYT_name)

#SOSYAL AYT DATAFRAME
ls_sosyal_ayt = []
for i in range(deneme_sayisi_deneme):
  b = float(degerList_SOSYAL_AYT[i])
  ls_sosyal_ayt.append(b)

sosyalAYT_name = ['edebiyat']
veriseti_sosyal_ayt = pd.DataFrame(data=ls_sosyal_ayt, columns=sosyalAYT_name)

#MATEMATİK AYT DATAFRAME
ls_matematik_ayt = []
for i in range(deneme_sayisi_deneme):
  b = float(degerList_MATEMATİK_AYT[i])
  ls_matematik_ayt.append(b)

matematikAYT_name = ['edebiyat']
veriseti_matematik_ayt = pd.DataFrame(data=ls_matematik_ayt, columns=matematikAYT_name)

#FEN AYT DATAFRAME
ls_fen_ayt = []
for i in range(deneme_sayisi_deneme):
  b = float(degerList_FEN_AYT[i])
  ls_fen_ayt.append(b)

fenAYT_name = ['edebiyat']
veriseti_fen_ayt = pd.DataFrame(data=ls_fen_ayt, columns=fenAYT_name)

#TAHMİN GRAFİĞİ İÇİN VERİ İŞLEME
x_deneme = veriseti_deneme.iloc[:,0:1]
x_deneme_veri = list(x_deneme.shape)

y_turkce_tyt = veriseti_turkce.iloc[:,0:1]
y_matematik_tyt = veriseti_matematik_tyt.iloc[:,0:1]
y_sosyal_tyt = veriseti_sosyal_tyt.iloc[:,0:1]
y_fen_tyt = veriseti_fen_tyt.iloc[:,0:1]
y_edebiyat_ayt = veriseti_edebiyat_ayt.iloc[:,0:1]
y_sosyal_ayt = veriseti_sosyal_ayt.iloc[:,0:1]
y_matematik_ayt = veriseti_matematik_ayt.iloc[:,0:1]
y_fen_ayt = veriseti_fen_ayt.iloc[:,0:1]

X = x_deneme.values
Y_tt = y_turkce_tyt.values
Y_mt = y_matematik_tyt.values
Y_st = y_sosyal_tyt.values
Y_ft = y_fen_tyt.values
Y_ea = y_edebiyat_ayt.values
Y_sa = y_sosyal_ayt.values
Y_ma = y_matematik_ayt.values
Y_fa = y_fen_ayt.values

#GRAFİK ÇİZİMLERİ
#Gecmis veriler icin dogrusal regresyon grafigi cizimi
#Bagimsiz degisken deneme sayisi, bagımli degisken TURKCE TYT tahmin net sayisi
from sklearn.linear_model import LinearRegression
tahmin = LinearRegression()
tahmin.fit(X,Y_tt)
plt.plot(X,Y_tt,color="red")
plt.title("Gelecek {} Deneme TURKCE TYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme Sayisi")
plt.ylabel("Netler")
plt.show()

#Bagimsiz degisken deneme sayisi, bagımli degisken MATEMATİK TYT tahmin net sayisi
from sklearn.linear_model import LinearRegression
tahmin = LinearRegression()
tahmin.fit(X,Y_mt)
plt.plot(X,Y_mt,color="red")
plt.title("Gelecek {} Deneme MATEMATİK TYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme Sayisi")
plt.ylabel("Netler")
plt.show()

#Bagimsiz degisken deneme sayisi, bagımli degisken SOSYAL TYT tahmin net sayisi
from sklearn.linear_model import LinearRegression
tahmin = LinearRegression()
tahmin.fit(X,Y_st)
plt.plot(X,Y_st,color="red")
plt.title("Gelecek {} Deneme SOSYAL TYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme Sayisi")
plt.ylabel("Netler")
plt.show()

#Bagimsiz degisken deneme sayisi, bagımli degisken FEN TYT tahmin net sayisi
from sklearn.linear_model import LinearRegression
tahmin = LinearRegression()
tahmin.fit(X,Y_ft)
plt.plot(X,Y_ft,color="red")
plt.title("Gelecek {} Deneme FEN TYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme Sayisi")
plt.ylabel("Netler")
plt.show()

#Bagimsiz degisken deneme sayisi, bagımli degisken EDEBİYAT AYT tahmin net sayisi
from sklearn.linear_model import LinearRegression
tahmin = LinearRegression()
tahmin.fit(X,Y_ea)
plt.plot(X,Y_ea,color="red")
plt.title("Gelecek {} Deneme EDEBİYAT AYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme Sayisi")
plt.ylabel("Netler")
plt.show()

#Bagimsiz degisken deneme sayisi, bagımli degisken SOSYAL AYT tahmin net sayisi
from sklearn.linear_model import LinearRegression
tahmin = LinearRegression()
tahmin.fit(X,Y_sa)
plt.plot(X,Y_sa,color="red")
plt.title("Gelecek {} Deneme SOSYAL AYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme Sayisi")
plt.ylabel("Netler")
plt.show()

#Bagimsiz degisken deneme sayisi, bagımli degisken MATEMATİK AYT tahmin net sayisi
from sklearn.linear_model import LinearRegression
tahmin = LinearRegression()
tahmin.fit(X,Y_ma)
plt.plot(X,Y_ma,color="red")
plt.title("Gelecek {} Deneme MATEMATİK AYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme Sayisi")
plt.ylabel("Netler")
plt.show()

#Bagimsiz degisken deneme sayisi, bagımli degisken FEN AYT tahmin net sayisi
from sklearn.linear_model import LinearRegression
tahmin = LinearRegression()
tahmin.fit(X,Y_fa)
plt.plot(X,Y_fa,color="red")
plt.title("Gelecek {} Deneme FEN AYT Net Grafiği".format(denemeSayisi))
plt.xlabel("Deneme Sayisi")
plt.ylabel("Netler")
plt.show()
