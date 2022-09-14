# def octact_identification(mod=5000):
###Code
# mod=5000
# octact_identification(mod)
import pandas as pd                     #imported pandas library
data = pd.read_csv('octant_input.csv')  #reading 'octant_input.csv' file 

data.at[0,'U_avg'] = data['U'].mean()
data.at[0,'V_avg'] = data['V'].mean() # using mean() taking average of U,V and W and making column in csv file
data.at[0,'W_avg'] = data['W'].mean()

data.to_csv('octant_output1.csv')