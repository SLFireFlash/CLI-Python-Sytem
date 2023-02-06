import funs

while True:
    start =int(input("\t1 To Login:\n\t2 To Register:\n\t0 To exit\n\t"))
    if(start == 0):
        print("\tGood Bye...")
        exit()
    elif(start == 1):
        uId , pWord = funs.loginData()
        break
    elif(start == 2):
        regId ,regPw = funs.regData()
        break
    else:
        print("\tWrong Input Try Again..")

        

