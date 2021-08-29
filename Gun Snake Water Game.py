import random

winy = 0
winc = 0
i = 1
while (i <=10):
    lst = ["g", "s", "w"]
    print("Press \n  g---gun \n  w---water \n  s---snake ")
    print("Number of times left for Entry for allowns a result",10-i)
    choose = input()
    choice = random.choice(lst)
    if choice == choose:
        # print(" you win", winy + 1)
        winy=winy+1


    else:
        # print("computer win", winc + 1)
        winc = winc + 1

    i = i + 1
print("total times you win",winy)
print("total times computer win",winc)


