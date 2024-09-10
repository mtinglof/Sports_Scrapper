class PlayerTransform:
    def transform (player):
        if player[-3:] == 'Jr.':
            player = player[:-4]
        elif player[-3:] == 'Sr.':
            player = player[:-4]
        elif player[-3:] == "III":
            player = player[:-4]
        elif player[-2:] == "II":
            player = player[:-3]
        elif player[-1:] == "I":
            player = player[:-2]
        elif player == 'Gabe Davis':
            player = 'Gabriel Davis'
        elif player == 'Joshua Palmer':
            player = 'Josh Palmer'
        elif player == 'Dee Eskridge':
            player = "D'Wayne Eskridge"
        elif player == 'Drew Ogletree':
            player = 'Andrew Ogletree'
        elif player == 'Mitch Trubisky':
            player = 'Mitchell Trubisky'
        elif player == 'JaMycal Hasty':
            player = 'Jamycal Hasty'
        return(player)        