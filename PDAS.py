import pandas as pd
import numpy as np
pd.set_option("display.max_rows", None)

class PDAS:
    
    def __init__(self, path_to_data_on_excel):
        self.path_to_data_on_excel= path_to_data_on_excel
        
    def data(self):
        df1 = pd.read_excel(self.path_to_data_on_excel,sheet_name='Sheet1', index_col = 'Age exact (x)')
        return df1

        
        
    
    def aide(self):
        df1 = pd.read_excel(self.path_to_data_on_excel,sheet_name='Sheet1', index_col = 'Age exact (x)')
        df1['1Lx+1'] = df1['1Lx'].shift(-1)
        df1.dropna()
        A = [0]
        for i in range(df1.shape[0]-1):
            A.append((df1['Fx'][i]*df1['1Lx+1'][i])/df1['1Lx'][i] + (df1['1SMx'][i]*(df1['1Lx+1'][i])/df1['1Lx'][i])/(2*df1['1Lx'][i]))
        df1["F'x"]= np.array(A)
        return df1
    
    def estim_N(self):
        df2 = pd.read_excel(self.path_to_data_on_excel,sheet_name='Sheet2')
        df2.columns = ['Age x', '1fx']
        dfa = self.aide().iloc[15:50,[2]]
        dfb = self.aide().iloc[15:50,[5]]
        df2['Effectif moyen'] = list((dfa['Fx']+dfb["F'x"])/2)
        df2['1fx*Effectif moyen'] = df2['1fx']*df2['Effectif moyen']
        N = df2['1fx*Effectif moyen'].sum()
        print('N (le nombre de naissances) estimé sur la base de la table de fécondité vaut: ', N)
        print('La table de fécondité')
        return df2
    
    def projection(self):
        df1 = pd.read_excel(self.path_to_data_on_excel,sheet_name='Sheet1', index_col = 'Age exact (x)')
        df1['1Lx+1'] = df1['1Lx'].shift(-1)
        df1.dropna()
        A = [(self.naissances()*0.488*df1['1Lx'][0])/df1['lx'][0]]
        for i in range(df1.shape[0]-1):
            A.append((df1['Fx'][i]*df1['1Lx+1'][i])/df1['1Lx'][i])
        df1["F'x"]= np.array(A)
        return df1
    
    def naissances(self):
        df2 = pd.read_excel(self.path_to_data_on_excel,sheet_name='Sheet2')
        df2.columns = ['Age x', '1fx']
        dfa = self.aide().iloc[15:50,[2]]
        dfb = self.aide().iloc[15:50,[5]]
        df2['Effectif moyen'] = list((dfa['Fx']+dfb["F'x"])/2)
        df2['1fx*Effectif moyen'] = df2['1fx']*df2['Effectif moyen']
        N = df2['1fx*Effectif moyen'].sum()
        return N
        
        
        
