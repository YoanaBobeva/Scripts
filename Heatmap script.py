import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#data2 = pd.read_excel('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\CSF extracellular\\CSF extracellular.xlsx', index_col=0)
#data2_tran =data2.T
#data3 = pd.read_excel('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\Machine learning\\ML plasma.xlsx', index_col=0)
#data3_tran =data3.T
#data4 = pd.read_excel('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\Machine learning\\ML CSF T.xlsx', index_col=0)
#data5= pd.read_excel('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\Olfactory\\Olfactory.xlsx', index_col=0)
#data5_tran =data5.T
#data6= pd.read_excel('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\Proteomic of exosome\\Exosome.xlsx', index_col=0)
#data6_tran =data6.T
#data7= pd.read_excel('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\Revealing the proteome\\Revealing data.xlsx', index_col=0)
#data7_tran =data7.T
#data8= pd.read_excel('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\Combined tissue\\Combined tissues .xlsx', index_col=0)
#data8_tran =data8.T
#data9= pd.read_excel('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\Cerebrospinal\\Cereb_all3Ready.xlsx', index_col=0)
#data9_tran =data9.T
data10= pd.read_csv('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\A Proteomic Network\\A prot ALS stats.csv', index_col=0)
data10_tran =data10.T
#data11= pd.read_excel('C:\\Users\\Client\\My Drive\\PhD\\Programing\\R\\Datasets\\Charact of PD\\Char of PD full.xlsx', index_col=0)
#data11_tran =data11.T



plt.figure(figsize=(40, 10))
#plt.title("CSF extracellular", size=15)
#plt.title("Machine learning Plasma", size=15)
#plt.title("Machine learning CSF", size=15)
#plt.title("Olfactory bulb", size=15)
#plt.title("Proteomic of exosome", size=15)
#plt.title("Revealing the proteome", size=15)
#plt.title("Combined tissues", size=15)
#plt.title("Cerebrospinal", size=15)
#plt.title("Characterization of Parkinson`s Disease", size=15)
sns.color_palette("viridis")
#sns.heatmap(data2_tran, center=0, cmap="viridis")
#sns.heatmap(data3_tran, center=30, cmap="viridis")
#sns.heatmap(data4, center=30, cmap="viridis")
#sns.heatmap(data5_tran, center=0, cmap="viridis")
#sns.heatmap(data6_tran, center=0, cmap="viridis")
#sns.heatmap(data7_tran, center=15, cmap="viridis")
#sns.heatmap(data8_tran, center=0, cmap="viridis")
#sns.heatmap(data9_tran, center=5, cmap="viridis")
#sns.heatmap(data10_tran, center=25, cmap="viridis")
als=sns.heatmap(data10_tran, center=3, cmap="viridis")
als.set(title="Heatmap",
      xlabel="Years",
      ylabel="Country Name",)
sns.set(font_scale=2)
#data4_tran.to_excel('ML CSF T.xlsx', index=False)

plt.show()
