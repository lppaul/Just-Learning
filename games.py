import random
import decimal

class Baseball:
    innings = 0
    inningsCounter = 1
    team1Temp = ''
    team2Temp = ''
    team1Runs = 0
    team2Runs = 0
    teamList = []
    teamWins = [0, 0, 0, 0, 0, 0, 0, 0]
    teamLosses = [0, 0, 0, 0, 0, 0, 0, 0]

    def atbat():
        outs = 0
        runs = 0

        while outs < 3:
            input('Press any key to swing')
            chance = random.randrange(1, 100)
            if chance <= 3:
                print('You scored a run!!!')
                runs += 1
            else:
                print('You got an out!')
                outs += 1
        if Baseball.innings % 2 == 0:
            Baseball.team1Runs += runs
        else:
            Baseball.team2Runs += runs
        Baseball.innings += 1
        Baseball.inningsCounter += .5

    def startgame():
        print('Welcome to the game, press any key to continue through the plays\n')

        while Baseball.innings <= 17 or Baseball.team2Runs == Baseball.team1Runs:
            if Baseball.innings % 2 == 0:
                print('It is the top of inning', int(Baseball.inningsCounter), 'and the', Baseball.team1Temp, 'are at bat')
            else:
                print('It is the bottom of inning', int(Baseball.inningsCounter), 'and the', Baseball.team2Temp, 'are at bat')
            Baseball.atbat()

        if Baseball.team1Runs > Baseball.team2Runs:
            print(Baseball.team1Temp, 'Wins with a score of ', Baseball.team1Runs, 'to', Baseball.team2Runs, '!')
        elif Baseball.team2Runs > Baseball.team1Runs:
            print(Baseball.team1Temp, 'Wins with a score of ', Baseball.team2Runs, 'to', Baseball.team1Runs, '!')


    def menu():
        name = input('HELLO USER, WHAT WOULD YOU LIKE TO BE CALLED?')

        print('Welcome,', name, '!\n')
        while True:
            print('\nPlease select from the following menu:'
                  '\n1. View list of teams currently in league'
                  '\n2. Add a team to the league'
                  '\n3. Remove a team from the league'
                  '\n4. Start a new game'
                  '\n5. Exit game)')
            menuChoice = int(input())

            if menuChoice == 1:
                print('***************STANDINGS**************')
                for x in range(len(Baseball.teamList)):
                    print('*', Baseball.teamList[x], ' W ', Baseball.teamList[x], ' L ', Baseball.teamList[x])
                    continue
                print('**************************************')
            elif menuChoice == 2:
                if len(Baseball.teamList) <= 7:
                    print('Enter name of new team')
                    teamName = input()
                    Baseball.teamList.append(teamName)
                    continue
                else:
                    print('Maximum number of teams already reached!')
                    continue
            elif menuChoice == 3:
                print('Enter name of team to remove')
                delName = input()
                for team in Baseball.teamList:
                    if delName == Baseball.teamList[team]:
                        del Baseball.teamList[team]
                continue
            elif menuChoice == 4:
                team1 = input('Please type the names of the first team who is playing today:')
                team2 = input('Please type the names of the second team who is playing today:')

                Baseball.game(team1, team2)
                Baseball.startgame()

            elif menuChoice == 5:
                print('Thank you for playing!')
                break

    def game(team1, team2):
        print('\n\nThe', team1, 'are playing the', team2, ', should be a great game!\n')
        Baseball.team1Temp = team1
        Baseball.team2Temp = team2
