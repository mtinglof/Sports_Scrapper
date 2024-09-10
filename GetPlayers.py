from MakeChrome import MakeChrome
from GetDataTable import DataTableExtract
from SaveAndLoad import SaveLoad
import pandas as pd
from PlayerTransform import PlayerTransform

class GetPlayers:
    def getplayers():
        link = 'https://www.pro-football-reference.com/'
        web_driver = MakeChrome.make_chrome(link)

        player_data = pd.read_csv('data files/players.csv')
        team_matrix = pd.read_excel('data files/team_matrix.xlsx')
        players = list(player_data['Name'])

        for index, player in enumerate(players):
            player = PlayerTransform.transform(player)
            team = player_data.at[index, 'TeamAbbrev']
            file_name = "{}-{}".format(player, team)
            ## Set to True to refresh already found players, set to False to keep all avaliable information and add new information
            refresh = False
            ##
            if player_data.at[index, 'Roster Position'] != 'DST':
                team_name = list(team_matrix.loc[team_matrix['dfk']==team]['full team name'])[0]
                savestate_2021 = SaveLoad.checkexisting("players/{}/{}".format('2021',file_name))
                savestate_2022 = SaveLoad.checkexisting("players/{}/{}".format('2022',file_name))
                if (refresh == True) or (savestate_2021 == False) or (refresh == savestate_2022):
                    if DataTableExtract.getplayer(web_driver,player,team_name) == 1:
                        if savestate_2021 == False:
                            DataTableExtract.changeyear(web_driver)
                            SaveLoad.saveplayer(DataTableExtract.gettabledata(web_driver,'player_fantasy'),"players/{}/{}".format('2021',file_name))
                        if (refresh == True) or (refresh == savestate_2022):
                            DataTableExtract.changeyear(web_driver)
                            SaveLoad.saveplayer(DataTableExtract.gettabledata(web_driver,'player_fantasy'),"players/{}/{}".format('2022',file_name))


GetPlayers.getplayers()