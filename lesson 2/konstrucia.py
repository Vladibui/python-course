while True:
    print()
    print("vvedite kakoe-nibud chislo")
    x=input()
    if x=="stop":
        break
    else:
        if int(x)%2==0:
            print("chislo chetnoe")
        elif int(x)%2==1:
            print("chislo nechetnoe")
