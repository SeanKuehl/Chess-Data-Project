
import csv
textFile = open("bundout.txt", "r")

linesList = textFile.readlines()

game = []

gameList = []

for line in linesList:
    if "#" in line:
        gameList.append(game)
        game = []
    else:
        refinedLine = line.rstrip()
        refinedLine = refinedLine.split(",")
        itemOne = refinedLine[0]
        itemTwo = ','.join(refinedLine[1:])
        refinedLine = [itemOne, itemTwo]

        if refinedLine == ['', '']:
            pass
        else:
            game.append(refinedLine)
    

def PositionScoreMetricGeneration(game):

    
    gameHeaders = []
    whitePosScores = []
    blackPosScores = []

    for line in game:
        if line[0].isdigit():
            splitLine = line[1].split(",")

            if splitLine[0] == "None":
                pass
            else:
                whitePosScores.append(float(splitLine[0]))

            if splitLine[1] == "None":
                pass
            else:
                blackPosScores.append(float(splitLine[1]))
        else:
            gameHeaders.append(line)


    #the metric is max-min of each side averaged with each other.
    #the higher the metric, the more exciting the game is
    whiteComponent = max(whitePosScores) - min(whitePosScores)
    blackComponent = max(blackPosScores) - min(blackPosScores)
    metric = (whiteComponent + blackComponent) / 2
    metric = round(metric, 2)

    gameHeaders.append(["ExcitementScore", metric])


    #more refinement to check for missing vals before putting on csv
    refinedHeaders = {}
    headerList = ['Date', 'Round', 'Result', 'BlackElo', 'BlackTitle', 'ECO', 'Opening', 'Variation', 'WhiteElo', 'WhiteTitle', 'ExcitementScore']

    for header in headerList:
        refinedHeaders[header] = "None"

    for header in gameHeaders:
        if header[0] in headerList:
            refinedHeaders[header[0]] = header[1]

    




    return refinedHeaders
    
            
refinedGameList = []

for game in gameList:
    refinedGameList.append(PositionScoreMetricGeneration(game))

header = ['Date', 'Round', 'Result', 'BlackElo', 'BlackTitle', 'ECO', 'Opening', 'Variation', 'WhiteElo', 'WhiteTitle', 'ExcitementScore']

with open('bundesliga.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = header)
    writer.writeheader()

    for game in refinedGameList:
        writer.writerow(game)
