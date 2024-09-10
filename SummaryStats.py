import pandas as pd
from PlayerTransform import PlayerTransform
import numpy
import math


class SummaryStats:
    def __init__(self):
        self.player_data = pd.read_csv('data files/players.csv')

    def createstats(self, file_name, index):
        summary = self.getsummary(file_name)
        flex = True if self.player_data.at[index, 'Roster Position'].split("/")[-1] == 'FLEX' else False
        row_entry = {
            'player':self.player_data.at[index, 'Name'],
            'team':self.player_data.at[index, 'TeamAbbrev'],
            'salary':self.player_data.at[index, 'Salary'],
            'position':self.player_data.at[index, 'Position'],
            'flex':flex,
            'avg':summary[0],
            'median':summary[1],
            'std':summary[2],
            'min':summary[3],
            'max':summary[4],
            'count':summary[5]
        }
        return(row_entry)

    def getplayers(self):
        summary_stats = {}
        players = list(self.player_data['Name'])
        for index, player in enumerate(players):
            player = PlayerTransform.transform(player)
            team = self.player_data.at[index, 'TeamAbbrev']
            file_name = "{}-{}".format(player, team)
            if self.player_data.at[index, 'Roster Position'] == 'DST':
                row_entry = self.dst(index)
            else:
                row_entry = self.createstats(file_name, index)
            summary_stats[file_name] = row_entry
        self.todataframe(summary_stats)

    def todataframe(self, summary_stats):
        df = pd.DataFrame.from_dict(summary_stats, orient='index', columns=['player','team','salary','position','flex','avg','median','std','min','max','count'])
        df.to_excel('data files/summary.xlsx')

    def getsummary(self, file_name):
        df = pd.read_csv("players/{}.csv".format(file_name))
        data = [float(x) for x in list(df.loc[2:, df.columns[-2]])]
        data = [x for x in data if math.isnan(x) == False]
        summary = [numpy.average(data),numpy.median(data),numpy.std(data),min(data),max(data),len(data)] if len(data) != 0 else ["","","","","",""]
        return(summary)

    def dst(self, index):
        row_entry = {
            'player':self.player_data.at[index, 'Name'],
            'team':self.player_data.at[index, 'TeamAbbrev'],
            'salary':self.player_data.at[index, 'Salary'],
            'position':self.player_data.at[index, 'Position'],
            'flex':False,
            'avg':self.player_data.at[index, 'AvgPointsPerGame'],
            'median':"",
            'std':"",
            'min':"",
            'max':"",
            'count':""
        }
        return(row_entry)

runner = SummaryStats()
runner.getplayers()