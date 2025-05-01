def reset():
    cmnd = str(input('Do you want to start again? y/n\n'))
    if cmnd == 'y':
        print('Restarting...')
        main()
    if cmnd == 'n':
        print()

def main():
    phr = str(input('\nWelcome to Character Counter! To start type your sentence\n')) # phr == phrase
    num = phr.count('')
    numspace = phr.count(' ')
    print('Number of symbols including spaces:', num-1)
    print('Number without spaces:', num-numspace-1)
    reset()
main()