import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys

path = "/".join(sys.argv[0].split("\\")[:-1])+"/"

st.set_page_config(page_title="finalproject_team53)", layout="wide")

hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibllity: hidden;}
</style>
"""

df = pd.read_csv('world_population.csv')
col = df.columns.values.tolist()
sidebar = st.sidebar

st.info("Word population simple visualization")

year = sidebar.selectbox("Choose year", col[5:13], 0)
continent = sidebar.selectbox("Choose continent", ["All continent"]+list(set(df[col[4]].values)), 0)

if continent!="All continent":
    data0 = df[(df["Continent"]==continent)][["Country/Territory", year]].copy()
    data0.sort_values(by=year, ascending=False, inplace=True)
    sidebar.table(data0)
else:
    data0 = df[["Country/Territory", year]].copy()
    data0.sort_values(by=year, ascending=False, inplace=True)
    sidebar.table(data0)

col1, col2 = st.columns([4, 8])

data1 = df[["Country/Territory", year]].copy().sort_values(by=year, ascending=False)
plt.style.use("ggplot")

fig = plt.figure(figsize=(10, 100), dpi=300)
plt.rcParams.update({'font.size': 50})

plt.barh(list(range(50)), (data1[year]/1e8).values.tolist()[:50][::-1])
plt.yticks(list(range(50)), data1["Country/Territory"].values.tolist()[:50][::-1])
plt.xticks(list(range(15)), rotation=90, fontsize=40)
plt.xlabel("population($10^8$)")
plt.ylabel("Country/Territory")
plt.ylim(-1, 51)
plt.title("Top 50 population of Country/Territory(%s)"%year, fontsize=50, loc="right")

col1.pyplot(fig)

data2 = pd.pivot_table(df, index="Continent", values=year, aggfunc="sum")
fig = plt.figure()
plt.rcParams.update({'font.size': 8})
labels = []
for i, j in list(zip(data2.index.values.tolist(), data2[year])):
    labels.append(str(i)+"(%s)"%(str(j)))
plt.pie(data2[year], labels=labels, autopct="%0.2f%%", wedgeprops={"width":0.3})
plt.title("Population of every continent")
plt.tight_layout()

col2.pyplot(fig)

data3 = df.sort_values(by="Growth Rate", ascending=False)
data3.index = list(range(data3.shape[0]))
print(data3.head())
fig = plt.figure(figsize=(6, 3))
plt.rcParams.update({'font.size': 8})

plt.plot(list(range(len(col[5:13]))), data3.loc[0].values.tolist()[5:13][::-1])
plt.plot(list(range(len(col[5:13]))), data3.loc[1].values.tolist()[5:13][::-1])
plt.plot(list(range(len(col[5:13]))), data3.loc[2].values.tolist()[5:13][::-1])
plt.plot(list(range(len(col[5:13]))), data3.loc[3].values.tolist()[5:13][::-1])
plt.plot(list(range(len(col[5:13]))), data3.loc[4].values.tolist()[5:13][::-1])
plt.legend(["Top "+str(i)+" "+j for i, j in zip(list(range(1, 6)), data3["Country/Territory"].values[:5].tolist())])
plt.xticks(list(range(len(col[5:13]))), col[5:13][::-1], rotation=90) 
plt.title("Top 5 growth rate country population groth")

col2.pyplot(fig)

fig = plt.figure(figsize=(6, 2.46))
plt.rcParams.update({'font.size': 8})
plt.hist(df[year], bins=50)
plt.xlabel("Country population count")
plt.ylabel("Number")
plt.title(year+" cut")

col2.pyplot(fig)


'Q1:The Trend of World Population.'
'ANWSER: '
'It is not difficult to find out from the chart of population cut of each year, the number of countries in the first range decreased from 200 to about 175.'


'Q2:Why are the populations of Africa and Asia growing together, but the growth rate of Africa is much higher than that of Asia.'
'ANWSER:'
'It can be seen from the world population proportion chart that from 2000 to 2022, with the population growing together, the proportion of Asian population fell from 60.76% to 59.21%, while the proportion of African population rose from 13.32% to 17.89%.'
'Population of Africa grew at an average annual rate of 2.3%, much higher than 1% in Asia.'