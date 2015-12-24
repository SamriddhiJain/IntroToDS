import numpy as np
import pandas as pd

df= pd.DataFrame.from_csv('titanic_data.csv')

'''
Pclass          Passenger Class
                    (1 = 1st; 2 = 2nd; 3 = 3rd)
    Name            Name
    Sex             Sex
    Age             Age
    SibSp           Number of Siblings/Spouses Aboard
    Parch           Number of Parents/Children Aboard
    Ticket          Ticket Number
    Fare            Passenger Fare
    Cabin           Cabin
    Embarked        Port of Embarkation
                    (C = Cherbourg; Q = Queenstown; S = Southampton)
'''

#print df.describe()
print df[['SibSp','Fare','Survived']][(df.Fare>20) & (df.Sex=='male') & (df.Age>18) & (df.Pclass!=1)]