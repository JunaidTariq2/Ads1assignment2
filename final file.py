# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:43:06 2022

@author: HANZALLAH
"""
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
#agricultural land heatmap
def readdata(filename):
   
    file = pd.read_csv(filename)
    return file

dt = readdata('C:\\Users\\HANZALLAH\\OneDrive\\Desktop\\agricultural land.csv')
dt.head()
data =dt.pivot_table(index ="Country Name",columns = "Indicator Name",values=['1990','1991','1992','1993','1994'])
d=data.head(8)
d
plt.figure(figsize=(6,4))
plt.title('agricultural heatmap')
sns.heatmap(data = d, annot = True,fmt='.0f')

#energy consumption heatmap
dta = readdata('C:\\Users\\HANZALLAH\\OneDrive\\Desktop\\energy consuption.csv')
dta.head()
data =dta.pivot_table(index = "Country Name",columns = "Indicator Name",values=['2014','2015','2017','2019'])
ad=data.head(8)
ad
plt.figure(figsize=(9,5))
plt.title("energy graph")
sns.heatmap(data = ad, annot = True)

#Arabal land heatmnap
t = readdata('C:\\Users\\HANZALLAH\\OneDrive\\Desktop\\Arabal land.csv')
ta =t.pivot_table(index ="Country Name",columns = "Indicator Name",values=['1990','1991','1992','1993','1994'])
ed=ta.head(8)
ed
plt.figure(figsize=(7,4))
plt.title("arabal land")
sns.heatmap(data = ed, annot = True,cmap= 'mako')

#arabal land chart
def readdta(filename):
      file = pd.read_csv(filename , usecols=['1961','1962','1963','1964','1965','1966'])
      return file

dt = readdta("C:\\Users\\HANZALLAH\\OneDrive\\Desktop\\Arabal land.csv")
colummns = ['Aruba','Africa Eastern and Southern','Afghanistan', 'Africa Western and Central','Angola','Albania']
fi = pd.read_csv("C:\\Users\\HANZALLAH\\OneDrive\\Desktop\\Arabal land.csv")
c_nm = fi['Country Name']
data_frame = pd.DataFrame(dt.head(6))
trans = data_frame.T
trans.columns = c_nm.head(6)
trans
country_names = c_nm.head(6)
years_values = trans.head(6)
years_values
years = list(years_values)
years
first = trans.loc[:,"Aruba"]
second = trans.loc[:,"Africa Eastern and Southern"]
third = trans.loc[:,"Afghanistan"]
fourth = trans.loc[:,"Africa Western and Central"]
fifth = trans.loc[:,"Angola"]
sixth = trans.loc[:,"Albania"]
x = years
y1 = first
y2 = second

fig, ax1 = plt.subplots()
plt.xticks(rotation=90)

ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-',linestyle = ':',label="1961")
ax2.plot(x, y2, 'b-',label="1962")
ax2.spines['left'].set_position(('outward',40))

ax3 = ax2.twinx()
ax3.plot(x,third,'r-',linestyle = ':',label="1963")
ax3.spines['left'].set_position(('outward',60))

ax4 = ax3.twinx()
ax4.plot(x,fourth,color = 'yellow',label="1964")
ax4.spines['left'].set_position(('outward',80))

ax5 = ax4.twinx()
ax5.plot(x,fifth,color="brown",linestyle = ':', label="1965")
ax5.spines['left'].set_position(('outward',100))

ax6 = ax5.twinx()
ax6.plot(x,sixth,color="black", label="1966")

ax1.set_xlabel('years')
ax1.set_ylabel('value')
ax6.set_ylabel('value')
plt.title('arabal land')
plt.show()

#agriculture plt
df = readdta("C:\\Users\\HANZALLAH\\OneDrive\\Desktop\\agricultural land.csv")
colummns = ['Aruba','Africa Eastern and Southern','Afghanistan', 'Africa Western and Central','Angola','Albania']
f11 = pd.read_csv("C:\\Users\\HANZALLAH\\OneDrive\\Desktop\\Arabal land.csv")
c_nnm = fi['Country Name']
data_frame = pd.DataFrame(dt.head(6))
transs = data_frame.T
transs.columns = c_nnm.head(6)
transs
country_names = c_nnm.head(6)
years_value = trans.head(6)
years_value
year = list(years_value)
year
fir = transs.loc[:,"Aruba"]
sec = transs.loc[:,"Africa Eastern and Southern"]
thi = transs.loc[:,"Afghanistan"]
fou = transs.loc[:,"Africa Western and Central"]
fif = transs.loc[:,"Angola"]
six = transs.loc[:,"Albania"]


x = year
y1 = fir
y2 = sec
fig, ax1 = plt.subplots()
plt.xticks(rotation=90)
ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-',linestyle = ':',label="1961")
ax2.plot(x, y2, 'b-',linestyle = ':',label="1962")
ax2.spines['left'].set_position(('outward',40))

ax3 = ax2.twinx()
ax3.plot(x,thi,'r-',label="1963")
ax3.spines['left'].set_position(('outward',80))

ax4 = ax3.twinx()
ax4.plot(x,fou,color = 'yellow',linestyle = ':',label="1964")
ax4.spines['left'].set_position(('outward',190))

ax5 = ax4.twinx()
ax5.plot(x,fif,color="brown",linestyle = ':', label="1965")
ax5.spines['left'].set_position(('outward',120))

ax6 = ax5.twinx()
ax6.plot(x,six,color="black",linestyle = ':', label="1966")


ax1.set_xlabel('years')
ax1.set_ylabel('value')
ax6.set_ylabel('value')
plt.title("agricultural land")
plt.show()

#arabal population graph
def read_energy(filename):
   
    file = pd.read_csv(filename,usecols=['2021','Country Name','Indicator Name'])
    return file

t= readdata("C:\\Users\\HANZALLAH\\OneDrive\\Desktop\\arabal population.csv")
t.pivot(index='Country Name',columns='Indicator Name',values='2021').plot(kind='bar',figsize = (15,8),width = 0.7)
plt.title('population increase')
plt.ylabel('val')

#energy consuption graph
f = read_energy('C:\\Users\\HANZALLAH\\OneDrive\\Desktop\\energy consuption.csv')
t = f.head(5)
t.pivot(index='Country Name',columns='Indicator Name',values='2021').plot(kind='bar',figsize = (15,8),width = 0.7)
plt.title('engergy consuption')
plt.ylabel('energy consumed')