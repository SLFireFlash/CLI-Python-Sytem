import json
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


def login():
    print("add login functions here")
    #maybe
        
