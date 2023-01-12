import pandas as pd
import plotly.express as px

#import database
table = pd.read_csv("telecom_users.csv")

#-----------------------------------------------------------------------------------------------------------------------
#solving table problems - wrong value recognition and empty values

#wrong value recognition 
table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors="coerce")  
#eraise columns that all values are empty
table = table.dropna(how="all",axis=1)
#eraise lines that have at least one value empty
table = table.dropna(how="any",axis=0)
#remove useless data 
table = table.drop("Unnamed: 0", axis=1)

#------------------------------------------------------------------------------------------------------------------------
#initial analysis

#counting how many people have cancelled - normalize transform the numbers in percent
print(table["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#------------------------------------------------------------------------------------------------------------------------
#compare each column with Churn

#create graph
for column in table.columns:
    graph = px.histogram(table, x=column, color="Churn", text_auto=True)
    #show graph
    graph.show()
