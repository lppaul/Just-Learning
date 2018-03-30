appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt', 'a')
appendFile.write('\n')
appendFile.write(appendMe)
appendFile.close