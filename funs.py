import json
from random import randint


def bootUp():
    start =int(input("\t1 To Login:\n\t2 To Register:\n\t0 To exit\n\t"))
    if(start == 0):
        print("\tGood Bye...")
        exit()
    elif(start == 1):
        uId ,pWord = loginData()
        login(uId,pWord)
    elif(start == 2):
        regData()
    else:
        print("\tWrong Input Try Again..")
        

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
    regPw =input("\tEnter Password:")
    regPwCc=input("\tRe Enter Password:")
    while True:
        if(regPw != regPwCc):
            print("password wrong try again")
            regPw =input("\tEnter Password:")
            regPwCc=input("\tRe Enter Password:")
        else:
            break
    addUser(regId,regPwCc)

def addUser(uid,pw):
    with open("json/db.json","r")as dbRead:
        dbData =json.load(dbRead)
    newUser ={"id":uid,"pw":pw}
    dbData.append(newUser)
    with open("json/db.json","w")as dbWrite:
        json.dump(dbData,dbWrite)
    print("Account created complete")
        
  
def tokenGen(userId):
    token=userId
    uidL = len(userId)
    for num in range(0,uidL):
        ranN =randint(0,9)
        token += str(ranN * uidL)
        print(token)
    return token  


def login(uid,pw):
    with open ("json/db.json","r")as dbRead:
        dbData =json.load(dbRead)
    for num in range(0,len(dbData)):
        if(dbData[num]['id'] == uid):
            if(dbData[num]['pw']== pw):
                print("\tlogin completed\n")
                print("You login as " + dbData[num]['id'])
                logSt =True
                break
            else:
                print("worng Password Try Again")
                uid,pw = loginData()

    if logSt != True:
        print("login Failed")
        bootUp()
        
        