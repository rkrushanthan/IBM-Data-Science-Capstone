import pandas as pd
import numpy as np

df=pd.read_csv("dataset_part_1.csv")
#print(df.head(10))

#percentage of null values
print(df.isnull().sum()/len(df)*100)

#column types
print(df.dtypes)

#Number of launch sites
print(df['LaunchSite'].value_counts())

#Number of Orbits
print(df['Orbit'].value_counts())

#Number of landing outcomes
landing_outcomes = df['Outcome'].value_counts()
print(landing_outcomes)

for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)
    
bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
print(bad_outcomes)

#If the value is zero, the first stage did not land successfully; one means the first stage landed Successfully
landing_class = [0 if outcome in bad_outcomes else 1 for outcome in df['Outcome']]
df['Class']=landing_class
print(df.head())

#success rate
print(df["Class"].mean())

df.to_csv("dataset_part_2.csv", index=False)

