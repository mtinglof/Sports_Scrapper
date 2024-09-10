import pandas as pd
from MakeChrome import MakeChrome
from GetDataTable import DataTableExtract
from GetTeams import GetTeams
from SaveAndLoad import SaveLoad


class GetTeamData:
    def getteams():
        link = 'https://www.pro-football-reference.com/'
        web_driver = MakeChrome.make_chrome(link)

        team_data = pd.read_csv('data files/players.csv')
        teams = list(set(team_data['TeamAbbrev']))

        for team in teams:
            reference = GetTeams.getreference(team).lower()
            link = 'https://www.pro-football-reference.com/teams/{}/2022.htm'.format(reference)
            web_driver.get(link)
            SaveLoad.saveteamdata(DataTableExtract.getinjuries(web_driver, reference), "injury/{}_injury".format(team))
            SaveLoad.saveteamdata(DataTableExtract.gettabledata(web_driver,'passing'), "passing/{}_passing".format(team))
            SaveLoad.saveteamdata(DataTableExtract.gettabledata(web_driver,'rushing_and_receiving'), "offense/{}_offense".format(team))
            SaveLoad.saveteamdata(DataTableExtract.gettabledata(web_driver,'kicking'), "kicking/{}_kicking".format(team))

GetTeamData.getteams()