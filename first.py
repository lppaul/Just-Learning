#simple program to test inputs and add and remove elements from a list

userList = ['paul', 'chuck', 'charles', 'kenny', 'griggs']

human = input('What is your name human?\n')

while True:
    print('Glad to have you here ' + human)
    print('\n\nWhat would you like to do today?')
    print('\n1. Go to main menu'
          '\n2. Print list of users'
          '\n3. Add user to list'
          '\n4. Delete user (you must know user number'
          '\n5. Exit Program')

    choice = int(input())

    if choice == 1:
        print('\nYou made choice 1 to go to the main menu which is not in the program yet.')
        continue
    elif choice == 2:
        for users in range(len(userList)):
            print(users, ". ", userList[users])
            continue
    elif choice == 3:
        option = input('\n\nPlease type the name of who you would like to add to the list')
        userList.append(option)
        print(userList)
        continue
    elif choice == 4:
        userNumber = int(input('Please type the user number: '))
        del userList[userNumber]
        print(userList[userNumber], " was deleted")
        continue
    elif choice == 5:
        print('Thank you for using the program!')
        break


print('\n\nprogram finish')
