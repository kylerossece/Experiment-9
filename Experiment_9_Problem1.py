import pandas as pd
x1={'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
Math=pd.DataFrame(x1,columns=['Student','Math'])
x2={'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
Electronics=pd.DataFrame(x2,columns=['Student','Electronics'])
x3={'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
geas=pd.DataFrame(x3,columns=['Student','GEAS'])
x4={'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
esat=pd.DataFrame(x4,columns=['Student','ESAT'])
merge=pd.merge(Math,Electronics, how='right', on='Student')
merge1=pd.merge(merge,geas, how='right', on='Student')
merge2=pd.merge(merge1,esat, how='right', on='Student')
X=pd.melt(merge2,id_vars=['Student'],var_name='Subject',value_name='Grades')
