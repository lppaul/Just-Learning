import games

name = input('HELLO USER, WHAT WOULD YOU LIKE TO BE CALLED?')
teamList = ['']

print('Welcome,', name, '!\n')


while True:
    print('Please select from the following menu:'
          '\n1. View list of teams currently in league'
          '\n2. Add a team to the league'
          '\n3. Remove a team from the league'
          '\n4. Start a new game'
          '\n5. Exit game)')
    menuChoice = int(input())

    if menuChoice == 1:
        print(teamList)
        continue
    elif menuChoice == 2:
        print('Enter name of new team')
        teamName = input()
        teamList.append(teamName)
        continue
    elif menuChoice == 3:
        print('Enter name of team to remove')
        delName = input()
        for team in teamList:
            if delName == teamList[team]:
                del teamList[team]
        continue
    elif menuChoice == 4:
        games.Baseball.atBat('')
        continue
    elif menuChoice == 5:
        break


