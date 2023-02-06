from random import randint


def loginData():
    while True:
        uId = input("\tEnter User Id:")
        pWord = input("\tEnter Password:")
        if len(uId) == 0 and len(pWord == 0):
            print("Password or user Name Empty.")
            print("try again")
        else:
            return uId , pWord
        
def regData():
    regId =input("\tUser Name:")
    while True:
        if( regPWrod != regPWrodConfrom):
            print("Password did not match try again")
            regPWrod =input("\tPassword :")
            regPWrodConfrom = input("\tRe Enter Password:")
        else:
            return regId , regPWrodConfrom

def tokenGen(userId):
    numbers =[0,1,2,3,4,5,6,7,8,9];
    UidL = len(userId)
