import pandas as pd
df=pd.read_csv('cars.csv')
A=df.iloc[:5,1:11:2]
B=df[df['Model']== 'Mazda RX4']
C=df.ix[df['Model']== 'Camaro Z28' , ['cyl']]
D=df.ix[[1,28,18],['cyl','gear']]
