for i in range(5):
    print(i)

    if(i == 4):
        break     # due to this the else statement not runs

else:    # if this part runs then it signifies that the loop is not breaked during execution it fully executed till the else condition without interruption
    print("The loop is ended and hence entered in else block")