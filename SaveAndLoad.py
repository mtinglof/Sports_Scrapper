from io import StringIO
import pandas as pd
import os.path
from os import path

class SaveLoad:
    def saveplayer(element,file_name):
        df = pd.read_csv(StringIO(element.text[80:]), sep=",")
        df.drop(list(df.loc[(df['Unnamed: 2']=='Total')].index), inplace=True)
        df.to_csv("{}.csv".format(file_name), index=None)
        return()

    def checkexisting(file_name):
        if path.exists("{}.csv".format(file_name)):
            return(True)
        else:
            return(False)
    
    def saveteamdata(element,file_name):
        df = pd.read_csv(StringIO(element.text[80:]), sep=",")
        try:
            df.drop(list(df.loc[((df['Player']=='Team Total')|(df['Player']=='Opp Total'))].index), inplace=True)
            df.drop(columns=['Player-additional'], inplace=True)
        except KeyError:
            df.drop(list(df.loc[((df['Unnamed: 1']=='Team Total')|(df['Unnamed: 1']=='Opp Total'))].index), inplace=True)
            df.drop(columns=['-additional'], inplace=True)
        df.to_csv("{}.csv".format(file_name), index=None)
        return()