## made by Matteo Zappia aka Dear Teo. ##
    ########## Lucky Day! ##########

while True:

    import random

    print('''                                       ## made by Matteo Zappia aka Dear Teo. ##
                                          ############ Lucky Day! ############
                                   / type start for generate your random numbers / \r\n ''')


    start = input()
    print ('\r\n')

    if start == str("start" or "START"):
        for numero in range(5):
            valore = random.randint(1,90)
            print (valore)
        print ("\r\nThank you for using Lucky Day. ")
    else:
        print ("Failed.")

    loop = input ('Do you want other numbers? Y/N ')
    if loop == "Y" or loop == "y":
        continue
    else: print ("\r\nThank you for using Lucky Day. ")
    break 

