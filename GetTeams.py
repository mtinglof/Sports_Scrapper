import pandas as pd


class GetTeams:
    def getreference(team):
        team_matrix = pd.read_excel('data files/team_matrix.xlsx')
        try:
            return(list(team_matrix.loc[team_matrix['dfk']==team]['reference'])[0])
        except IndexError:
            raise Exception("{} needs to be added to the matrix".format(team))