import json
from resources import const
from datetime import datetime

class Matches:

    def __init__(self):
        self.matchDump = {}

    def setMatchState(self, accessToken, newState):
        self.matchDump[accessToken].gameState = newState

    def getMatchState(self, accessToken):
        return self.matchDump[accessToken].gameState

    def newStateExists(self, accessToken, whosTurn):
        return self.matchDump[accessToken].gameState['whosTurn'] != whosTurn

    def addMatch(self, accessToken, newMatch):
        self.matchDump[accessToken] = newMatch

    def tokenExists(self, token):
        return token in self.matchDump

    def addToDBQueue(self, accessToken, nextMove):
        pass

    def checkWhosTurn(self, accessToken, userToken):
        matchData = self.matchDump[accessToken]
        whitesTurn = matchData.gameState['whosTurn'] == const.WHITE and userToken != matchData.whiteToken
        blacksTurn = matchData.gameState['whosTurn'] == const.BLACK and userToken != matchData.blackToken
        return (whitesTurn or blacksTurn)

    def getColor(self, accessToken, userToken):
        match = self.matchDump[accessToken]
        if(match.gameState['whosTurn'] == const.BLACK):
            return const.BLACK

        elif (match.gameState['whosTurn'] == const.WHITE):
            return const.WHITE

        else:
            return const.EMPTY
    
    def indexIsEmpty(self, accessToken, index):
        return self.matchDump[accessToken].gameState['boardState'][index[0]][index[1]] == const.EMPTY        

    def removeInactiveMatches(self):
        pass


class Match:

    def __init__(self):
        self.lastUpdated = datetime.now()
        self.gameState = {
            "whosTurn": const.BLACK,
            "boardState": [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ]
        }


    


class Model:
    def __init__():
        pass